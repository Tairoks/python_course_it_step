"""
Перед вами имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен.
Ключами словаря на любом уровне могут быть только строки, значения - только числа.

Учитывая указанные выше условия, ваша задача состоит в том,
чтобы преобразовать этот вложенный словарь в плоский (состоящий только из одного уровня),
где ключи формируются конкатенацией вложенных ключей, соединенных знаком _

Для этого необходимо определить рекурсивную функцию flatten_dict.
Она должна принимать вложенный словарь и возвращать плоский
"""
nested = {'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}
#{'Q_w_E_r_T_y': 123}

nested_ = {'Germany': {'berlin': 7},
          'Europe': {'italy': {'Rome': 3}},
          'USA': {'washington': 1, 'New York': 4}}
# {'Germany_berlin': 7, 'Europe_italy_Rome': 3, 'USA_washington': 1, 'USA_New York': 4}


def flatten_dict(d: dict, key_: str = '') -> dict:
    c = {}
    for key, value in d.items():
        if isinstance(value, dict):
            c.update(flatten_dict(value, key_ + '_' + key))
        else:
            c.update({key_ + '_' + key: value})
    return c


print(flatten_dict(nested_))