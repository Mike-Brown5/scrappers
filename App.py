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
        search_results = soup.find_all('div', class_='col-lg-8 mb-4 mb-lg-0')
        # print(f"Found {len(search_results)} search results.")
        return search_results

class DataProcessor:
    def process_search_results(self, search_results):
        data = []
        for result in search_results:
            try:
                service = result.find('h1', class_='listing-title mb-0').text.strip()
                # print(service)
                name = result.find('a', class_='font-weight-bold').text.strip()
                # print(name)
                tags = result.find_all('span', class_='badge badge-secondary badge-alt mt-2')
                tags = [tag.text.strip() for tag in tags]
                tags = ', '.join(tags)
                # print(tags)
                description = result.find('div', class_='listing-body').text.strip()
                # print(description)
                availability = result.find_all('span', class_='badge badge-secondary')
                availability = [state.text.strip() for state in availability]
                availability = ', '.join(availability)
                # print(availability)
                # availability_states = [state.strip() for state in availability.split(',')]
                # categorized_tags = [tag.strip() for tag in tags.split(',')]
                # data.append({
                #     'Service': service,
                #     'Name': name,
                #     **{f'Tags {i+1}': tag for i, tag in enumerate(categorized_tags)},
                #     'Description': description,
                #     **{f'Availability {i+1}': state for i, state in enumerate(availability_states)}
                # })
                data.append({
                    'Service': service,
                    'Name': name,
                    'Tags':tags,
                    'Description': description,
                    'Availability':availability
                })
            except AttributeError as e:
                print(f"Error scraping data for result {name}: {e}")
        return data

class DatabaseStorage:
    def __init__(self, db_config):
        self.db_config = db_config

    def store_data(self, data):
        cnx = mysql.connector.connect(**self.db_config)
        cursor = cnx.cursor()

        # Insert the data into the table
        for item in data:
            service = item['Service']
            name1 = item['Name']
            tags1 = item['Tags']
            description = item['Description']
            states = item['Availability']

            query = "SELECT * FROM listings_in WHERE Service = %s and Name=%s and Tags = %s and Description = %s and Availability = %s;"
            cursor.execute(query, (service, name1,tags1, description, states))
            result = cursor.fetchone()
            if result is None:
                print("data not found so I'm adding it")
                sql = "INSERT INTO listings_in (Service, Name, Tags, Description, Availability) VALUES (%s, %s, %s, %s, %s)"

                cursor.execute(sql, (service, name1, tags1, description, states))


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
    # print(f"Found {len(search_results)} search results.")
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
            links = result.find_all('a', class_='btn btn-primary no-expand px-4 mb-3 mb-md-0') 
            data = [link['href']  for link in links]
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
                            url = dataG[j] # this is the link for each listing by it self
                        # print(url)
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