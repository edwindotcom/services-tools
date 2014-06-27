#!/usr/bin/env python
# encoding: utf-8

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
import os

import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


FXA_ROOT = os.getenv('PUBLIC_URL', "https://accounts.stage.mozaws.net/")
if FXA_ROOT[-1:] != '/':
    FXA_ROOT += "/"

FMD_URL = "https://fmd.stage.mozaws.net"
OAUTH_SIGNIN = "https://accounts.stage.mozaws.net/oauth/"

FXA_SIGNIN = FXA_ROOT + 'signin'
FXA_SIGNUP = FXA_ROOT + 'signup'
FXA_SETTINGS = FXA_ROOT + 'settings'
FXA_DELETE = FXA_ROOT + 'delete_account'
FXA_CHANGE_PW = FXA_ROOT + 'change_password'

signin_locator = "Sign in"
btn_signin_locator = "button.signin"
btn_signup_locator = "button.signup"
input_email = "input.email"
input_password = "input.password"
btn_submit = "submit-btn"
signed_in_locator = "p.signed-in-email-message"
signed_in_text = 'You are signed in as'

header_locator = 'h1'
loading_locator = 'h2'
map_locator = 'leaflet-map-pane'

# fxa_exist_user = 'fxa.test.acct@restmail.net'
fxa_exist_user = 'ed777@restmail.net'

user_name = fxa_exist_user.split('@')[0]
fxa_password = '12345678'


class FMDTest(unittest.TestCase):

    def setUp(self):
        des_caps = {'browserName':'firefox'}
        des_caps['loggingPrefs'] = { 'browser':'ALL' }
        self.driver = webdriver.Remote(desired_capabilities=des_caps)
        self.driver.implicitly_wait(60)

    def wait_leave_page(self, current_url):
        while(self.driver.current_url == current_url):
            # print 'wait', self.driver.current_url
            time.sleep(3)
        return True

    def test_fmd(self):
        # sign into FMD
        # click sign in link
        self.driver.get(FMD_URL)
        self.driver.find_element_by_link_text(signin_locator).click()
        self.wait_leave_page(FMD_URL)

        # enter user:pw
        # assert 'Find' in 
        time.sleep(5)
        print self.driver.title
        username = self.driver.find_element_by_css_selector(input_email)
        username.send_keys(fxa_exist_user)

        pw = self.driver.find_element_by_css_selector(input_password)
        pw.send_keys(fxa_password)
        self.driver.find_element_by_id(btn_submit).click()
        time.sleep(5)

        # should be on finding phone page
        header = self.driver.find_element_by_css_selector(header_locator)
        # print 'header', header.get_attribute("innerHTML")
        assert(user_name in header.get_attribute("innerHTML"))

        time.sleep(60)

        fmd_map = self.driver.find_element_by_class_name(map_locator)
        for item in fmd_map:
            print item

        ## if not found - this should work:
        # loading = self.driver.find_element_by_css_selector(loading_locator)
        # print 'loading', loading.get_attribute("innerHTML")

    def tearDown(self):
        # self.driver.quit()
        # leave the browser open for now
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)

# parser = OptionParser(usage="usage: %prog [options] runType {smoke|oauth|full}")
# parser.add_option("-p", "--platforms",
#                   help="comma seperated list of platforms to run: %s" % platform_types)
# parser.add_option("--local",
#                   action='store_true',
#                   help="option to run against run_local selenium server")
# options, args = parser.parse_args()


