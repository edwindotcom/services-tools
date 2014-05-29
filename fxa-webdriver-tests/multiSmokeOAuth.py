#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
import unittest
import nose
from nose.plugins.multiprocess import MultiProcess
import new
import json
import httplib
import base64
import os
import sys
import time

chosen_browsers = [
    ('Windows 7', 'chrome', '34'),
    ('OS X 10.8', 'chrome', '34'),
    ('Linux', 'chrome', '34'),

    ('Windows 7', 'firefox', '29'),
    ('Windows 8', 'chrome', '34'),
    ('Windows 8', 'firefox', '29'),
    ('Windows 8', 'internet explorer', '10'),
    ('OS X 10.9', 'firefox', '28'),
    ('Linux', 'firefox', '29'),
    ('OS X 10.9', 'safari', '7'),

    ('linux', 'android', '4'),
    ('MAC', 'iPhone', '6'), # 7.x not working
]

user = os.environ.get('PERSONA_SAUCE_USER')
key = os.environ.get('PERSONA_SAUCE_APIKEY')

# OAUTH_RP = "https://123done.dev.lcip.org"
OAUTH_RP = "http://edwong.mozcloud.org"

btn_signin_locator = "button.signin"
btn_signup_locator = "button.signup"
input_email = "input.email"
input_password = "input.password"
btn_submit = "submit-btn"

fxa_user = 'fxa.test.acct@restmail.net'
fxa_password = '12345678'


class FxaOAuthTest(unittest.TestCase):
    # Nose won't run the original Test Class, we'll change this in the
    # dynamically generated classes
    __test__ = False

    def setUp(self):
        des_caps = {
                # The following properties are set dynamically
                'platform': self.os,
                'browserName': self.br,
                'version': self.version,
                'name': self.name,
                # "selenium-version": "2.41.0"
                }
        # instantiate the browser
        self.driver = webdriver.Remote(desired_capabilities=des_caps,
                                       command_executor="http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
                                       % (user, key))
        self.driver.implicitly_wait(60)

    def _exc_info(self):
        """Return a version of sys.exc_info() with the traceback frame
           minimised; usually the top level of the traceback frame is not
           needed.
        """
        return sys.exc_info()

    def test_return_oauth(self):
        self.driver.get(OAUTH_RP)
        assert '123 Done' in self.driver.title
        # print self.driver.page_source
        self.driver.find_element_by_css_selector(btn_signin_locator).click()

        username = self.driver.find_element_by_css_selector(input_email)
        username.send_keys(fxa_user)
        self.assertTrue('Sign in to 123done' in self.driver.title)
        pw = self.driver.find_element_by_css_selector(input_password)
        pw.send_keys(fxa_password)
        self.driver.find_element_by_id(btn_submit).click()

        # print self.driver.current_url

        # TODO: Need https in my awsbox instance
        # btn_is_displayed = self.driver.find_element_by_css_selector(btn_signin_locator).is_displayed()

        # self.assertTrue(btn_is_displayed)


    def report_pass_fail(self):
        # Sauce doesn't really know what the test in your end does with the
        # browser, let us know
        base64string = base64.encodestring('%s:%s' % (user, key))[:-1]
        result = json.dumps({'passed': self._exc_info() == (None, None, None)})
        connection = httplib.HTTPConnection('saucelabs.com')
        connection.request('PUT', '/rest/v1/%s/jobs/%s' % (user,
                                                           self.driver.session_id),
                           result,
                           headers={"Authorization": "Basic %s" % base64string})
        result = connection.getresponse()
        return result.status == 200

    def tearDown(self):
        self.report_pass_fail()
        self.driver.quit()

# Here's where the magic happens
classes = {}
for os, browser, version in chosen_browsers:
    # Make a new class name for the actual test cases
    name = "%s_%s_%s_%s" % (FxaOAuthTest.__name__, os, browser, version)
    name = name.encode('ascii')
    if name.endswith("."): name = name[:-1]
    for x in ".-_":
        name = name.replace(x, " ")

    # Copy the magic __dict__ from the original class
    d = dict(FxaOAuthTest.__dict__)
    # Update the new class' dict with a new name and a __test__ == True
    d.update({'__test__': True,
              '__name__': name,
              # Set these properties dynamically, the test uses them to
              # instantiate the browser
              'name': name,
              'os': os,
              'br': browser,
              'version': version
             })

    # append the new class to the classes dict
    classes[name] = new.classobj(name, (FxaOAuthTest,), d)

# update the global context (believe it or not, it's a dict), with the new
# classes we just dynamically generated
globals().update(classes)

# this is just handy. If __main__, just run the tests in multiple processes
if __name__ == "__main__":
    nose.core.run(argv=["nosetests", "-vv",
                        "--processes", len(chosen_browsers),
                        "--process-timeout", 180,
                        __file__],
                  plugins=[MultiProcess()])
