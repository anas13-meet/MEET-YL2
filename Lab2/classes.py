class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sleep(self):
        print self.name + " of "+ self.age +" years old is sleeping"

    def eat(self):
        print self.name + " of " + self.age + " years old is eating banana"

class dog(Animal):
    def __init__(self, name, age, fur_color):
        Animal.__init__(self,name,age)
        self.fur_color= fur_color
    def bite(self):
        print "My dog, "+ self.name + " has a" + self.fur_color + " fur. He likes to bite. He is " +str(self.age) + "years old"

class bird(Animal):
    def __init__(self, name, age, wings_color):
        Animal.__init__(self,name,age)
        self.wings_color = wings_color
    def fly(self):
       print self.name + " hasn't started his life yet. He is " + str(self.age) + " years before birdy (B.Birdy)" + " Legend says that he is meant to be created " + self.wings_color
         
        
a= dog("banks",9, "black")
b= bird("birdy", -11, "colorless")
