#! python
# copy from https://blog.csdn.net/lanbing510/article/details/48633427
import shutil
import os
import time
import exifread
import sys


class ReadFailException(Exception):
    pass


def getOrignalDate(filename):
    try:
        fd = open(filename, 'rb')
    except:
        print("Cannot open: ", filename)
        raise ReadFailException
    data = exifread.process_file(fd)
    if data:
        try:
            t = data['EXIF DateTimeOriginal']
            return str(t).replace(":", ".")[:7]
        except:
            print("No exif: ", filename)
            pass
    state = os.stat(filename)
    print("get state", filename)
    return time.strftime("%Y.%m", time.localtime(state[-2]))


def classify_pics(file_url):
    for root, dirs, files in os.walk(file_url, True):
        dir = []
        for filename in files:
            filename = os.path.join(root, filename)
            f, e = os.path.splitext(filename)
            if e.lower() not in ('.jpg', '.png', '*.mp4'):
                continue
            info = "Filename: " + filename + " "
            t = ""
            try:
                t = getOrignalDate(filename)
            except Exception:
                print("cannot get time", filename)
                continue
            info = info + "Taken time: " + t + " "
            pwd = sys.argv[1] + '\\' + t
            if not os.path.exists(pwd):
                os.mkdir(pwd)
            print(info, pwd)
            shutil.copy2(filename, pwd)
            # os.remove(filename)


if __name__ == '__main__':
    path = sys.argv[2]
    classify_pics(path)
