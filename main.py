from selenium import webdriver

chrome_drivr_path = "/Users/Kamiklza/PycharmProjects/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_drivr_path)
driver.get("https://www.amazon.com/Medify-Air-MA-15-Purifier-filter/dp/B089CBRBVX/ref=sr_1_2_sspa?dchild=1&keywords=dyson&qid=1629874067&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFKQkpFUFBTNlI0MVQmZW5jcnlwdGVkSWQ9QTAwODU4MTYzMVpSUDhTTDZFVzMwJmVuY3J5cHRlZEFkSWQ9QTA3MjI4NTMzTDhPV0E2MUtCMzUmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1")
price = driver.find_element_by_id("price_inside_buybox")
item_variation = driver.find_element_by_xpath('//*[@id="a-autoid-11-announce"]/div/div[1]/p')
print(item_variation.text)
driver.quit()

