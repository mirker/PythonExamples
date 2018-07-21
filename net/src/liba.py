#!/usr/bin/env python

import cookielib
import urllib
import urllib2

ID_USERNAME = 'id_username'
ID_PASSWORD = 'id_password'
USERNAME = ''
PASSWORD = ''

#LOGIN_URL = 'https://passport.liba.com/login.htm'
#NORMAL_URL= 'https://www.liba.com'
LOGIN_URL = 'https://signin.ebay.com/ws/eBayISAPI.dll?SignIn'
NORMAL_URL = 'https://www.ebay.com'


def extract_cookie_info():
    """ Fake login to a site with cookie """
    # setup cookie jar
    cj = cookielib.CookieJar()
    login_data = urllib.urlencode({ID_USERNAME : USERNAME,
                                   ID_PASSWORD : PASSWORD})
    # create url opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    resp = opener.open(LOGIN_URL, login_data)

    # send login info
    for cookie in cj:
        print "----First time cookie: %s --> %s" % (cookie.name, cookie.value)
    print "Headers: %s" %resp.headers

    # now access without any login info
    resp = opener.open(NORMAL_URL)
    for cookie in cj:
        print "++++Second time cookie: %s --> %s" %(cookie.name, cookie.value)
    print "Headers: %s" %resp.headers

if __name__ == "__main__":
    extract_cookie_info()
