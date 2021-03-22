print(a.position())  # Берём позицию курсора
print(a.size())  # Размер экрана
a.PAUSE = 0.5
a.move(-200, 300)  # Перемещение курсора
a.move(-200, 300, duration=0.5)  # Переход
a.moveTo(500, 500)
a.moveTo(100, 100, duration=1)  # Переход
a.click()

a.moveTo(1000, 1040)
a.click(button='right')
a.move(20, -100)
a.click(button='left')
print(a.pixel(500, 500))