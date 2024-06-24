from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urlparse, urlunparse
import time
import logging
# import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import mysql.connector
import requests
logging.basicConfig(level=logging.WARNING)
url = 'https://www.mynewmarkets.com/markets'
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)  
driver.get(url)
# time.sleep(3)
# WebDriverWait.until()
# CommonSearches1 = driver.find_elements(By.CSS_SELECTOR,".slick-slide.slick-active")
# CommonSearches2 = driver.find_elements(By.CSS_SELECTOR,".slick-slide.slick-cloned")
# CommonSearches3 = driver.find_elements(By.CSS_SELECTOR,".slick-slide")
# CommonSearches4 = driver.find_elements(By.CSS_SELECTOR,".slick-slide.slick-current.slick-active")
# CommonSearches = CommonSearches1+CommonSearches2+CommonSearches3+CommonSearches4
# print(len(CommonSearches))
# driver.quit()
# /html/body/div[1]/main/section[1]/div/div[1]/div/div/div[10]/div/div/a
# /html/body/div[1]/main/section[1]/div/div[1]/div/div/div[10]/div/div/a
def DatabaseStorage(db_config,data):
    # cnx = mysql.connector.connect(**db_config)
    # cursor = cnx.cursor()

    for item in data:
        Company_Name = item['Company_Name']
        Company_URL = item['Company_URL']
        Description = item['Description']
        HQAddress = item['HQAddress']
        HQNumber = item['HQNumber']
        OtherLocations = item['OtherLocations']
        try:
            cnx = mysql.connector.connect(**db_config)
            cursor = cnx.cursor()
            query = "SELECT * FROM companies_list WHERE Company_Name = %s;"
            cursor.execute(query,(Company_Name,))
            result = cursor.fetchone()
            if result is None:
                print("Not in Database...Adding It...")
                sql = "INSERT INTO companies_list (Company_Name, Company_URL, Description, HQAddress, HQPhoneNumber, OtherLocations) VALUES (%s, %s, %s, %s, %s, %s)"

                cursor.execute(sql, (Company_Name, Company_URL,Description, HQAddress, HQNumber, OtherLocations))
                cnx.commit()
            cursor.close()
            cnx.close()
        except:
            print(f"Failed to write {Company_Name} data")


        # Commit the changes and close the connection
    # cnx.commit()
    # cursor.close()
    # cnx.close()

