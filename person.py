class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print ("Hi, I am {}".format(self.name))


john = Person("John Smith")
print (john.name)
john.talk()