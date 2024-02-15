try:
    import selenium
except:
    import os
    os.system("pip3 install selenium")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
#options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.get("https://www.kali.org/tools/all-tools/")

elems = driver.find_elements(By.XPATH,"//a[@href]")
Toolsurl=[]

for elem in elems:
    if(elem.get_attribute("href").startswith("https://www.kali.org/tools")):
        Toolsurl+= [elem.get_attribute("href")]
Skip=[]
for i in Toolsurl:
    driver.get(i)
    j=driver.find_elements(By.TAG_NAME,"code")
    for i in j:
        if i.text.startswith("sudo apt install"):
            if(Skip.count(i.text)):
                continue
            else:
                print(i.text)
                Skip+=[i.text]
            #print(Skip)

elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()