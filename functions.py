import random
import string
import sys
import time

import numpy as np
import scipy.interpolate as si
from colorama import Back, Fore, init
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

init(convert=True)


def random_user():
    name_l1=["Dave","Johny","Lisa","Jacky","mike","Janeth","Jade","Jude","Kenny","Myriam","Allegra","Detra","Angela","Cleo","Vella","Douglass","Kristen","Jeneva","Mercy","Berta","Leonard","Alida"]
    name_l2=["Lane","Kiana","Sara","wenny","john","Windy","Kimbra","Kisha","Donetta","Tawnya","Marya","Veronique","Brittney","Han","Scarlett","Eric","Jocker","Ervin"]
    name_1=random.choice(name_l1)
    name_2=random.choice(name_l2)
    year=str(random.randrange(1950,2000))
    date=str(random.randrange(1,30))
    randuser=name_1,name_2,year,date
    randuser="".join(randuser)
    return randuser

def random_pwd():
    l=string.ascii_letters+string.digits
    return str(random.randint(0,9))+"pwd@PROTON"+str(random.randint(0,9))

def new_tab(driver,url):
    driver.execute_script('''window.open("{}","_blank");'''.format(url))
    
def switch_frame(driver,xpath):
    WebDriverWait(driver,60).until(EC.frame_to_be_available_and_switch_to_it(
        (By.XPATH,xpath)))
    time.sleep(0.5)

def find_xpath(driver,xpath):
    temp=WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,xpath)))
    time.sleep(.5)
    return temp

def find_id(driver,id):
    temp=WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID,id)))
    time.sleep(.5)
    return temp
    
def input_value(driver,xpath,value):
    input_box=WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,xpath)))
    for i in value:
        input_box.send_keys(i)
        time.sleep(.1)
    time.sleep(1)

def calculate_move():
    points = [[6, 2], [3, 2],[0, 0], [0, 2]]
    points = np.array(points)
    x = points[:,0]
    y = points[:,1]
    t = range(len(points))
    ipl_t = np.linspace(0.0, len(points) - 1, 100)
    x_tup = si.splrep(t, x, k=1)
    y_tup = si.splrep(t, y, k=1)
    x_list = list(x_tup)
    xl = x.tolist()
    x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]
    y_list = list(y_tup)
    yl = y.tolist()
    y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]
    x_i = si.splev(ipl_t, x_list)
    y_i = si.splev(ipl_t, y_list)
    return x_i,y_i
def human_move(driver,xpath,x_i,y_i):
    startElement=find_xpath(driver,xpath)
    action=ActionChains(driver)
    action.move_to_element(startElement)
    action.perform()
    c = 5
    i = 0
    for mouse_x, mouse_y in zip(x_i, y_i):
        action.move_by_offset(mouse_x,mouse_y)
        action.perform()
        time.sleep(0.03)
        i+=1    
        if i==c:
            break
    startElement.click()
