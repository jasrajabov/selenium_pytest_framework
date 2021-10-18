from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class Utils:
            
    def __init__(self, browser, config):
        self.browser = browser
        self.timeout = int(config['timeout']['wait'])
        self.homepage_url = config['urls']['home_page']
        self.admin = config['credentials']['test']
        self.password = config['credentials']['password']


    def open(self, url):
        self.browser.get(url)
    
    def open_home_page(self):
        self.browser.get(self.homepage_url)
    
    def find_by_xpath(self, xpath):
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
    
    def find_by_xpath_m(self, xpath):
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def find_by_css(self, css):
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
    
    def find_by_css_m(self, css):
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css)))

    def find_by_name(self, name):
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((By.NAME, name)))
    
    def login_as_test(self):
        self.open_home_page()
        login = self.find_by_xpath("//div/div/a")
        login.click()
        self.find_by_name('username').send_keys(self.admin)
        self.find_by_name('password').send_keys(self.password)
        login_button = self.find_by_css("button[type='submit']")
        login_button.click()
        self.browser.implicitly_wait(5)
    
    def generate_fix_based_on_data(self, data):
        stock_, quantity_, price_, side_, order_type_ = [v for k, v in data.items()]
        stock = self.find_by_css('#stock_symbol')
        stock.send_keys(stock_)
        quantity = self.find_by_css('#quantity')
        quantity.send_keys(quantity_)
        price = self.find_by_css('#price')
        price.send_keys(price_)
        side= self.find_by_css('#side')
        side.click()
        self.find_by_css(f"option[value='{side_}']").click()
        order_type = self.find_by_css('#order_type')
        order_type.click()
        self.find_by_css(f"option[value='{order_type_}']").click()
        generate = self.find_by_css("button[type='submit']")
        generate.click()


    def go_to_fix_generate_page(self):
        fix_gen_link = self.find_by_css('a[class="nav-link"][href="/fixinput/"]')
        fix_gen_link.click()

    @property  
    def alert(self):
        alert = Alert(self.browser)
        return alert

    def close_browser(self):
        self.browser.close()

    def fix_to_dict(self, fix):
        splitted_by_del = fix.split('|')
        pairs = list(map(lambda x: x.split('='), splitted_by_del))
        d = {lst[0]: lst[1] for lst in pairs}
        return d
    
