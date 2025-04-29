# parent class
class person(object):

    #_init_is known as constructor
    def _init_(self, name, idnumber):
     self.name = Name
     self.idnumber = idnumber
    def display(self):
     print(self.name)
     print(self.idnumber)

# child class
class employee( person ):
    def _init_(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post 
        # invoking _init_ of the parent class
        person._init_ (self, name, idnumber)

# a creation of an object variable or an instance
a = employee('penguin', 20211041, 15000, "intern")

# calling a function of the class person using its intstance
a.display()