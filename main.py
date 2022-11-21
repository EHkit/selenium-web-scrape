from selenium import webdriver

def get_html_code(url):
    DRIVER_PATH = 'driver/chrome'

    # Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
    driver.get(url)

    page_code = driver.page_source
    
    print(page_code)
