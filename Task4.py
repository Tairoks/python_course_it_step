"""На вход программе подается вещественное число. Вывести первую цифру после запятой."""
a = 5.39432332
b = str(int((a * 10) % 10))

print('response: ' + b)
