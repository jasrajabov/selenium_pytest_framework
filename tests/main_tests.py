from datetime import datetime
from dateutil.relativedelta import *
import pytest


class TestFixapp:
    
    def test_login_text(self, fixapp):
        fixapp.open_home_page()
        text = fixapp.find_by_xpath("//div/div/p").text
        assert text == 'You are not logged in'

    def test_login_page(self, fixapp):
        fixapp.open_home_page()
        login = fixapp.find_by_xpath("//div/div/a")
        login.click()
        assert fixapp.browser.current_url == 'http://fixstockdataapp.herokuapp.com/accounts/login/'

    
    def test_login(self, fixapp):
        fixapp.login_as_test()
        title = fixapp.find_by_css('.display-5').text
        path = fixapp.find_by_xpath('//div/div/h3[2]')
        stock = path.text.split(':')[1][:-1].strip()
        assert stock == 'GOOGL'
        assert title == 'STOCK DATA'

    
    @pytest.mark.parametrize('stock', ['AAPL', 'FB'])
    def test_search_stock(self, stock, fixapp):
        fixapp.login_as_test()
        stock_box = fixapp.find_by_css('#stock_symbol')
        submit_button = fixapp.find_by_css('button[type="submit"][class*=btn]')
        stock_box.send_keys(stock)
        submit_button.click()
        _stock = fixapp.find_by_xpath_m('//div/div/h3[2]')[0].text.split(':')[1][:-1].strip()
        dates = list(map(lambda x: x.text, fixapp.find_by_css_m('.table-info tbody tr td:nth-child(6)')))
        assert _stock == stock


    
    def test_popup(self, fixapp, test_input_buy_limit):
        fixapp.login_as_test()
        fixapp.go_to_fix_generate_page()
        fixapp.generate_fix_based_on_data(test_input_buy_limit)
        assert fixapp.alert.text == "Do you want to generate FIX message?"

    @pytest.mark.draft
    def test_fix_message_generated_success(self, fixapp, test_input_buy_limit):
        fixapp.login_as_test()
        fixapp.go_to_fix_generate_page()
        fixapp.generate_fix_based_on_data(test_input_buy_limit)
        fixapp.alert.accept()
        message = fixapp.find_by_xpath('//body/div/div/div/b').text.strip()
        print(message)
        assert message.startswith('Success')


        


        