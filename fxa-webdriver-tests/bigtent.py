#!/usr/bin/env python

import unittest
from selenium import webdriver
import time

class TestYahooBigtent(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def testYahooNegative(self):
        self.browser.get('http://beta.123done.org/')
        time.sleep(4)
        signup = self.browser.find_element_by_css_selector("li#loggedout button img")
        signup.click()
        time.sleep(2)
        self.browser.switch_to_window('__persona_dialog')
        time.sleep(1)
        email = self.browser.find_element_by_id('authentication_email')
        email.send_keys('karl_H_thiessen@yahoo.com')
        time.sleep(1)
        nnext = self.browser.find_element_by_css_selector('p.submit.buttonrow button.start')
        nnext.click()
        time.sleep(3)
        nverify = self.browser.find_element_by_css_selector('button#verifyWithPrimary')
        nverify.click()
        time.sleep(5)
        # self.browser.switch_to_window('auth_with_primary')
        # time.sleep(5)
        # print self.browser.page_source
        username = self.browser.find_element_by_id('username')
        username.send_keys('karl_thiessen@yahoo.com')
        passwd = self.browser.find_element_by_id('passwd')
        passwd.send_keys('PASSWORD')
        save = self.browser.find_element_by_name('.save')
        save.click()
        # self.browser.switch_to_window('')
        time.sleep(10)
        assert "different address" in self.browser.page_source
        
    def testYahooPositive(self):
        self.browser.get('http://beta.123done.org/')
        time.sleep(4)
        signup = self.browser.find_element_by_css_selector("li#loggedout button img")
        signup.click()
        time.sleep(2)
        self.browser.switch_to_window('__persona_dialog')
        time.sleep(1)
        email = self.browser.find_element_by_id('authentication_email')
        email.send_keys('karl_thiessen@yahoo.com')
        time.sleep(1)
        nnext = self.browser.find_element_by_css_selector('p.submit.buttonrow button.start')
        nnext.click()
        time.sleep(3)
        # self.browser.switch_to_window('auth_with_primary')
        # time.sleep(5)
        # print self.browser.page_source
        username = self.browser.find_element_by_id('username')
        username.send_keys('karl_thiessen@yahoo.com')
        passwd = self.browser.find_element_by_id('passwd')
        passwd.send_keys('PASSWORD')
        save = self.browser.find_element_by_name('.save')
        save.click()
        self.browser.switch_to_window('')
        time.sleep(10)
        assert "logout" in self.browser.page_source


    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
