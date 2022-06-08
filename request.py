import requests

req = requests.get('https://stepic.org/media/attachments/course67/3.6.2/833.txt').text.splitlines()
print(len(req))
