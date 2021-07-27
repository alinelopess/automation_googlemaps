import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleMapsSearch(unittest.TestCase):

    def setUp(self):
        # declare and initialize driver variable
        self.driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")

    def test_search_dublin_in_google_maps(self):
        # to load a given URL in browser window
        driver = self.driver
        driver.get("http://www.google.com/maps")
        time.sleep(2)

        # to accept the cookies
        elem = driver.find_element_by_xpath("//*[@jsname='higCR']").click() 

        # to write dublin in search
        elem = driver.find_element_by_name("q")
        elem.send_keys("Dublin")

        # to click in search button
        elem = driver.find_element_by_id("searchbox-searchbutton").click()
        time.sleep(3)

        # to validate that 'Dublin' name as a headline text
        elem = driver.find_element_by_xpath("//*[@class='x3AX1-LfntMc-header-title-title gm2-headline-5']")

        # to click in directions icon
        elem = driver.find_element_by_xpath("//*[@class='DVeyrd gm2-hairline-border section-action-chip-button']").click()
        time.sleep(3)

        # to verify that dublin is in destination field
        elem = driver.find_element_by_xpath("//*[@aria-label='Destino Dublin, Irlanda']")
        elem.send_keys(Keys.RETURN)

        # to verify if the search results page contains any results or no results were found.
        assert "No results found." not in driver.page_source
        
    def tearDown(self):
        # to close the browser
        self.driver.close()

if __name__ == "__main__":
    unittest.main()