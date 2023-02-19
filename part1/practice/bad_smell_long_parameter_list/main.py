# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, state, speed, x, y, field):
        self.state = state
        self.speed = speed
        self.x = x
        self.y = y
        self.field = field

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError

    def move(self, field, direction):
        speed = self._get_speed()
        if direction == 'UP':
            field.set_unit(x=self.x + speed, y=self.y + speed, unit=self)
        elif direction == 'DOWN':
            field.set_unit(x=self.x, y=self.y - speed, unit=self)
        elif direction == 'LEFT':
            field.set_unit(x=self.x - speed, y=self.y, unit=self)
        elif direction == 'RIGTH':
            field.set_unit(x=self.x + speed, y=self.y, unit=self)


#     ...
