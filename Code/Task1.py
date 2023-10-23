"""
Открыть клиентский TCP сокет на google.com (порт 80), сказать в сокет "GET", получить ответ, сохранить в файл

1) откройте клиентский TCP сокет на smtp.gmail.com порт 587
2) поздоровайтесь с гуглом, скажите "EHLO google.com" (здесь не опечатка, именно EHLO)
3) ответ получите и выведите на экран
"""
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("smtp.gmail.com", 587))
sock.send(b"POST /EHLO google.com HTTP/1.1\r\nHost:smtp.gmail.com\r\n\r\n")
response = sock.recv(4096)
sock.close()
print(response.decode())
