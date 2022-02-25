from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException


import os
import datetime
from webdriver_manager.chrome import ChromeDriverManager



        

driver = webdriver.Chrome()
delay = 10
 
driver.get('https://www.instagram.com ')


############################
myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, "username")))
myElem.send_keys("your username here")
password = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("your password here")
print ("First Page is Ok ! ")
############################

time.sleep(2)

#username=driver.find_element_by_name("username")
#password=driver.find_element_by_name("password")




 
############################
button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div")))
#button_element = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")


#button_element = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button")
button_element.click()
############################



#time.sleep(5)

button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/div/div/section/div/button")))
#button_element = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/section/div/button")
button_element.click() 

#time.sleep(5)





############################
button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")))
#button_element = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
button_element.click()

############################


# Burası ana menü

#time.sleep(5)
print ( " This is your main instagram page !!! " )  
button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/section/div[3]/div[1]/div/div[1]/a")))
#button_element = driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[3]/div[1]/div/div[1]/a")

button_element.click()

#time.sleep(5)
#Burası Hesabım
#Burada takipçilerime basıcak






print(driver.current_url)
   
   

    
print ( " This is your main instagram page !!! " )       
    
    
    
count=10
#################################################################################################################################################################################
def is_my_friend_okey(x,y):
    #print(x)
    #print(y)
    if(x<2000  and  y<2000):
        print("BU kişi uygun")
        return True
    else:
        print("Bu kişi uygun değil")
        return False
           
################################################################################################################################################################################# 
def add_friends(count):
    
    for i in range(2,count):
        print("KONTROL",i)
    
        #arkadaşın arkadaşlarına bakıyor    
        button_element = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]")
        button_element.click()
    
    
        scr2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        sleep(5)
        text1 = scr2.text
        
        #print(text1)
        
        
        scr1 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[%s]' % i)
        print("BAŞLANGIÇ 2")
        #aaaa = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[1]/div/div[2]/button')
       
        #aaaa.click()
                                           
        driver.execute_script("arguments[0].scrollIntoView();", scr1)
        sleep(5)
       
        text = scr1.text
       
        list = text.encode('utf-8').split()
        person=list[0]
        person=person.decode("utf-8")
        print(person)   
        ############################################
        driver.get("https://www.instagram.com/{f}".format(f=person))
        body = driver.find_element_by_tag_name("body")
   
        body.send_keys(Keys.CONTROL + 't')
        
        followers_numberr = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]').text
        followers_numberr=followers_numberr.replace('takipçi','')
        following_numberr= driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]').text
        following_numberr=following_numberr.replace('takip','')
        
 
         
        list = followers_numberr.encode('utf-8').split()
        person=list[0]
        person=person.decode("utf-8")
        person=person.replace('.', '')
        followers_numberr=int(person)
         
        list = following_numberr.encode('utf-8').split()
        person=list[0]
        person=person.decode("utf-8")
        person=person.replace('.', '')
        following_numberr=int(person)
           
        sleep(5)
    
        print(followers_numberr , " Takipçi ")
        print(following_numberr , " Takip Ettiği ")
        
        
        
        kont=is_my_friend_okey(followers_numberr, following_numberr)
        
        if(kont):
            print("Bu kişiyi arkadaş olarak eklerim")
            
            
            #check_button = driver.find_element_by_link_text('Takip Et')
            
            
            try:



                ############### FOTO KONTROL ##########################

                # if fotodaki kız ise 
                #
                #aşağıdaki kodları çalıştır değil ise çalıştırma
                #
                #


                
                check_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/span/span[1]/button')
                
                print("kontrol 1")
                check_button.click()
            except:
                
                print("kontrol 2")
                print("Bu kişi hesabı kapalı")
                try:

                    
                    ############### FOTO KONTROL ##########################

                    # if fotodaki kız ise 
                    #
                    #aşağıdaki kodları çalıştır değil ise çalıştırma
                    #
                    #


                    
                    check_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/button')
                    check_button.click()
                except:
                    print("Bu kişi bende zaten ekli")
                
                

             
            
          
            
            
            
             
    
      
       ###############################################################OPEN 
        
    
         
       
        #look_my_friend_fol_lof(person)
       
       
       
       
        sleep(5)
       
        driver.execute_script("window.history.go(-1)")
       #############################################################CLOSE
       
################################################################################################################################################################################# 
def look_my_friend_fol_lof(person): 

   username=person     
   driver.get("https://www.instagram.com/{f}".format(f=person))
    
   body = driver.find_element_by_tag_name("body")
   
   body.send_keys(Keys.CONTROL + 't')
   
   
   followers_number = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
   following_number= driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text
    
   list = followers_number.encode('utf-8').split()
   person=list[0]
   person=person.decode("utf-8")
    
    
   person=person.replace('.', '')
    
   followers_number=int(person)
   
   list = following_number.encode('utf-8').split()
   person=list[0]
   person=person.decode("utf-8")
   person=person.replace('.', '')

   
   following_number=int(person)
       
   sleep(5)

   print(followers_number , " Takipçi ")
   print(following_number , " Takip Ettiği ")
    
    
   ####################  CHECK MY FRİENDS FOLLOWERS AND FOLLOWİNG NUMBERS İS OKEY #######################################
   
   kontrol=is_my_friend_okey(followers_number,following_number)
   
   if(kontrol):
       
       count1=followers_number
       print("Şimdi",username,"'nın takipçileri yazdırılacak")       
       add_friends(count1)
       

       count2=following_number
       print("Şimdi ",username,"'nın takip ettikleri yazdırılacak")
       add_friends(count2)
   
   
   
   
   
###################################################################################################################################################################################################################################################################################################### 
   
    


   
#password = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, "password")))
for i in range(1,count):
    
   print("Burada liste açılacak")

   button_element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]")))
   #button_element = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]")
    
   button_element.click()


   scr2 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
   #scr2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
   sleep(5)
   text1 = scr2.text
    
   #print(text1)
    

   scr1 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/ul/div/li[%s]' % i)))
   #scr1 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[%s]' % i)
   print("BAŞLANGIÇ")
   #aaaa = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[1]/div/div[2]/button')
   
   #aaaa.click()
                                       
   driver.execute_script("arguments[0].scrollIntoView();", scr1)
   sleep(5)
   
   text = scr1.text
   
   list = text.encode('utf-8').split()
   person=list[0]
   person=person.decode("utf-8")
   print(person)
   
   
  
###############################################################OPEN 
    

   sleep(5)
   
   look_my_friend_fol_lof(person)
   
   
   
   
   sleep(5)
   
   driver.execute_script("window.history.go(-1)")
#############################################################CLOSE
   
 



