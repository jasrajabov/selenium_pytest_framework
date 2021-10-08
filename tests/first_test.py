from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pytest
from dateutil.relativedelta import *


# opts = Options()
# opts.headless = True

# def test_login_text():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('http://fixstockdataapp.herokuapp.com/')
#     text = driver.find_element_by_xpath("//div/div/p").text
#     assert text == 'You are not logged in'
#     driver.quit()


# def test_login_page():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('http://fixstockdataapp.herokuapp.com/')
#     login = driver.find_element_by_xpath("//div/div/a")
#     login.click()
#     assert driver.current_url == 'http://fixstockdataapp.herokuapp.com/accounts/login/'

#     text = driver.find_element_by_tag_name("h2").text
#     assert text == 'Log In'
#     driver.quit()

# def test_login():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('http://fixstockdataapp.herokuapp.com/')
#     login = driver.find_element_by_xpath("//div/div/a")
#     login.click()
#     driver.find_element_by_name('username').send_keys('admin')
#     driver.find_element_by_name('password').send_keys('1Dalg091!')
#     login_button = driver.find_element_by_css_selector("button[type='submit']")
#     login_button.click()
#     driver.implicitly_wait(5)
#     title = driver.find_element_by_css_selector('.display-5').text
#     stock = driver.find_element_by_xpath('//div/div/h3[2]').text.split(':')[1][:-1].strip()
#     assert stock == 'GOOGL'
#     assert title == 'STOCK DATA'
#     driver.quit()


# def test_search_stock():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('http://fixstockdataapp.herokuapp.com/')
#     login = driver.find_element_by_xpath("//div/div/a")
#     login.click()
#     driver.find_element_by_name('username').send_keys('admin')
#     driver.find_element_by_name('password').send_keys('1Dalg091!')
#     login_button = driver.find_element_by_css_selector("button[type='submit']")
#     login_button.click()
#     driver.implicitly_wait(5)
#     stock_box = driver.find_element_by_css_selector('#stock_symbol')
#     submit_button = driver.find_element_by_css_selector('button[type="submit"][class*=btn]')
#     stock_box.send_keys('AAPL')
#     submit_button.click()
#     stock = driver.find_element_by_xpath('//div/div/h3[2]').text.split(':')[1][:-1].strip()
#     dates = list(map(lambda x: x.text, driver.find_elements_by_css_selector('.table-info tbody tr td:nth-child(6)')))
#     print(dates)
#     assert stock == 'AAPL'
#     driver.quit()



# def test_dates():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('http://fixstockdataapp.herokuapp.com/')
#     login = driver.find_element_by_xpath("//div/div/a")
#     login.click()
#     driver.find_element_by_name('username').send_keys('admin')
#     driver.find_element_by_name('password').send_keys('1Dalg091!')
#     login_button = driver.find_element_by_css_selector("button[type='submit']")
#     login_button.click()
#     driver.implicitly_wait(5)
#     stock_box = driver.find_element_by_css_selector('#stock_symbol')
#     submit_button = driver.find_element_by_css_selector('button[type="submit"][class*=btn]')
#     stock_box.send_keys('AAPL')
#     submit_button.click()
#     dates = list(map(lambda x: x.text, driver.find_elements_by_css_selector('.table-info tbody tr td:nth-child(6)')))
#     now = datetime.now()
#     year = now.strftime("%Y")
#     month = now.strftime("%m")
#     first_month = f"{year}-{month}-01"
#     last = now - relativedelta(month=6)
    
#     last_el_year = last.strftime("%Y")
#     last_el_month = last.strftime("%m")
#     last_month = f"{last_el_year}-{last_el_month}-01"

#     assert first_month == dates[0]
#     assert last_month == dates[-1]
#     driver.quit()


# # @pytest.mark.draft
# def test_fix_generator_page():
#     driver = webdriver.Chrome(options=opts)
#     driver.get('http://fixstockdataapp.herokuapp.com/')
#     login = driver.find_element_by_xpath("//div/div/a")
#     login.click()
#     driver.find_element_by_name('username').send_keys('admin')
#     driver.find_element_by_name('password').send_keys('1Dalg091!')
#     login_button = driver.find_element_by_css_selector("button[type='submit']")
#     login_button.click()
#     driver.implicitly_wait(5)
#     fix_gen_button = driver.find_element_by_css_selector("a[class='nav-link'][href='/fixinput/']")
#     fix_gen_button.click()
#     display_text = driver.find_element_by_css_selector('h3[class="display-5"]').text
#     assert display_text == 'FIX MESSAGE GENERATOR'
#     driver.quit()


