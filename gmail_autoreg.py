from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from random import randint


def set_options(options):
    """ua = UserAgent()
    user_agent = ua.random
    print(user_agent)"""
    options.add_argument(f"--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                         f"like Gecko) Chrome/121.0.0.0 Safari/537.36")
    options.binary_location = "chrome-win\\chrome.exe"
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    # options.add_argument(f'--load-extension={_path_del}')
    # options.add_argument(f'--load-extension={_path}')

    # options.add_extension(r'C:\Users\User\PycharmProjects\Epicparser\extien
    # \GJLDCDNGMDKNPINOEMNDLIDPCABKGGCO_9_5_1_0.crx')


opt = uc.ChromeOptions()
# opt = Options()
set_options(opt)
driver = uc.Chrome(options=opt)


def password_generator(n=16):
    res = ''
    symbols = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ_'
    for i in range(n):
        res += symbols[randint(0, len(symbols) - 1)]
    return res


def gmail_autoregistration():
    try:
        curr_url = driver.current_url

        driver.get("https://www.google.com/account/about/")
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
        sleep(1)
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

        sleep(100000)
    except Exception as ex:
        print(ex)
        sleep(10000)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    gmail_autoregistration()
