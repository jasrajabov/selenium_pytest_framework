from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    
    def close_browser(self):
        self.browser.close()

    
    
