import os
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.lamudi.co.id/east-java/malang/house/buy/?page='

headers = {
    'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

result = []

#inspeksi nomor pages
num_pages = 0

for page in range(1, 100):
    num_pages += 1
    print('page:', num_pages)
    response = requests.get(url+str(page), headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

#process scraping
    headers_content = soup.find_all('div', 'row ListingCell-row ListingCell-agent-redesign')
    
    for content in headers_content:
        title = content.find('h3', 'ListingCell-KeyInfo-title').text.strip()
        try:
            location = content.find('div', 'ListingCell-KeyInfo-address ellipsis').text.strip()
        except:
            continue
        try:
            detail = ''.join(content.find('div', 'ListingCell-keyInfo-details').text.strip().split('\n'))
        except:
            continue
        try:
            price = content.find('span', 'PriceSection-FirstPrice').text.strip()
        except:
            continue
        try:
            agent = content.find('div', 'ListingDetail-agent-name').text.strip()
        except:
            continue
        try:
            status = content.find('span', 'verified').text.strip()
        except AttributeError:
            try:
                status = content.find('span', 'semi-verified').text.strip()
            except AttributeError:
                try:
                    status = content.find('span', 'not-verified').text.strip()
                except AttributeError:
                    continue
        try:
            description = content.find('div', 'ListingCell-shortDescription').text.strip()
        except:
            continue

    
        final_data = {
            'title': title,
            'location': location,
            'detail': detail,
            'price': price,
            'agent_name': agent,
            'agent_status': status,
            'description': description
        }
        result.append(final_data)

#print scrape data
# for data in result:
#     print(data)
    
csv_filename = 'data/lamudi_malang_house_scraping.csv'

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'location', 'detail', 'price', 'agent_name', 'agent_status', 'description']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    for data in result:
        csv_writer.writerow(data)
        
print(f"Hasil scraping data {csv_filename} berhasil!. Selamat!")