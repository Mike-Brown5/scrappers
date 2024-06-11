import requests
from bs4 import BeautifulSoup
import mysql.connector
from urllib.parse import urlparse
class WebScraper:
    def __init__(self, url):
        self.url = url

    def scrape_search_results(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve data from {self.url}: {e}")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        search_results = soup.find_all('div', class_='organization organization-single')
        # print(f"Found {len(search_results)} search results.")
        return search_results

class DataProcessor:
    def process_search_results(self, search_results):
        data = []
        for result in search_results:
            try:
                compName = result.find('h1', class_='organization-title mb-0').text.strip()
                # print(compName)
                compURL = result.find('p', class_='organization-subtitle text-muted mt-n1 text-4').text.strip()
                # print(compURL)
                description = result.find('div', class_='organization-body').text.strip()
                print(description)
                HQaddress = result.find_all('div', class_='text-4 mb-4')
                HQaddress = [address.text.strip() for address in HQaddress]
                # lines = HQaddress.split('\n')
                # HQaddress = [line.strip() for line in lines if line.strip() and 'Company Headquarters' not in line]
                const = 0
                if 'Headquarters' in HQaddress[0]:
                    HQaddress = ' '.join([line.strip() for line in HQaddress[0].split('\n') if line.strip() and 'Company Headquarters' not in line])
                    const = 1
                try:
                    if 'Headquarters' in HQaddress[1] and const ==0:
                        HQaddress = ' '.join([line.strip() for line in HQaddress[1].split('\n') if line.strip() and 'Company Headquarters' not in line])
                    elif 'Headquarters' in HQaddress[2] and const == 0:
                        HQaddress = ' '.join([line.strip() for line in HQaddress[2].split('\n') if line.strip() and 'Company Headquarters' not in line])
                except:
                    HQaddress = ''
                print(HQaddress)
                OfficeLocations = result.find_all('div', class_='col-sm-5 mr-auto')
                OfficeLocations = [location.text.strip() for location in OfficeLocations]
                OfficeLocations = ', '.join(OfficeLocations)
                print(OfficeLocations)
                ContactNums = result.find('div', class_='click-reveal-target').text.strip()
                # ContactNums = [num.text.strip() for num in ContactNums]
                ContactNums= [line.strip() for line in ContactNums.split('\n') if line.strip()]
                ContactNums =list(zip(ContactNums[::2], ContactNums[1::2]))
                ContactNums = ', '.join([f'{text}: {number}' for text, number in ContactNums])
                print(ContactNums)
                memberships = result.find_all('p', class_='text-4 mb-4')
                memberships = [membership.text.strip() for membership in memberships]
                const = 0
                try:
                    if 'location' not in memberships[0]:
                        memberships = ', '.join([line.strip() for line in memberships[0].split('\n') if line.strip() and 'Memberships' not in line])
                        const = 1
                    try:
                        if 'location' not in memberships[1] and const ==0:
                            memberships = ', '.join([line.strip() for line in memberships[1].split('\n') if line.strip() and 'Memberships' not in line])
                        elif 'location' not in memberships[2] and const ==0:
                            memberships = ', '.join([line.strip() for line in memberships[2].split('\n') if line.strip() and 'Memberships' not in line])
                    except:
                        memberships = '' 
                except:
                    memberships =''              
                print(memberships)
                data.append({
                    'compName': compName,
                    'compURL': compURL,
                    'HQaddress':HQaddress,
                    'Description': description,
                    'ContactNums':ContactNums,
                    'memberships':memberships
                })
            except AttributeError as e:
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
            ContactNums = item['ContactNums']
            memberships = item['memberships']

            # query = "SELECT * FROM listings_in WHERE compName = %s and compURL=%s and HQaddress = %s and Description = %s and ContactNums = %s and memberships = %s;"
            # cursor.execute(query, (compName, compURL,HQaddress, description, ContactNums, memberships))
            # result = cursor.fetchone()
            # if result is None:
            #     print("data not found so I'm adding it")
            #     sql = "INSERT INTO listings_in (compName, compURL, HQaddress, Description, ContactNums, memberships) VALUES (%s, %s, %s, %s, %s, %s)"

            #     cursor.execute(sql, (compName, compURL, HQaddress, description, ContactNums, memberships))


        # Commit the changes and close the connection
        cnx.commit()
        cursor.close()
        cnx.close()

def scrap_listing_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data from {url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    search_results = soup.find_all('div', class_='px-1 py-2')
    links = [result.text for result in search_results]
    print(links)
    return search_results

def scrap_listing_linksOne(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data from {url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    search_results = soup.find_all('div', class_='results results-listings mt-5 mt-lg-0')
    # print(f"Found {len(search_results)} search results.")
    return search_results
def scrap_listing_pageByPage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data from {url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    pages = soup.find_all('div', class_='col-lg order-1 order-lg-2')
    # print(f"Found {len(search_results)} search results.")
    return pages

def process_listing_links(search_results):
    data = []
    for result in search_results:
        try:
            links = result.find('a', class_='card card-action card-appear')['href'] 
            data.append({
                'Links':links,
            })
        except Exception as e:
            print(f"Error scraping data for result {links}: {e}")
    # print(data)
    return data

def process_listing_linksOne(search_results):
    data = []
    for result in search_results:
        try:
            links = result.find_all('a', class_='no-expand') 
            data = [link['href']  for link in links]
            data = list(set([link for link in data if '/companies/' in link]))
            # data.append({
            #     'LinksO':links,
            # })
        except Exception as e:
            print(f"Error scraping data for result {links}: {e}")
    # print(data)
    return data

def process_listing_pageByPage(search_results):
    data = []
    for result in search_results:
        try:
            links = result.find_all('a', class_='page-link')
            # data = [link['href'][-2]  for link in links]
            try:
                # int(max(data))
                data = [link['href'][-2:]  for link in links]
                data = [elem for elem in data if elem.isdigit()]
                data = int(max(data))
                return data
            except:
                data = data = [link['href'][-1]  for link in links]
                data = int(max(data))
                return data
            print(data)
            # data.append({
            #     'LinksN':links,
            # })
        except Exception as e:
            print(f"Error scraping data for result {links}: {e}")
    # print(data)
    return data

if __name__ == '__main__':
    
    url = 'https://www.mynewmarkets.com/markets'
    search_results = scrap_listing_links(url)
    if search_results:
        dataL = process_listing_links(search_results)
        # print(len(data[:]))
        i = 0
        try:
            for i in range(len(dataL)):
                # print(dataL[i]['Links'])
                urlres = dataL[i]['Links'] # this is the link for the lsiting search results
                search_results = scrap_listing_pageByPage(urlres)
                dataN = process_listing_pageByPage(search_results)
                k = 1
                print(f'accessing link {url}')
                # for k in range(len(dataN)):
                for k in range(1,dataN):
                    if k>1:
                        url = urlparse(urlres)._replace(query='').geturl()
                    url = f'{urlres}?page={k}'
                    # url = dataN[k] #the link for the page number
                    search_results = scrap_listing_linksOne(url)# main div that contains the listing cards
                    if search_results:
                        dataG = process_listing_linksOne(search_results) # list of 'view listing links' each one by it self
                        j = 0
                        print(f'accessing link {url}')
                        for j in range(len(dataG)):
                            # url = dataG[j] # this is the link for each listing by it self
                            url = 'https://www.mynewmarkets.com/companies/specialtyhumanservices'
                        # print(url)
                            print(f'accessing link {url}')
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
                            j=+1
                    k=+1
                print(f'done for {url}')
                i =+ 1
        except IndexError:
            print("No more links to scrap")