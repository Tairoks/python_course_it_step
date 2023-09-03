"""
Написать класс `Cat`, создать ему атрибуты `size`, `color`, `cat_type`.

1.1. При создании объекта класса передавать в конструктор `color` и `cat_type`, которые записываются в соответсвующие
атрибуты.

1.2. Сделать метод `set_size`, в котором если `self.cat_type` это `indoor`, то `self.size = ‘small’` иначе `self.size =
’undefined’`. Протестируйте разные варианты.

1.3. Сделать класс Tiger, унаследованный от класса `Cat`.

1.4. Переопределить метод `set_size` таким образом чтобы если `self.cat_type это ‘wild’`, то `self.size = ‘big’` иначе
`self.size=’undefined’`
"""

class Cat:
    def __init__(self, color, cat_type, size='undefined'):
        self.color = color
        self.cat_type = cat_type
        self.size = size

    def set_size(self):
        if self.cat_type == 'indoor':
            self.size = 'small'
            return self.size
        else:
            return self.size


class Tiger(Cat):
    def __init__(self, cat_type, size='undefined'):
        Cat.__init__(self, cat_type, size)
        self.cat_type = cat_type

    def set_size(self):
        if self.cat_type == 'wild':
            self.size = 'big'
            return self.size
        else:
            return self.size

cat1 = Cat('black', 'indoor')
cat2 = Cat('orange', 'not indoor')
print(cat1.set_size())
print(cat2.set_size())
tiger1 = Tiger('not wild')
tiger2 = Tiger('wild')
print(tiger1.set_size())
print(tiger2.set_size())