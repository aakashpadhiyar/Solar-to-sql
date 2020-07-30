from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from selenium.webdriver.chrome.options import Options
import csv_to_sqlite 

BASE_DIR =  os.getcwd()

cleared = ('/html/body/app-root/app-inject-solar/div/div[2]/div[2]/div/app-errore-log/div/div/nav/div/a[2]')
uncleared = ('/html/body/app-root/app-inject-solar/div/div[2]/div[2]/div/app-errore-log/div/div/nav/div/a[1]')
download = ('/html/body/app-root/app-inject-solar/div/div[2]/div[2]/div/app-errore-log/div/div/div[2]/div/div/form/div/div[3]/button[3]')

print("""To run this Script [ python -i main.py ] and wait untill 'error-log' page load.\n\nTo add Un-Cleared data to sql use [ bot.uncleared() ] and for Cleared [ bot.cleared() ].\n\n To add csv to DataBase use[ bot.tosql() ] by {'https://github.com/aakashpadhiyar'} 
""")




class jnjectsolar:
    
    def __init__(self):

        chrome_options = webdriver.ChromeOptions()

        prefs = {'download.default_directory' : BASE_DIR}
        chrome_options.add_experimental_option('prefs', prefs)
                
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')

        self.driver = webdriver.Chrome(executable_path='./chromedriver')

        self.driver.get('http://www.injectsolar.com/portal/#/login')

        login_user = self.driver.find_element_by_id('login_id')
        login_pass = self.driver.find_element_by_id('password')
        login_button = self.driver.find_element_by_class_name('login-button')

        login_user.send_keys('triose')
        login_pass.send_keys('triose123')

        sleep(1)
        login_button.click()


    
    def login(self):
        sleep(3)
        self.driver.get('http://www.injectsolar.com/portal/#/inject-solar/errore-log')

    def uncleared(self):
        self.driver.find_element_by_xpath(uncleared).click()
        sleep(3)
        to_date = self.driver.find_element_by_xpath('/html/body/app-root/app-inject-solar/div/div[2]/div[2]/div/app-errore-log/div/div/div[2]/div/div/form/div/div[1]/div/mat-form-field/div/div[1]/div[1]/input')
        to_date.send_keys('1/1/2020')
        from_date = self.driver.find_element_by_xpath('/html/body/app-root/app-inject-solar/div/div[2]/div[2]/div/app-errore-log/div/div/div[2]/div/div/form/div/div[2]/div/mat-form-field/div/div[1]/div[1]/input')
        from_date.send_keys('2/29/2020')
        search = self.driver.find_element_by_xpath('/html/body/app-root/app-inject-solar/div/div[2]/div[2]/div/app-errore-log/div/div/div[2]/div/div/form/div/div[3]/button[1]')
        sleep(1)
        search.click()
        sleep(2)
        self.driver.find_element_by_xpath(download).click()
        sleep(1)
        tosql(self)
    
    def cleared(self):
        self.driver.find_element_by_xpath(cleared).click()
        sleep(3)
        to_date = self.driver.find_element_by_xpath('/html/body/app-root/app-inject-solar/div/div[2]/div[2]/div/app-errore-log/div/div/div[2]/div/div/form/div/div[1]/div/mat-form-field/div/div[1]/div[1]/input')
        to_date.send_keys('1/1/2020')#starting date
        from_date = self.driver.find_element_by_xpath('/html/body/app-root/app-inject-solar/div/div[2]/div[2]/div/app-errore-log/div/div/div[2]/div/div/form/div/div[2]/div/mat-form-field/div/div[1]/div[1]/input')
        from_date.send_keys('2/29/2020')#ending date
        search = self.driver.find_element_by_xpath('/html/body/app-root/app-inject-solar/div/div[2]/div[2]/div/app-errore-log/div/div/div[2]/div/div/form/div/div[3]/button[1]')
        sleep(1)
        search.click()
        sleep(2)
        self.driver.find_element_by_xpath(download).click()
        sleep(1)
        tosql(self)
    
    def tosql(self):
        options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250") 

        solar_data = ["Download_CSV.csv"]

        csv_to_sqlite.write_csv(solar_data, "SolarData.sqlite", options)

bot = jnjectsolar()
bot.login()