import sys
import requests
# import urlparse
# import os

class WebError(Exception):
    def __init__(self, r):
        self.r = r
        self.args = (r, r.content)
        sys.exit(1)

RESTMAILURL = "http://restmail.net/mail/"

def getRestmailLink(email):
    try:
      r = requests.get("%s%s" % (RESTMAILURL, email))
      if r.status_code != 200:
          raise WebError(r)
      restmail_dict = r.json()
    except:
        print '*** FAIL: No data for restmail.net acct'
        sys.exit(1)
    assert len(restmail_dict)
     
    return restmail_dict[-1]['headers']['x-link']