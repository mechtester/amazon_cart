from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time

"fire fox driver"
# driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
"chrome driver"
driver=webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

url="https://www.amazon.in/"

driver.get(url)
driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath("//a[@id='nav-link-accountList']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='ap_email']").send_keys("7092030460")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='continue']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='ap_password']").send_keys("9525@amazon")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='signInSubmit']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").click()
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("i phone")
driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()

windows_before=driver.window_handles[0]


"scrolling for specific location"
driver.execute_script("window.scrollBy(1000,1400)","")
time.sleep(3)
driver.find_element_by_xpath("//div[@class='s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16']//span[@class='a-size-medium a-color-base a-text-normal'][normalize-space()='New Apple iPhone 11 (64GB) - Black']").click()
time.sleep(3)


windows_after=driver.window_handles[1]

driver.switch_to.window(windows_before)
time.sleep(3)

driver.switch_to.window(windows_after)

driver.implicitly_wait(5)
wait = ui.WebDriverWait(driver, 10)
wait.until(lambda driver: driver.find_element_by_id('add-to-cart-button'))
pwd = driver.find_element_by_id('add-to-cart-button')
pwd.click()