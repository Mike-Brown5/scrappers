from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
from urllib.parse import urlparse
from time import time
class WebScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()  # Replace with your preferred browser

    def scrape_search_results(self):
        self.driver.get(self.url)
        search_results = self.driver.find_elements(By.CSS_SELECTOR, 'div.organization.organization-single')
        return search_results

class DataProcessor:
    def process_search_results(self, search_results):
        data = []
        for result in search_results:
            try:
                compName = result.find_element(By.CSS_SELECTOR, 'h1.organization-title.mb-0').text
                compURL = result.find_element(By.CSS_SELECTOR, 'p.organization-subtitle.text-muted.mt-n1.text-4').text
                description = result.find_element(By.CSS_SELECTOR, 'div.organization-body').text
                HQaddress = result.find_elements(By.CSS_SELECTOR, 'div.text-4.mb-4')
                HQaddress = [address.text for address in HQaddress]
                # ...
                data.append({
                    'compName': compName,
                    'compURL': compURL,
                    'HQaddress': HQaddress,
                    'Description': description,
                    # ...
                })
            except Exception as e:
                print(f"Error scraping data for result {compURL}: {e}")
        return data

class DatabaseStorage:
    def __init__(self, db_config):
        self.db_config = db_config

    def store_data(self, data):
        cnx = mysql.connector.connect(**self.db_config)
        cursor = cnx.cursor()

        # Insert the data into the table
        for item in data:
            compName = item['compName']
            compURL = item['compURL']
            HQaddress = item['HQaddress']
            description = item['Description']
            # ...

            # query = "SELECT * FROM listings_in WHERE compName = %s and compURL=%s and HQaddress = %s and Description = %s and ...;"
            # cursor.execute(query, (compName, compURL, HQaddress, description, ...))
            # result = cursor.fetchone()
            # if result is None:
            #     print("data not found so I'm adding it")
            #     sql = "INSERT INTO listings_in (compName, compURL, HQaddress, Description, ...) VALUES (%s, %s, %s, %s, ...)"
            #     cursor.execute(sql, (compName, compURL, HQaddress, description, ...))

        # Commit the changes and close the connection
        cnx.commit()
        cursor.close()
        cnx.close()

def scrap_listing_links(url):
    driver = webdriver.Chrome()  
    driver.get(url)
    time.sleep(1)
    search_results = driver.find_elements(By.CSS_SELECTOR, 'div.px-1.py-2')
    links = [result.text for result in search_results]
    print(links)
    return search_results

def scrap_listing_linksOne(url):
    driver = webdriver.Chrome() 
    driver.get(url)
    search_results = driver.find_elements(By.CSS_SELECTOR, 'div.results.results-listings.mt-5.mt-lg-0')
    return search_results

def scrap_listing_pageByPage(url):
    driver = webdriver.Chrome()  
    driver.get(url)
    pages = driver.find_elements(By.CSS_SELECTOR, 'div.col-lg.order-1.order-lg-2')
    return pages

def process_listing_links(search_results):
    data = []
    for result in search_results:
        try:
            links = result.find_element(By.CLASS_NAME, "//a[@class='card card-action card-appear']")
            data.append({
                'Links': links,
            })
        except Exception as e:
            print(f"Error scraping data for result {links}: {e}")
    return data

def process_listing_linksOne(search_results):
    data = []
    for result in search_results:
        try:
            links = result.find_elements(By.CSS_SELECTOR, 'a.no-expand')
            data = [link['href'] for link in links]
            data = list(set([link for link in data if '/companies/' in link]))
        except Exception as e:
            print(f"Error scraping data for result {links}: {e}")
    return data

def process_listing_pageByPage(search_results):
    data = []
    for result in search_results:
        try:
            links = result.find_elements(By.CSS_SELECTOR, 'a.page-link')
            data = [link['href'][-2:] for link in links]
            data = [elem for elem in data if elem.isdigit()]
            data = int(max(data))
            return data
        except Exception as e:
            print(f"Error scraping data for result {links}: {e}")
    return data

if __name__ =='__main__':
    url = 'https://www.mynewmarkets.com/markets'
    search_results = scrap_listing_links(url)
    if search_results:
        dataL = process_listing_links(search_results)
        i = 0
        try:
            for i in range(len(dataL)):
                urlres = dataL[i]['Links']  # this is the link for the lsiting search results
                search_results = scrap_listing_pageByPage(urlres)
                dataN = process_listing_pageByPage(search_results)
                k = 1
                print(f'accessing link {url}')
                for k in range(1, dataN):
                    if k > 1:
                        url = urlparse(urlres)._replace(query='').geturl()
                    url = f'{urlres}?page={k}'
                    search_results = scrap_listing_linksOne(url)  # main div that contains the listing cards
                    if search_results:
                        dataG = process_listing_linksOne(search_results)  # list of 'view listing links' each one by it self
                        j = 0
                        print(f'accessing link {url}')
                        for j in range(len(dataG)):
                            url = dataG[j]  # this is the link for each listing by it self
                            scraper = WebScraper(url)
                            db_config = {
                                'user': 'root',
                                'password': '',
                                'host': 'localhost',
                                'database': 'Sky_ScraperDB'
                            }
                            search_results = scraper.scrape_search_results()
                            if search_results:
                                processor = DataProcessor()
                                data = processor.process_search_results(search_results)
                                storage = DatabaseStorage(db_config)
                                storage.store_data(data)
                            j += 1
                    k += 1
                print(f'done for {url}')
                i += 1
        except IndexError:
            print("No more links to scrap")