## /e/StudentFiles/Quarter05/USD-T/Python/BookWork
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User invited to make a to-do item immediately.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        ## The user adds "Buy peacock feathers" as their first item
        inputbox.send_keys('Buy peacock feathers')

        ## When enter is pressed, the page updates and displays the item as:
        #    # "1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER) 
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        ## There is still a text box to add more items. She adds a new item
        #    # "2: Use peacock feathers to make a fly"
        self.fail('Finish the test!')

        ## Page remembers previous to-do list

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 