#brew install chromedriver
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time,sys,os

pw = [i.strip() for i in tuple(open('pass.word'))]


itemidurl = sys.argv[0]
maxbidebay = sys.argv[1]
if maxbidebay>70: sys.exit()
'''
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(executable_path=os.popen('which chromedriver').read().strip(),options=options)
'''

display = Display(visible=0, size=(1024, 768))
display.start()

driver = webdriver.Firefox()

driver.get(itemidurl)
time.sleep(3)
elements = driver.find_element_by_id("MaxBidId")
elements.send_keys(maxbidebay)
time.sleep(3)
elements = driver.find_element_by_css_selector('a[data-cta="placebid"]')


elements.click()



time.sleep(2)
driver.find_elements_by_id("userid")[0].send_keys(pw[0])
driver.find_elements_by_id("pass")[0].send_keys(pw[1])
button = driver.find_element_by_id("sgnBt")
button.click()
time.sleep(3)



times = driver.find_element_by_id("vi-cdown_timeLeft").text.split(' ')
print times
total = -5
for t in times:
    if 's' in t:
        total += int(filter(lambda x: x.isdigit(), t))

    elif 'm' in t:
        total += int(filter(lambda x: x.isdigit(), t))*60
 
    '''
    elif 'h' in t:
        total += int(filter(lambda x: x.isdigit(), t))*3600
    elif 'd' in t:
        total += int(filter(lambda x: x.isdigit(), t))*86400
    '''

time.sleep(1)

io = driver.find_element_by_class_name("button-placebid")#reviewBidSec_btn']")
time.sleep(total-10)
io.click()
time.sleep(20)

driver.quit()
