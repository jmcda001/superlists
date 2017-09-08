from selenium import webdriver
import unittest

from superlists.settings import chromedriverPath

class newVisitorTest(unittest.TestCase):
    # setUp and tearDown get run before EACH test
    def setUp(self):
        self.browser = webdriver.Chrome(chromedriverPath)

    def tearDown(self):
        self.browser.quit()


    # Any method whose name starts with test is a test method and will be run by the test runner.
    # You can have multiple test_ method per class, descriptive names are better
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test!')
        
        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box (Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists 
        # "1: Buy peackock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees that the site has generated a unique URL fo her -- there is some explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
