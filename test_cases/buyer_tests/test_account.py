import unittest

from selenium import webdriver
from selenium.webdriver import ChromeOptions

from pages.buyer_pages.account import Account
from common.login_buyer import LoginBuyer


class KirvBuyerProfileTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def test_user_profile(self):
        # Account-section
        LoginBuyer().sign_in_existing_buyer(self)
        account = Account(self.driver)
        account.go_to_account()
        account.check_account_active()
        account.check_title_in_account()
        account.go_to_user_profile()
        account.check_user_profile_active()
        account.check_title_on_user_profile()
        account.check_fields()

if __name__ == "__main__":
    unittest.main()