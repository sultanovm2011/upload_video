from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pyautogui
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(1)
wait = WebDriverWait(driver, 1000)
driver.get("https://www.spankwire.com/");
pyautogui.press('f11')

def click_wait(elem):
    i = 0
    while i<20:        
        try:
            elem.click() 
        except Exception:
            time.sleep(0.5)
        else: i += 21
        finally: i += 1 
            
def authorisation():
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Upload")))
    click_wait(driver.find_element(By.LINK_TEXT, "Upload"))
    wait.until(EC.element_to_be_clickable((By.NAME,"username"))).send_keys("granula2000")
    wait.until(EC.element_to_be_clickable((By.NAME,"password"))).send_keys("granula2000")
    wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/forgot']/preceding-sibling::button"))).click()
  
            
def fileUploading():
    i = 0
    while i<20:        
        try:
            driver.find_element(By.LINK_TEXT, "Upload").click()
        except Exception:
            time.sleep(0.5)
        else: i += 21
        finally: i += 1

    # Click to "Choose file to upload" button
    i = 0
    while i<20:        
        try:
            driver.find_element_by_xpath('//*[@id="js-react-upload-video-form"]//*[contains(text(),"Files from your computer")]/following-sibling::label').click()
        except Exception:
            time.sleep(0.5)
        else: i += 21
        finally: i += 1    
    time.sleep(1)
    
    # Path to file
    pyautogui.typewrite('/home/max/sk.mp4', interval=0.03)
    pyautogui.press('enter') 
    time.sleep(1)

    # FILE DESCRIPTION
    
    elems = driver.find_elements_by_xpath("//div[@class='css-1wy0on6']")    
    # Select "Product type" 
    click_wait(elems[0])
    # uncomment nothing to choose "Proffesional"    
#    pyautogui.press('down') #uncomment to choose "Homemade" 
    pyautogui.press('enter')     

    # Select "Orientation"
    click_wait(elems[1])
    # uncomment nothing to choose "Straight"
#    pyautogui.press('down') #uncomment to choose "Tranny" 
#    for i in range(2): pyautogui.press('down') #uncomment to choose "Gay"
    pyautogui.press('enter') 
    elems = driver.find_elements_by_xpath("//div[@class='css-1wy0on6']")

    # choose "Categories"
    click_wait(elems[2])
    pyautogui.typewrite('saggy', interval=0.05)
    time.sleep(3)
    pyautogui.press('enter') 

    # Type "title"
    wait.until(EC.element_to_be_clickable((By.NAME,"title"))).send_keys("masturbation")

    # choose "Pornstars"
    click_wait(elems[3])
    pyautogui.typewrite('a.j.', interval=0.05)
    time.sleep(4)
    pyautogui.press('enter') 
    
    # Type "description"
    i = 0
    while i<20:        
        try:
            driver.find_element(By.XPATH,'//*[@id="js-react-upload-video-form"]//*[@name="description"]').send_keys("orgazm")
        except Exception:
            time.sleep(0.5)
        else: i += 21
        finally: i += 1
 
    # Submit
    i = 0
    while i<20:        
        try:
            driver.find_element(By.XPATH, '//*[@id="js-react-upload-video-form"]//*[contains(text(),"Submit")]').click()
        except Exception:                                
            time.sleep(0.5)
        else: i += 21
        finally: i += 1    

# MAIN
authorisation()
fileUploading()
