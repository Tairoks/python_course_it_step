

def translator(money, currency):
    if currency == 'USD':
        return f'{round(money * 0.319, 2)} USD'
    if currency == 'EUR':
        return f'{round(money * 0.292, 2)} EUR'
    if currency == 'RUB':
        return f'{round(money * 0.333, 2)} RUB'
    else:
        return 'ERROR'
