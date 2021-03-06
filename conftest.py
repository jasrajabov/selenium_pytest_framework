from .utils.utils import Utils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import configparser
from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture
def config(scope='session'):
    config = configparser.ConfigParser()
    config.read('test_config.ini')
    return config

@pytest.fixture
def browser(config):
    opts = Options()
    opts.headless = config['chrome_options'].getboolean('headless')
    driver = config['browser']['browser']
    if driver == 'chrome':
        exec_path = config['paths']['exc_path_chrome']
        # _browser = webdriver.Chrome(options=opts, executable_path=exec_path)
        _browser = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

    # Return the WebDriver instance for the setup
    yield _browser
    # Quit the WebDriver instance for the cleanup
    _browser.quit()


@pytest.fixture
def fixapp(browser, config):
    return Utils(browser, config)


@pytest.fixture
def test_input_buy_limit():
    return {'stock': 'AAPL', 'quantity': 123, 'price': 123, 'side': 'Buy', 'order_type': 'Limit'}

