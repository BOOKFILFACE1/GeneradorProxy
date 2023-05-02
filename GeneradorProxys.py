import requests
from bs4 import BeautifulSoup
import random

url = 'https://hidemy.name/es/proxy-list/'

response = requests.get(url)

def get_proxies(content):
soup = BeautifulSoup(conten, 'html.parser')
proxies =[]
table = soup.find('table', {'class':'proxy__t'})
rows = table.tbody.find_all('tr')
for row in rows:
    columns = row.find_all('tr')
    ip = columns[0].text.strip()
    port = columns[1].text.strip()
    protocol = columns[4].text.strip()
    proxies.append({'ip':ip, 'port': port, 'protocol': protocol})
    return proxies


    proxies_list = get_proxies(response.conten)

    random
    random_proxy = random.choice(proxies_list)

    print(f"Proxy seleccionado: {random_proxy['protocol']}://{random_proxy[ip]}:{random_proxy['port']}")