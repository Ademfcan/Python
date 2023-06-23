class person:
    
    def __init__(self, name : str, age: int, smart : bool) -> None:
        self.Name = name
        self.Age = age
        self.Smart = smart

    def getAge(self):
         return self.Age
        
    def getName(self):
         return self.Name
    
    def IsSmart(self):
         return self.Smart
    




p = person("",0,False)
name = "tbd"

print("Welcome to the online job interview")


def dataCollection():

        global name
        name = input("What is your name?: ")
        print("Ok " + name + " , I have a couple of basic questions to start")
        age = input("How old are you: ")
        HighSchool = input("Have you graduated highschool?(y/n): ")
        knowledge = input("What is the derivative of the SIN function?: ")
        knowledgeSimpl = input("What is i^2(i squared)?: ")
        global p
        p = person(name,age,knowledge or knowledgeSimpl)
        

        
    


dataCollection()
print("Hello " + p.getName() + " It is nice to meet you")