def collectTheCompaniesData(companiesList):
    db_config = {
    'user': 'riskbeanAdmin',
    'password': 'RB55P@$$word',
    'host': 'riskbean-mysql-db.mysql.database.azure.com',
    'database': 'riskbean_db',
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': './DigiCertGlobalRootG2.crt.pem'
    }
    # data= []
    for company in companiesList:
        data= []
        print(f"\ncollecting data from {company}\n")
        driverY = webdriver.Chrome(options=chrome_options)
        driverY.get(company)
        # driverY.get("https://www.mynewmarkets.com/companies/amwins") #tessting
        # /html/body/div[1]/main/div[2]/div[2]/div[1]/div/div[2]/h1
        # /html/body/div[1]/main/div[2]/div[2]/div[1]/div[2]/div[2]/h1
        # /html/body/div[1]/main/div[2]/div[2]/div[1]/div[2]/div[2]/h1
        try:
            try:
                Title = WebDriverWait(driverY,10).until(EC.presence_of_element_located((By.XPATH,"./html/body/div[1]/main/div[2]/div[2]/div[1]/div[2]/div[2]/h1")))
                # print(Title.text)
                Title = Title.text
                CompanyURL = WebDriverWait(driverY,10).until(EC.presence_of_element_located((By.XPATH,"./html/body/div[1]/main/div[2]/div[2]/div[1]/div[2]/div[2]/p")))
                # print(CompanyURL.text)
                CompanyURL = CompanyURL.text
            except:
                try:
                    Title = WebDriverWait(driverY,10).until(EC.presence_of_element_located((By.XPATH,"./html/body/div[1]/main/div[2]/div[2]/div[1]/div/div[2]/h1")))
                    # print(Title.text)
                    Title = Title.text
                    CompanyURL = WebDriverWait(driverY,10).until(EC.presence_of_element_located((By.XPATH,"./html/body/div[1]/main/div[2]/div[2]/div[1]/div/div[2]/p")))
                    # print(CompanyURL.text)
                    CompanyURL = CompanyURL.text
                except:
                    Title = " "
                    CompanyURL = " "
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[1]/section[1]/div
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[1]/section[1]/div/p
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[1]/section[1]/div
            # /html/body/div[1]/main/div[2]/div[2]/div[1]/div/div[2]/p
            # /html/body/div[1]/main/div[2]/div[2]/div[1]/div[2]/div[2]/p
            try:
                Description = WebDriverWait(driverY,10).until(EC.presence_of_element_located((By.XPATH,"./html/body/div[1]/main/div[2]/div[2]/div[2]/div[1]/section[1]/div")))
                # print(Description.text)
                Description = Description.text
            except:
                Description = ""
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[2]/a
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[2]/a
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[2]/a
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[2]/a
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[1]
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[1]
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[1]
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[1]
            try:
                HQAddress = WebDriverWait(driverY,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[1]")))
                if "HEADQUARTERS" in HQAddress.text:
                    HQAddress = HQAddress.text.strip()
                    HQAddress = ' '.join([line.strip() for line in HQAddress.split('\n') if line.strip() and 'Company Headquarters' not in line])
                    # print(HQAddress)
            except:
                HQAddress = " "
                # print(HQAddress)
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[2]/a
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[2]/a
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div/a
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div/a
            # /html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div/a
            try:
                try:
                    showPhoneNumber = WebDriverWait(driverY,10).until(EC.presence_of_element_located((By.XPATH,"./html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div[2]/a")))
                    if showPhoneNumber is not None:
                        showPhoneNumber.click()
                        time.sleep(1)
                        phoneNumber = WebDriverWait(driverY,10).until(EC.presence_of_element_located((By.XPATH,".//*[@id='organziationPhoneReveal']")))
                        phoneNumber = phoneNumber.text.strip()
                        phoneNumber= [line.strip() for line in phoneNumber.split('\n') if line.strip()]
                        phoneNumber =list(zip(phoneNumber[::2], phoneNumber[1::2]))
                        phoneNumber = ', '.join([f'{text}: {number}' for text, number in phoneNumber])
                        # print(phoneNumber)
                except:
                    showPhoneNumber = WebDriverWait(driverY,10).until(EC.presence_of_element_located((By.XPATH,"./html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/div/a")))
                    if showPhoneNumber is not None:
                        showPhoneNumber.click()
                        time.sleep(1)
                        phoneNumber = WebDriverWait(driverY,10).until(EC.presence_of_element_located((By.XPATH,".//*[@id='organziationPhoneReveal']")))
                        phoneNumber = phoneNumber.text.strip()
                        phoneNumber= [line.strip() for line in phoneNumber.split('\n') if line.strip()]
                        phoneNumber =list(zip(phoneNumber[::2], phoneNumber[1::2]))
                        phoneNumber = ', '.join([f'{text}: {number}' for text, number in phoneNumber])
                        # print(phoneNumber)
            except:
                phoneNumber = " "
            try:
                ShowOfficeLocations = WebDriverWait(driverY,10).until(EC.presence_of_element_located((By.XPATH,"./html/body/div[1]/main/div[2]/div[2]/div[2]/div[2]/section/div[2]/p[1]/button")))
                if ShowOfficeLocations is not None:
                    ShowOfficeLocations.click()
                    time.sleep(2)
                    numberOflocations = WebDriverWait(driverY,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"organization-office")))
                    time.sleep(5)
                    i =1
                    locationsList = []
                    # //*[@id="organizationOfficesModal"]/div/div/div[2]/div[1]/div
                    # "//*[@id='organizationOfficesModal']/div/div/div[2]/div[2]/div"
                    # //*[@id="organizationOfficesModal"]/div/div/div[2]/div[2]/div/div[1]
                    # //*[@id="organizationOfficesModal"]/div/div/div[2]/div[4]/div/div[1]
                    # //*[@id="organizationOfficesModal"]/div/div/div[2]/div[1]/div/div[2]/a
                    # //*[@id="organizationOfficesModal"]/div/div/div[2]/div[3]/div/div[2]/a
                    # //*[@id="officePhoneReveal13887"]/div
                    for location in numberOflocations:
                        SecLoc = location.find_element(By.XPATH,f"//*[@id='organizationOfficesModal']/div/div/div[2]/div[{i}]/div")
                        # time.sleep(10)
                        address = SecLoc.find_element(By.XPATH,f"//*[@id='organizationOfficesModal']/div/div/div[2]/div[{i}]/div/div[1]")
                        # time.sleep(10)
                        # print(address.text)
                        try:
                            showPhone = SecLoc.find_element(By.XPATH,f"//*[@id='organizationOfficesModal']/div/div/div[2]/div[{i}]/div/div[2]/a")
                            # time.sleep(10)
                            if showPhone is not None:
                                showPhone.click()
                                time.sleep(1)
                                Phone = SecLoc.find_element(By.CLASS_NAME,"ml-sm-3")
                                # time.sleep(10)
                                # print(Phone.text)
                        except:
                            Phone = " "
                        if f"{address.text} : {Phone.text}" not in locationsList:
                            locationsList.append(f"{address.text} : {Phone.text}")
                        i = i +1
                    if locationsList:
                        locationsList = ", ".join([location for location in locationsList])
                    # print(locationsList)
            except:
                ShowOfficeLocations = " "
                locationsList = " "
                    # locations = WebDriverWait(driverY,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#organizationOfficesModal > div > div > div.modal-body > div:nth-child(4) > div")))
            data.append({
                'Company_Name':Title,
                'Company_URL':CompanyURL,
                'HQAddress':HQAddress,
                'HQNumber':phoneNumber,
                'Description': Description,
                'OtherLocations':locationsList
            })
        except AttributeError as e:
            print(f"Error scrapping data for result {company}: {e}")
        driverY.quit()
        try:
            DatabaseStorage(db_config,data)
        except:
            print("Failed to write into the database")
        
        

