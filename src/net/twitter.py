#!/usr/bin/env python

import requests
import urllib
import urllib2

ID_USERNAME = 'signup-user-name'
ID_EMAIL = 'signup-user-email'
ID_PASSWORD = 'signup-user-password'
USERNAME = 'y'
EMAIL = '@hotmail.com'
PASSWORD = ''
SIGNUP_URL = 'https://twitter.com/i/flow/signup'

def submit_form():
    payload = { ID_USERNAME : USERNAME,
                ID_EMAIL : EMAIL,
                ID_PASSWORD : PASSWORD,
    }

    # make a get request
    resp = requests.get(SIGNUP_URL)
    print "Response to GET request: %s" %resp.content

    # send a POST request
    resp = requests.post(SIGNUP_URL, payload)
    print "Headers from a POST request response: %s" %resp.headers

if __name__ == '__main__':
    submit_form()
