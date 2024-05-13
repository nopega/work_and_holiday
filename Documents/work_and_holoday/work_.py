from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://161.82.213.251/opp/app/frm_yproject_project_member.php?act=&t=20240513104009")
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="content2"]/table/tbody/tr[3]/td/form/table/tbody/tr[1]/td[2]/input'))
)
driver.find_element(By.XPATH, '//*[@id="content2"]/table/tbody/tr[3]/td/form/table/tbody/tr[1]/td[2]/input').send_keys("pongkunak2@gmail.com")
driver.find_element(By.XPATH, '//*[@id="content2"]/table/tbody/tr[3]/td/form/table/tbody/tr[2]/td[2]/input').send_keys("35650")
driver.find_element(By.XPATH,'//*[@id="button"]').click()
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="chk_firm"]'))
)
driver.find_element(By.XPATH, '//*[@id="chk_firm"]').click()
driver.find_element(By.XPATH, '//*[@id="search_button"]').click()
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="race_code"]'))
)
input_1 = Select(driver.find_element(By.XPATH, '//*[@id="race_code"]'))
input_1.select_by_visible_text("ไทย")
input_2 = Select(driver.find_element(By.XPATH, '//*[@id="religion_code"]'))
input_2.select_by_visible_text("พุทธ")
driver.find_element(By.XPATH, '//*[@id="birth_date"]').send_keys("11062544")
driver.find_element(By.XPATH, '//*[@id="mobile_phone"]').send_keys("0869595012")
driver.find_element(By.XPATH, '//*[@id="institute_bhl_detail"]').send_keys("มหาวิทยาลัยมหิดล")
input_3 = Select(driver.find_element(By.XPATH, '//*[@id="bachelor_degree_detail"]'))
input_3.select_by_visible_text("ปริญญาตรี หรือเทียบเท่า")
input_3 = Select(driver.find_element(By.XPATH, '//*[@id="status_test"]'))
input_3.select_by_visible_text("ผลการทดสอบทักษะภาษาอังกฤษ ")
driver.find_element(By.XPATH,'//*[@id="agn_prefix_code_thai_003"]').click()
driver.find_element(By.XPATH, '//*[@id="agn_first_name"]').send_keys("ชัยสิทธิ์")
driver.find_element(By.XPATH, '//*[@id="agn_last_name"]').send_keys("ชัยจีระธิกุล")
input_3 = Select(driver.find_element(By.XPATH, '//*[@id="agn_relation_code"]'))
input_3.select_by_visible_text("บิดา")
driver.find_element(By.XPATH, '//*[@id="agn_mobile"]').send_keys("0815991185")
driver.find_element(By.XPATH, '//*[@id="agn_email"]').send_keys("chaisitchaichi@gmail.com")
driver.find_element(By.XPATH,'//*[@id="save_button"]').click()
