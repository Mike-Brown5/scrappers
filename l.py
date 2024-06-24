# # def last_s2_chars(input_string, s2):
# #     return input_string[-s2:]

# # input_string = "Geeksforgeeks"
# # s2 = 4
# # print(input_string[-2:])  # Output: eeks
# # from urllib.parse import urlparse, urlunparse

# # url = 'https://www.mynewmarkets.com/search/charter+bus+and+limousine+service?page=2'
# # parsed_url = urlparse(url)
# # url = urlparse(url)._replace(query='').geturl()

# # print(url)

# # input_list = ['apple', 'banana', 'cherry']
# # output_string = ', '.join(input_list)
# # print(output_string)  # Output: apple, banana, cherry

# import mysql.connector

# # Connect to the database
# # cnx = mysql.connector.connect(user='root', password='', host='localhost', database='sky_scraperdb')
# # cursor = cnx.cursor()

# # service = 'Alternative & Primary Insurance'
# # name1 = 'Allied Public Risk'
# # tags1 = 'Water Authories-Sewer Authorities-Emergency Transport-Fire & Water-Schools-Municipalities-Self Insured Retention-Community College-Volunteer Fire-+ 1 more'
# # description = 'Experience with public and quasi-public entities. Programs include WaterPlus, MuniPlus, FirePlus and JPRIMA.'
# # states = 'Alabama-Alaska-Arizona-Arkansas-California-Colorado-Connecticut-Delaware-District of Columbia-Florida-Georgia-Hawaii-Idaho-Illinois-Indiana-Iowa-Kansas-Kentucky-Louisiana-Maine-Maryland-Massachusetts-Michigan-Minnesota-Mississippi-Missouri-Montana-Nebraska-Nevada-New Hampshire-New Jersey-New Mexico-New York-North Carolina-North Dakota-Ohio-Oklahoma-Oregon-Pennsylvania-Rhode Island-South Carolina-South Dakota-Tennessee-Texas-Utah-Vermont-Virginia-Washington-West Virginia-Wisconsin-Wyoming'
# # # Check if the data already exists in the table
# # query = "SELECT * FROM listings_in WHERE Service = %s and Name=%s and Tags = %s and Description = %s and Availability = %s;"
# # cursor.execute(query, (service, name1,tags1, description, states))
# # result = cursor.fetchone()
# # print(result)
# # cnx.commit()
# # # If the result is None, insert the new data
# # if result is None:
# #     print("data not found so I'm adding it")
# #     query = "INSERT INTO listings_in (Service, Name, Tags, Description, Availability) VALUES (%s, %s, %s, %s, %s)"
# #     # data = (value,)
# #     cursor.execute(query, (service, name1,tags1, description, states))
# #     cnx.commit()

# # # Close the database connection
# # # cursor.close()
# # cnx.close()

# # complist = ['https://www.mynewmarkets.com/companies/contund', 'https://www.mynewmarkets.com/companies/contund', 'https://www.mynewmarkets.com/listings/x8wz3r', '#', 'https://www.mynewmarkets.com/companies/londonuw', 'https://www.mynewmarkets.com/companies/londonuw', 'https://www.mynewmarkets.com/listings/xrzw75', '#', 'https://www.mynewmarkets.com/companies/integrateduw', 'https://www.mynewmarkets.com/companies/integrateduw', 'https://www.mynewmarkets.com/listings/axh6bn', '#', 'https://www.mynewmarkets.com/companies/amwins', 'https://www.mynewmarkets.com/companies/amwins', 'https://www.mynewmarkets.com/listings/8c8klq', '#', 'https://www.mynewmarkets.com/companies/fluxins', 'https://www.mynewmarkets.com/companies/fluxins', 'https://www.mynewmarkets.com/listings/4wr3rp', '#', 'https://www.mynewmarkets.com/companies/ftpins', 'https://www.mynewmarkets.com/companies/ftpins', 'https://www.mynewmarkets.com/listings/x3vw39', '#', 'https://www.mynewmarkets.com/companies/natl', 'https://www.mynewmarkets.com/companies/natl', 'https://www.mynewmarkets.com/listings/4vp9qw', '#', 'https://www.mynewmarkets.com/companies/transportationrisk', 'https://www.mynewmarkets.com/companies/transportationrisk', 'https://www.mynewmarkets.com/listings/x6rqzz', '#', 'https://www.mynewmarkets.com/companies/btisinc', 'https://www.mynewmarkets.com/companies/btisinc', 'https://www.mynewmarkets.com/listings/x3v7w2', '#', 'https://www.mynewmarkets.com/companies/integrateduw', 'https://www.mynewmarkets.com/companies/integrateduw', 'https://www.mynewmarkets.com/listings/7iu3ts', '#', 'https://www.mynewmarkets.com/companies/hinterlandins', 'https://www.mynewmarkets.com/companies/hinterlandins', 'https://www.mynewmarkets.com/listings/4z8vq6', '#', 'https://www.mynewmarkets.com/companies/jmwilson', 'https://www.mynewmarkets.com/companies/jmwilson', 'https://www.mynewmarkets.com/listings/es7fio', '#', 'https://www.mynewmarkets.com/companies/mcneilandcompany', 'https://www.mynewmarkets.com/companies/mcneilandcompany', 'https://www.mynewmarkets.com/listings/96ep0e', '#', 'https://www.mynewmarkets.com/companies/amwins', 'https://www.mynewmarkets.com/companies/amwins', 'https://www.mynewmarkets.com/listings/xywrv7', '#', 'https://www.mynewmarkets.com/companies/jamesriverins', 'https://www.mynewmarkets.com/companies/jamesriverins', 'https://www.mynewmarkets.com/listings/2lluie']
# # companies_links = list(set([link for link in complist if '/companies/' in link]))
# # print(complist)
# # print(len(complist))
# # print(companies_links)
# # print(len(companies_links))
# # address = '''Company Headquarters
# #                             50 Brewery St., Ste. 8476

# #                             New Haven, CT 06530'''


# # lines = address.split('\n')


# # address = [line.strip() for line in lol if line.strip() and 'Memberships' not in line]

# # address = ' '.join(address)

# # print(address)

# # memberships = '\nMemberships\n                            WSIA, IIAB\n                        '
# # # lines = memberships.split('\n')
# # # memberships = [line.strip() for line in lines if line.strip() and 'Memberships' not in line]
# # memberships = ', '.join([line.strip() for line in memberships.split('\n') if line.strip() and 'Memberships' not in line])
# # print(memberships)

# # phone_data = 'Phone\n636-391-4841\nTollfree\n800-757-1905'
# # phone_data = 'Phone\n636-391-4841\nTollfree\n800-757-1905'
# # phone_list = [f'{text}: {number}' for text, number in zip(phone_data.split('\n')[:-1], phone_data.split('\n')[1:])]
# # phone_string = ', '.join(phone_list)
# # print(phone_string)
# # phone = 'Phone\n636-391-4841\nTollfree\n800-757-1905'

# # # Split the string into lines
# # # lines = phone_data.split('\n')

# # # Filter out empty lines
# # phone = [line.strip() for line in phone.split('\n') if line.strip()]

# # # Pair the text and numbers
# # phone = list(zip(phone[::2], phone[1::2]))

# # # Format the pairs as text:number
# # phone = ', '.join([f'{text}: {number}' for text, number in phone])

# # # Join the formatted pairs with commas
# # # result = ', '.join(phone)

# # print(phone)

# l1 = [1,2,3,4,5,6]
# l2 = [5,7,6,8,7,9,10]
# l3 = l1 + l2

# print(l3)

import ssl
print(ssl.OPENSSL_VERSION)
