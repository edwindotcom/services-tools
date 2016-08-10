# encoding=utf8  

import requests
import json
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

from pprint import pprint

embedly_proxy = "https://embedly-proxy.dev.mozaws.net/v2/extract"
fathom_proxy = "https://metadata.dev.mozaws.net/v1/metadata"
prod_proxy = "https://embedly-proxy.services.mozilla.com/v2/extract"


def load_json_file(file):
    with open(file) as data_file:
        data = json.load(data_file)

    # print data['raw']['Highlights']
    urls = []
    for row in data['raw']['Highlights']['rows']:
        urls.append(row['url'])
    return urls

def diff_objs(obj1, obj2, url):
    try:
        d1 = obj1['urls'][url]
        d2 = obj2['urls'][url]
        for key in d1:
            print
            print ':::', key
            print ("FATHOM : %s" % (d1[key]))
            if key not in ['icon_url', 'image_url']:
                print ("EMBEDLY: %s" % (d2[key]))
    except e:
        print '### COULD NOT PARSE %s ### - Error: %s' % (url, e)

def strip_chars(st):
    return st.replace(u"\u2018", "'").replace(u"\u2019", "'")

def extract(url, server):
    beg_ts = time.time()
    response = requests.post(server,
                             data=json.dumps({'urls': [url]}),
                             headers={'content-type':'application/json'})
    end_ts = time.time()
    print(":::request time: %f - %s" % (end_ts - beg_ts, server) )
    if response.status_code == 200:
        return json.loads(strip_chars(response.content))
    else:
        return 'ERROR'

if __name__ == '__main__':
    h_urls =  load_json_file('data.json')
    pprint(h_urls)
    print '------------'
    for url in h_urls:
        print
        print "*** PARSING: %s ***" % url
        f_obj = extract(url, fathom_proxy)
        e_obj = extract(url, prod_proxy)
        diff_objs(f_obj, e_obj, url)

