#  Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для инкремента и декремента значения.
try:
    class Counter:
        def __init__(self, initial_value=0):
            self.value = initial_value

        def increment(self, step=1):
            self.value += step

        def decrement(self, step=1):
            self.value -= step

        def get_value(self):
            return self.value


    counter = Counter(5)
    counter.increment()
    counter.increment(2)
    counter.decrement()
    counter.decrement(3)

    print(counter.get_value())

except ValueError:
    print("Ошибка")