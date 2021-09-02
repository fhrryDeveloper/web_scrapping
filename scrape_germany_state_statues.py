from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Firefox()
driver.get("https://www.niche.com/colleges/harvard-university/majors")

majors = driver.find_elements_by_class_name('majors-list-item-major')
results = []
with open('majors.csv', 'w', newline='') as product:
    product_wirter = csv.writer(product, quoting=csv.QUOTE_ALL)
    for major in majors:
        print(major)
        print("/n")
        result = major.get_attribute('innerHTML')
        results.append(result)
        Major = result
        save_state = product_wirter.writerow([Major])
print(results)
if save_state :
    print("successfully saved!")
else :
    print("occur error while saving!")
