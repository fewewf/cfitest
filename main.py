import re
import random
import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
}

ips = []
cidr = []
result = ''

if __name__ == '__main__':
    with open('ipv4.txt', 'r') as f:
        cidr = f.read()

    cidr = re.findall('[0-9]+.[0-9]+.[0-9]+.', cidr)
    ips = [ip + str(random.randint(1, 255)) for ip in cidr]

    for ip in ips:
        try:
            x = requests.get(url='http://' + ip + '/cdn-cgi/trace', headers=header, timeout=1)
            result = result + ip + ' ' + re.findall('colo=[A-Z]{3}', x.text)[0] + '\n'
        except requests.exceptions.RequestException as e:
            result = result + ip + ' timeout' + '\n'

    with open('result.txt', 'w') as f:
        f.write(result)
