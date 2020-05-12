import time
from selenium import webdriver
from json import load


def send_whatsapp(phone, i, msg):
    print(i, end='')
    try:
        driver.get("https://web.whatsapp.com/send?phone=" + phone)
        driver.execute_script("window.onbeforeunload = function() {};")
        time.sleep(5)
        msg_box = driver.find_element_by_class_name('_1Plpp')
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        print(")sent message to ", phone)

        button.click()
    except Exception as e:
        print(")web address not valid or time taken to load is high.so not send to ", phone)


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
try:
    phone_numbers = load((open('phone_number.json')))
    message = "    " + input("Enter message to be send:")
    for i in range(len(phone_numbers)):
        send_whatsapp(phone_numbers[i], i , message)
except Exception as e:
    print("Error reading data from json file table", e)
finally:
    time.sleep(5)
    driver.close()
