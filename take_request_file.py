import requests

request_data = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt').text

while not request_data.startswith('We'):
    link = f'https://stepic.org/media/attachments/course67/3.6.3/{request_data}'
    request_data = requests.get(link).text

print(f'{request_data}')