def AccessCompaniesURL(pagesList):
    listOfCompanies = []
    for link in pagesList:
        print(f"\n Starting Link {link}")
        driverx = webdriver.Chrome(options=chrome_options)
        driverx.get(link)
        # driverx.get("https://www.mynewmarkets.com/search/rps+signature+programs") #testing
        links= WebDriverWait(driverx,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".no-expand")))
        for link in links:
            if link.get_attribute('href') is not None:
                if 'companies' in link.get_attribute('href'):
                    if link.get_attribute('href') not in listOfCompanies:
                        listOfCompanies.append(link.get_attribute('href'))
        driverx.quit()
    collectTheCompaniesData(listOfCompanies)


def checkEachURL(pagesnumber,url):
    urlres = urlparse(url)._replace(query='').geturl()
    UrlPagesList = []
    for num in range(1,pagesnumber):
        url = f'{urlres}?page={num}'
        UrlPagesList.append(url)
    AccessCompaniesURL(UrlPagesList)

constForSearch = 0

searchesList = []

commonSearches = driver.find_elements(By.CSS_SELECTOR,".card.card-action.card-appear")
# # driver.quit()

for link in commonSearches:
    if link.get_attribute('href') is not None:
        if "search" in link.get_attribute('href'):
            if link.get_attribute('href') not in searchesList:
                searchesList.append(link.get_attribute('href'))
print(searchesList)
for commonSearch in searchesList:
    # time.sleep(3)
    # if constForSearch == 1:
    #     driver = webdriver.Chrome()
    #     driver.get('https://www.mynewmarkets.com/markets')
    # SearchResutlsLink = WebDriverWait(commonSearch, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card.card-action.card-appear"))).get_attribute('href')
    # constForSearch = 1
    print(f'accessing {commonSearch}')
    url = urlparse(commonSearch)._replace(query='').geturl()
    driverOne = webdriver.Chrome(options=chrome_options)
    driverOne.get(url)
    try:
        numberOfPages = WebDriverWait(driverOne,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".page-link")))
        print(len(numberOfPages))
        listOfLinks= []
        for i in numberOfPages:
            if i.get_attribute('href') is not None:
                if 'page' in i.get_attribute('href'):
                    if i.get_attribute('href') not in listOfLinks:
                        listOfLinks.append(i.get_attribute('href'))
        try:
            print(listOfLinks)
            # listOfLinks = [link for link in listOfLinks if link is not None]
            data = [link[-2:]  for link in listOfLinks]
            data = [elem for elem in data if elem.isdigit()]
            data = int(max(data))
        except:
            data = [link[-1]  for link in listOfLinks]
            data = [elem for elem in data if elem.isdigit()]
            data = int(max(data))
        driverOne.quit()
        print(data)
        checkEachURL(data,url)
    except:
        print(f'Done with sites on {commonSearch}')
        driverOne.quit()

    # except:
    #     print("Element not found")