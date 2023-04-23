import requests
from bs4 import BeautifulSoup
import json

#URL = "https://explorer.celo.org/mainnet/token/0x471EcE3750Da237f93B8E339c536989b8978a438/token-holders"
URL = "https://explorer.celo.org/mainnet/token/0x471ece3750da237f93b8e339c536989b8978a438/token-holders?address_hash=0x482c90e123e898acfdacde6f027d9599da503a11&items_count=100&value=1078748513136379888478800&type=JSON"

response = requests.get(URL).json()
arr = response["items"]

arr_string = ' '.join([str(elem) for elem in arr])

soup = BeautifulSoup(arr_string, 'html.parser')

holder_containers = soup.find_all('div', class_="col-md-7 col-lg-8 d-flex flex-column")

i = 0
for holder in holder_containers:
    # address = holder.find('span', class_="d-none").text
    address = holder.span.a.span['data-address-hash']
    balance_raw = holder.find('span', class_='text-dark').text
    balance = balance_raw[:balance_raw.find(" ")]
    i = i + 1
    print(str(i) + " | " + address + " | " + balance)
    print("--------------------------------------" )

# holder_containers = str(soup.find('span', class_='text-dark').text)


# holder_container = str(soup.find('span', class_='text-dark').text)

# first_space = holder_container.find(" ")
# balance = holder_container[2:first_space]

# print(holder_containers)

# print(arr_string)