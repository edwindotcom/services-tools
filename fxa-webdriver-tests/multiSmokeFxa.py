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
    # ('MAC', 'firefox', ''), # LOCAL

    ('Windows 7', 'chrome', '34'),
    ('OS X 10.8', 'chrome', '34'),
    ('Linux', 'chrome', '28'),

    ('Windows 7', 'firefox', '29'),
    ('Windows 8', 'chrome', '34'),
    ('Windows 8', 'firefox', '29'),
    ('Windows 8', 'internet explorer', '10'),
    ('Windows 8.1', 'internet explorer', '11'),
    ('Windows 7', 'internet explorer', '11'),
    ('Windows 7', 'internet explorer', '10'),
    ('OS X 10.9', 'firefox', '28'),
    ('Linux', 'firefox', '29'),
    ('OS X 10.9', 'safari', '7'),

    ('linux', 'android', '4'),
    ('MAC', 'iPhone', '6'), # 7.x not working
]

user = os.environ.get('PERSONA_SAUCE_USER')
key = os.environ.get('PERSONA_SAUCE_APIKEY')

FXA = "https://accounts.firefox.com/signin"

btn_signin_locator = "button.signin"
btn_signup_locator = "button.signup"
input_email = "input.email"
input_password = "input.password"
btn_submit = "submit-btn"
signed_in_locator = "p.signed-in-email-message"
signed_in_text = 'You are signed in as'

fxa_user = 'fxa.test.acct@restmail.net'
fxa_password = '12345678'


class FxaTest(unittest.TestCase):
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
                                       # command_executor='http://127.0.0.1:4444/wd/hub')
                                       % (user, key))
        self.driver.implicitly_wait(60)

    def _exc_info(self):
        """Return a version of sys.exc_info() with the traceback frame
           minimised; usually the top level of the traceback frame is not
           needed.
        """
        return sys.exc_info()

    def test_fxa_signin(self):
        self.driver.get(FXA)
        time.sleep(2)
        assert 'Sign in' in self.driver.title

        username = self.driver.find_element_by_css_selector(input_email)
        username.send_keys(fxa_user)
        time.sleep(2)
        pw = self.driver.find_element_by_css_selector(input_password)
        pw.send_keys(fxa_password)
        self.driver.find_element_by_id(btn_submit).click()

        # print self.driver.current_url

        while(self.driver.current_url == FXA):
            # print 'wait', self.driver.current_url
            time.sleep(3)

        signout_link = self.driver.find_element_by_id('signout')

        signed_in_node = self.driver.find_element_by_css_selector(signed_in_locator)
        assert("Sign out" in signout_link.get_attribute("innerHTML"))
        assert(fxa_user in signed_in_node.get_attribute("innerHTML"))

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

classes = {}
for os, browser, version in chosen_browsers:
    # Make a new class name for the actual test cases
    name = "%s_%s_%s_%s" % (FxaTest.__name__, os, browser, version)
    name = name.encode('ascii')
    if name.endswith("."): name = name[:-1]
    for x in ".-_":
        name = name.replace(x, " ")

    # Copy the magic __dict__ from the original class
    d = dict(FxaTest.__dict__)
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
    classes[name] = new.classobj(name, (FxaTest,), d)

globals().update(classes)

# this is just handy. If __main__, just run the tests in multiple processes
if __name__ == "__main__":
    nose.core.run(argv=["nosetests", "-vv",
                        "--processes", len(chosen_browsers),
                        "--process-timeout", 120,
                        __file__],
                  plugins=[MultiProcess()])
