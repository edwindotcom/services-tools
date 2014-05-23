from selenium import webdriver
import unittest
import os

user = os.environ.get('PERSONA_SAUCE_USER')
key = os.environ.get('PERSONA_SAUCE_APIKEY')

OAUTH_RP = "https://123done.dev.lcip.org/"

btn_signin_locator = "button.signin"
btn_signup_locator = "button.signup"
input_email = "input.email"
input_password = "input.password"
btn_submit = "submit-btn"

fxa_user = 'fxa.test.acct@restmail.net'
fxa_password = '12345678'

class ManualTest(unittest.TestCase):

    def setUp(self):
        des_caps = {
                # The following properties are set dynamically
                'platform': 'Linux',
                'browserName': 'firefox',
                'version': '29',
                'name': 'edwong',
                }

        self.driver = webdriver.Remote(
            desired_capabilities=des_caps,
            command_executor="http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
                % (user, key))
        self.driver.implicitly_wait(5)

    def test_basic_page(self):
        self.driver.get(OAUTH_RP)
        # assert '123 Done' in self.driver.title
        self.driver.find_element_by_css_selector(btn_signin_locator).click()
        # assert 'Firefox' in self.driver.title

        # username = self.driver.find_element_by_css_selector(input_email)
        # username.send_keys(fxa_user)
        # pw = self.driver.find_element_by_css_selector(input_password)
        # pw.send_keys(fxa_password)
        # self.driver.find_element_by_id(btn_submit).click()

        # btn_is_displayed = self.driver.find_element_by_css_selector(btn_signin_locator).is_displayed()

        # assert btn_is_displayed
        # assert '123 Done' in self.driver.title

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
