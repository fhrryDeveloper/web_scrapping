from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', port=27017)
db=client.critical_products
product_data = db.critical_product

driver = webdriver.Firefox()
driver.get("https://www.rrpcanada.org/#/")
total_data = {}
total_product_data = []
try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table"))
    )
    titleElements = driver.find_elements_by_class_name("line-item-title")
    priceElements = driver.find_elements_by_class_name("line-item-bold")
    for i in range(len(titleElements)):
        product_name = titleElements[i].get_attribute('innerHTML')
        total_available = priceElements[i].get_attribute('innerHTML').lstrip()
        total_data['name'] = product_name
        total_data['available'] = total_available
        if product_data.find_one({"name": product_name, "available": total_available}) == None:
            total_data['_id'] = ObjectId()
            product_data.insert_one(total_data)
finally:
    driver.quit()