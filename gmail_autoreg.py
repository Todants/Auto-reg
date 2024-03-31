from time import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from random import randint
from fivesim import *
import zipfile


def password_generator(n=16):
    res = ''
    symbols = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ_'
    for i in range(n):
        res += symbols[randint(0, len(symbols) - 1)]
    return res


def get_chromedriver(use_proxy=False):
    chrome_options = uc.ChromeOptions()

    if use_proxy:
        with open('proxy.txt', 'r') as file:
            first_line = file.readline()
        PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS = first_line.split(':')

        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

        plugin_file = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(plugin_file, 'w') as zp:
            zp.writestr('manifest.json', manifest_json)
            zp.writestr('background.js', background_js)

        chrome_options.add_extension(plugin_file)
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')

    ua = UserAgent()
    user_agent = ua.random
    print(user_agent)
    chrome_options.add_argument(f"--user-agent={user_agent}")

    chrome_options.binary_location = "chrome-win\\chrome.exe"
    driver = uc.Chrome(options=chrome_options)

    return driver


def gmail_autoregistration():
    try:
        driver = get_chromedriver(use_proxy=False)

        driver.get("https://www.google.com/account/about/")
        # driver.get("https://2ip.ru")
        # driver.get("https://www.google.com")

        curr_url = driver.current_url

        enter = driver.find_elements(By.XPATH, '''//html//body//header//div[1]//div[5]//ul//li[1]''')
        enter[0].click()

        while curr_url == driver.current_url:
            sleep(1)
        sleep(1)
        curr_url = driver.current_url

        enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        2]//div//div//div//form//span//section//div//div//div//div[1]//div[1]//div//div[1]//div//div[1]//input''')
        enter[0].send_keys(password_generator(7))

        enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        2]//div//div//div//form//span//section//div//div//div//div[1]//div[2]//div//div[1]//div//div[1]//input''')
        enter[0].send_keys(password_generator(5))

        enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        3]//div//div//div//div//button''')
        enter[0].click()

        while curr_url == driver.current_url:
            sleep(1)
        sleep(1)
        curr_url = driver.current_url

        enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        2]//div//div//div//form//span//section//div//div//div[1]//div[1]//div//div//div[1]//div//div[1]//input''')
        enter[0].send_keys(f'{randint(1, 29)}')

        enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        2]//div//div//div//form//span//section//div//div//div[1]//div[3]//div//div//div[1]//div//div[1]//input''')
        enter[0].send_keys(f'{randint(1970, 2004)}')

        temp = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        2]//div//div//div//form//span//section//div//div//div[1]//div[2]//div//div//div[2]//select''')
        enter = Select(temp[0])
        enter.select_by_value(f"{randint(1, 12)}")

        temp = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        2]//div//div//div//form//span//section//div//div//div[2]//div[1]//div//div[2]//select''')
        enter = Select(temp[1])
        enter.select_by_value(f"{randint(1, 2)}")

        enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        3]//div//div//div//div//button''')
        enter[0].click()

        while curr_url == driver.current_url:
            sleep(1)
        sleep(2)
        curr_url = driver.current_url

        enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        2]//div//div//div//form//span//section//div//div//div[1]//div[1]//div//span//div[1]//div''')
        enter[0].click()

        enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[3]//div//div[
        1]//div//div//button''')
        enter[0].click()

        while curr_url == driver.current_url:
            sleep(1)
        sleep(1)
        curr_url = driver.current_url
        temp = password_generator()
        enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        2]//div//div//div//form//span//section//div//div//div//div[1]//div//div//div[1]//div//div[1]//div//div[
        1]//input''')
        enter[0].send_keys(temp)

        enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        2]//div//div//div//form//span//section//div//div//div//div[1]//div//div//div[2]//div//div[1]//div//div[
        1]//input''')
        enter[0].send_keys(temp)

        enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//c-wiz//div//div[
        3]//div//div//div//div//button''')
        enter[0].click()
        while curr_url == driver.current_url:
            sleep(1)
        sleep(1)
        curr_url = driver.current_url
        while True:
            while True:
                numb = get_number()
                order_phone = numb['phone']
                order_id = numb['id']

                enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//div//div//div[
                2]//div//div//div[1]//form//span//section//div//div//div[2]//div//div[2]//div[1]//label//input''')
                enter[0].clear()
                enter[0].send_keys(order_phone)

                enter = driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//div//div//div[3]//div//div[
                1]//div//div//button''')
                enter[0].click()

                if driver.find_elements(By.XPATH, '''//html//body//div[1]//div[1]//div[2]//div//div//div[
                2]//div//div//div[1]//form//span//section//div//div//div[2]//div//div[2]//div[2]//div'''):
                    ban_order(id=str(order_id))
                    continue
                else:
                    break

            t = time()
            while time() - t <= 120 and check_order(id=str(order_id))['sms'] == []:
                sleep(10)
            if check_order(id=str(order_id))['sms']:
                print(check_order(id=str(order_id))['sms'])
                break

        sleep(100000)
    except Exception as ex:
        print(ex)
        sleep(10000)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    gmail_autoregistration()
