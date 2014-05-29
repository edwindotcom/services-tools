import json
from pprint import pprint
with open('sauce.json') as data_file:    
    data = json.load(data_file)

print "chosen_browsers = ["
for item in data:
    if 'webdriver' in item['backends']:
        os = item['os']
        ver = item['short_version']
        browser = item['name']
        if 'Windows' in os:
            os = item['os_display']
        if 'Mac' in os:
            os = os.replace('Mac', 'OS X')
        if 'googlechrome' in browser:
            browser = browser.replace('googlechrome', 'chrome')
        if '5' in ver or '10.6' in os or 'XP' in os or 'lynx' in browser:
            continue
        if 'firefox' in browser and float(ver) < 26:
            continue
        if ver != 'beta':
            if 'chrome' in browser and float(ver) < 27:
                continue
        print "    ('%s', '%s', '%s')," % (os, browser, ver)

print ']'
