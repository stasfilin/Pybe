__author__ = 'Stas Filin'
#Github: https://github.com/stasfilin/Pybe
#LinkedIN: https://www.linkedin.com/in/stasfilin
from selenium import webdriver
import time

class Youtube(object):
    def __init__(self, email, password, proxy=None):
        self.email = email
        self.password = password
        self.proxy = proxy
        self.xpaths = \
            {
                'usernameTxtBox' : "//input[@name='Email']",
                'passwordTxtBox' : "//input[@name='Passwd']",
                'submitButton' :   "//input[@name='signIn']"
            }
        self.css = \
            {
                'likeVideo' : "#watch-like > span.yt-uix-button-icon-wrapper",
                'dislikeVideo' : "#watch-dislike > span.yt-uix-button-icon-wrapper"
            }



        if self.proxy:
            service_args = \
                [
                '--proxy='+self.proxy,
                ]
            self.browser = webdriver.PhantomJS("Pybe/webdrivers/phantomjs.exe", service_args=service_args)
        else:
            self.browser = webdriver.PhantomJS("Pybe/webdrivers/phantomjs.exe")
            
    def login(self):
        try:
            self.browser.get("https://accounts.google.com/login")
            self.browser.set_page_load_timeout(60)
            self.browser.find_element_by_xpath(self.xpaths['usernameTxtBox']).clear()
            self.browser.find_element_by_xpath(self.xpaths['usernameTxtBox']).send_keys(self.email)
            self.browser.find_element_by_xpath(self.xpaths['passwordTxtBox']).clear()
            self.browser.find_element_by_xpath(self.xpaths['passwordTxtBox']).send_keys(self.password)
            self.browser.find_element_by_xpath(self.xpaths['submitButton']).click()
            return True
        except:
            return False

    def like(self, link):
        try:
            self.browser.get(link)
            self.browser.set_page_load_timeout(60)
            time.sleep(5)
            self.browser.find_element_by_css_selector(self.css['likeVideo']).click()
            return True
        except:
            return False
    def dislike(self, link):
        try:
            self.browser.get(link)
            self.browser.set_page_load_timeout(60)
            time.sleep(5)
            self.browser.find_element_by_css_selector(self.css['dislikeVideo']).click()
            return True
        except:
            return False

    def stop(self):
        try:
            self.browser.quit()
            return True
        except:
            return False