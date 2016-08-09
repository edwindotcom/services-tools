# encoding=utf8  

import requests
import json
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

from pprint import pprint

embedly_proxy = "https://embedly-proxy.dev.mozaws.net/v2/extract"
fathom_proxy = "https://metadata.dev.mozaws.net/"
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
    d1 = obj1['urls'][url]
    if 'urls' in obj2.keys():
        if url in obj2['urls'].keys():
            d2 = obj2['urls'][url]
    try:
        for key in d1:
            print '#####', key
            print ("###FATHOM : %s" % (d1[key]))
            if key not in ['icon_url', 'image_url']:
                print ("###EMBEDLY: %s" % (d2[key]))
    except:
        print '### could not parse'

def strip_chars(st):
    return st.replace(u"\u2018", "'").replace(u"\u2019", "'")

def extract(url, server):
    beg_ts = time.time()
    response = requests.post(server,
                             data=json.dumps({'urls': [url]}),
                             headers={'content-type':'application/json'})
    end_ts = time.time()
    print 'extract: ', url
    print("###%s request time: %f" % (server[0:10], end_ts - beg_ts))
    if response.status_code == 200:
        return json.loads(strip_chars(response.content))
    else:
        return 'ERROR'

if __name__ == '__main__':
    h_urls =  load_json_file('data.json')
    pprint(h_urls)
    for url in h_urls:
        f_obj = extract(url, fathom_proxy)
        e_obj = extract(url, prod_proxy)
        diff_objs(f_obj, e_obj, url)

