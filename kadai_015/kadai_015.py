class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printinfo(self):
        print(f'名前:{self.name}, 年齢:{self.age}')

taro = Human("taro", 23)
jiro = Human("jiro", 55)

taro.printinfo()
jiro.printinfo()