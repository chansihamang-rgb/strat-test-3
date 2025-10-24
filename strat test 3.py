class Cat :
    def __init__(self, name, color) :
        self.name = name
        self.color = color
    def meow(self):
        print('My name is {}, color is {}, meow meow~~'.format(self.name, self.color))

nabi = Cat('Nabi', 'Black')
nero = Cat('Nero', 'white')
mimi = Cat('Mimi', 'Brown')

nabi.meow()
nero.meow()
mimi.meow()