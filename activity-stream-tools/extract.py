
import requests
import json
import sys
import time

from pprint import pprint

embedly_proxy = "https://embedly-proxy.dev.mozaws.net/v2/extract"
fathom_proxy = "https://metadata.dev.mozaws.net/"
prod_proxy = "https://embedly-proxy.services.mozilla.com/v2/extract"

def diff_objs(obj1, obj2):
    d1 = obj1['urls'][sys.argv[1]]
    d2 = obj2['urls'][sys.argv[1]]
    for key in d1:
        print key
        print ("fathom : %s" % (d1[key]))
        if key not in ['icon_url', 'image_url']:
            print ("embedly: %s" % (d2[key]))

def extract(url, server):
    beg_ts = time.time()
    response = requests.post(server,
                             data=json.dumps({'urls': [url]}),
                             headers={'content-type':'application/json'})
    end_ts = time.time()
    print("server request time: %f" % (end_ts - beg_ts))
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return 'ERROR'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: python extract_sample.py url')
        sys.exit(1)
    print 'extracting: ', sys.argv[1]
    print
    print 'fathom:'
    f_obj = extract(sys.argv[1], fathom_proxy)
    # pprint(f_obj)
    print 'embedly:'
    e_obj = extract(sys.argv[1], prod_proxy)
    # pprint(e_obj)
    print 'diff:'
    print diff_objs(f_obj, e_obj)

