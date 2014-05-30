#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
import unittest
import json
import httplib
import base64
import os
import sys
import time

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


class FxaTestCase(unittest.TestCase):
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

    def tearDown(self):
        self.report_pass_fail()
        self.driver.quit()
