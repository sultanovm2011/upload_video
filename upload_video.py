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


def authorisation():
    driver.find_element_by_partial_link_text("Upload").click()
    driver.find_element_by_name("username").send_keys("granula2000")
    driver.find_element_by_name("password").send_keys("granula2000")
    driver.find_element_by_xpath("//a[@href='/forgot']/preceding-sibling::button").click()
    
def fileUploading():
    time.sleep(3)
#    wait.until(driver.invisibility_of_element_located(By.link_text, "Upload")).click()
    driver.find_element_by_partial_link_text("Upload").click()
    # Click to "Choose file to upload" button
    driver.find_element_by_xpath('//*[@id="js-react-upload-video-form"]//*[contains(text(),"Files from your computer")]/following-sibling::label').click()
    # Path to file
    pyautogui.typewrite('/home/max/sk.mp4')
    pyautogui.press('enter') 
    
    # File description
    elems = driver.find_elements_by_xpath("//div[@class='css-1wy0on6']")
    # Select "Product type" 
    elems[0].click()
    # uncomment nothing to choose "Proffesional"    
#    pyautogui.press('down') #uncomment to choose "Homemade" 
    pyautogui.press('enter')     
    time.sleep(1)

    # Select "Orientation"
    elems[1].click()  
    # uncomment nothing to choose "Straight"
#    pyautogui.press('down') #uncomment to choose "Tranny" 
#    for i in range(2): pyautogui.press('down') #uncomment to choose "Gay"
    pyautogui.press('enter') 
    time.sleep(1)
    elems = driver.find_elements_by_xpath("//div[@class='css-1wy0on6']")
    time.sleep(1)

    # choose "Categories"
    elems[2].click() 
#    wait.until(EC.element_to_be_clickable((elems[1]))).click()
    pyautogui.typewrite('saggy')
    time.sleep(2)
    pyautogui.press('enter') 
    time.sleep(1)

    # Type "title"
    driver.find_element_by_name("title").send_keys("masturbation")
    time.sleep(1)
    
    # choose "Pornstars"
    elems[3].click() 
    pyautogui.typewrite('a.j.')
    time.sleep(3)
    pyautogui.press('enter') 
    time.sleep(1)
    
    # Type "description"
    driver.find_element_by_xpath("//textarea[@class='sc-dUjcNx sc-gHboQg sc-elNKlv dTqHfs']").send_keys("orgazm")
   
    # Submit
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='sc-fYiAbW sc-fOKMvo sc-hUMlYv kFEgXl']"))).click()

# main
authorisation()
fileUploading()
