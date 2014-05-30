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
    ('Linux', 'android', '4.3'),
    ('Linux', 'android', '4.2'),
    ('Linux', 'android', '4.1'),
    ('Linux', 'android', '4.0'),
    ('OS X 10.8', 'iphone', '6.1'),
    ('OS X 10.8', 'iphone', '6.0'),
    ('OS X 10.8', 'ipad', '6.1'),
    ('OS X 10.8', 'ipad', '6.0'),
    ('OS X 10.9', 'iphone', '7.1'),
    ('OS X 10.9', 'iphone', '7.0'),
    ('OS X 10.9', 'ipad', '7.1'),
    ('OS X 10.9', 'ipad', '7.0'),
    ('Windows 8.1', 'iexplore', '11'),
    ('Windows 8.1', 'firefox', '26'),
    ('Windows 8.1', 'firefox', '27'),
    ('Windows 8.1', 'firefox', '28'),
    ('Windows 8.1', 'firefox', '29'),
    ('Windows 8.1', 'chrome', '27'),
    ('Windows 8.1', 'chrome', '28'),
    ('Windows 8.1', 'chrome', '29'),
    ('Windows 8.1', 'chrome', '30'),
    ('Windows 8.1', 'chrome', '31'),
    ('Windows 8.1', 'chrome', '32'),
    ('Windows 8.1', 'chrome', '33'),
    ('Windows 8.1', 'chrome', '34'),
    ('Windows 8.1', 'chrome', 'beta'),
    ('Windows 7', 'iexplore', '9'),
    ('OS X 10.9', 'firefox', '26'),
    ('OS X 10.9', 'firefox', '27'),
    ('OS X 10.9', 'firefox', '28'),
    ('OS X 10.9', 'safari', '7'),
    ('OS X 10.9', 'chrome', '31'),
    ('OS X 10.9', 'chrome', '32'),
    ('OS X 10.9', 'chrome', '33'),
    ('OS X 10.9', 'chrome', '34'),
    # ('Windows 7', 'iexplore', '8'),
    # ('Windows 7', 'opera', '11'),
    # ('Windows 7', 'opera', '12'),
    # ('Windows 7', 'iexplore', '10'),
    # ('Windows 7', 'firefox', '26'),
    # ('Windows 7', 'firefox', '27'),
    # ('Windows 7', 'firefox', '28'),
    # ('Windows 7', 'firefox', '29'),
    # ('Windows 7', 'chrome', '27'),
    # ('Windows 7', 'chrome', '28'),
    # ('Windows 7', 'chrome', '29'),
    # ('Windows 7', 'chrome', '30'),
    # ('Windows 7', 'chrome', '31'),
    # ('Windows 7', 'chrome', '32'),
    # ('Windows 7', 'chrome', '33'),
    # ('Windows 7', 'chrome', '34'),
    # ('Windows 7', 'chrome', 'beta'),
    # ('Windows 8', 'iexplore', '10'),
    # ('Windows 8', 'firefox', '26'),
    # ('Windows 8', 'firefox', '27'),
    # ('Windows 8', 'firefox', '28'),
    # ('Windows 8', 'firefox', '29'),
    # ('Windows 8', 'chrome', '27'),
    # ('Windows 8', 'chrome', '28'),
    # ('Windows 8', 'chrome', '29'),
    # ('Windows 8', 'chrome', '30'),
    # ('Windows 8', 'chrome', '31'),
    # ('Windows 8', 'chrome', '32'),
    # ('Windows 8', 'chrome', '33'),
    # ('Windows 8', 'chrome', '34'),
    # ('Windows 8', 'chrome', 'beta'),
    # ('Windows 7', 'iexplore', '11'),
    # ('OS X 10.8', 'safari', '6'),
    # ('OS X 10.8', 'chrome', '27'),
    # ('OS X 10.8', 'chrome', '28'),
    # ('OS X 10.8', 'chrome', '31'),
    # ('OS X 10.8', 'chrome', '32'),
    # ('OS X 10.8', 'chrome', '33'),
    # ('OS X 10.8', 'chrome', '34'),
    # ('OS X 10.8', 'chrome', 'beta'),
    # ('Linux', 'opera', '12'),
    # ('Linux', 'firefox', '26'),
    # ('Linux', 'firefox', '27'),
    # ('Linux', 'firefox', '28'),
    # ('Linux', 'firefox', '29'),
    # ('Linux', 'chrome', '27'),
    # ('Linux', 'chrome', '28'),
    # ('Linux', 'chrome', '29'),
    # ('Linux', 'chrome', '30'),
    # ('Linux', 'chrome', '31'),
    # ('Linux', 'chrome', '32'),
    # ('Linux', 'chrome', '33'),
    # ('Linux', 'chrome', '34'),
]

user = os.environ.get('PERSONA_SAUCE_USER')
key = os.environ.get('PERSONA_SAUCE_APIKEY')

FXA = "https://accounts.firefox.com/signin"
# FXA = "https://nightly.dev.lcip.org/signin"
# FXA = "https://latest.dev.lcip.org/signin"

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
                # "selenium-version": "2.42.0"
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
                        "--process-timeout", 500,
                        __file__],
                  plugins=[MultiProcess()])
