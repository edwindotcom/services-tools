from selenium import webdriver
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import time

# OAUTH_RP = "https://123done.dev.lcip.org/"
OAUTH_RP = "http://edwong.mozcloud.org"

btn_signin_locator = "button.signin"
btn_signup_locator = "button.signup"
input_email = "input.email"
input_password = "input.password"
btn_submit = "submit-btn"

fxa_user = 'fxa.test.acct@restmail.net'
fxa_password = '12345678'

class ManualTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
           command_executor='http://127.0.0.1:4444/wd/hub',
           desired_capabilities=DesiredCapabilities.SAFARI)
        self.driver.implicitly_wait(30)

    def test_basic_page(self):
        self.driver.get(OAUTH_RP)
        assert '123 Done' in self.driver.title
        self.driver.find_element_by_css_selector(btn_signin_locator).click()
        time.sleep(10)
        # assert 'Firefox' in self.driver.title

        username = self.driver.find_element_by_css_selector(input_email)
        username.send_keys(fxa_user)
        pw = self.driver.find_element_by_css_selector(input_password)
        pw.send_keys(fxa_password)
        self.driver.find_element_by_id(btn_submit).click()

        # WebDriverWait(self.driver, 5).until(
        #         lambda d: d.find_element_by_css_selector(btn_signin_locator).is_displayed())
        # time.sleep(2)
        btn_is_displayed = self.driver.find_element_by_css_selector(btn_signin_locator).is_displayed()

        assert btn_is_displayed
        assert '123 Done' in self.driver.title

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
