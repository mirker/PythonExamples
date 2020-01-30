#!/usr/bin/env python3
def between_markers(text, begin=None, end=None):
    """
        returns substring between two given markers
    """
    # your code here
    if begin == None and end == None:
        return text
    substr_start = 0
    substr_end = 0
    
    if begin == None:
        substr_start = 0
        sbustr_end = text.find(end)

    if end == None:
        sutstr_start = text.find(begin)
        substr_end = len(text)
        
    if begin != None and end != None:
        substr_start = text.find(begin)
        substr_end = text.find(end)
        #print(substr_start, substr_end)
        print(text[substr_start:substr_end])
        
    if substr_start >= substr_end:
        return ''
    else:
        return text[substr_start:substr_end]

    return ''


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
