## /e/StudentFiles/Quarter05/USD-T/Python/BookWork

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  
    def setUp(self):  
        self.browser = webdriver.Firefox()
    def tearDown(self):  
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):  
        ## First Connection from User
        self.browser.get('http://localhost:8000')

        ## User sees 'To-Do' mentioned in Title & Header
        self.assertIn('To-Do', self.browser.title)  
        self.fail('Finish the test!') 

        ## User invited to make a to-do item, adds "Buy peacock feathers"
        ## When enter is pressed, the page updates and displays the item as:
        #    # "1: Buy peacock feathers"
        ## There is still a text box to add more items. She adds a new item
        #    # "2: Use peacock feathers to make a fly"
        ## Page remembers previous to-do list

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 