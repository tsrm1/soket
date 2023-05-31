import socket

url = 'google.com'

print(f'IP adress {url}: {socket.gethostbyname(url)}')
