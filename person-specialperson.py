
class Person:
    global ID
    ID = 0
    def __init__(self):
        name, age, address = self.AskforDetails()
        self.AddPersonDetails(name, age, address)


    def AskforDetails(self):
        detail1 = input("Enter name:age:address : ")
        detail1 = detail1.split(":")
        return detail1


    def AddPersonDetails(self, name, age, address):
        ID + 1
        self.__name = name
        self.__age = age
        self.__address = address
        self.__ID = ID


    def EditPersonDetails(self):
        choice = 0
        while choice < 4:
            choice = int(input("Enter 1 to change name, 2 to change age, 3 to change address, 4 to exit: "))
            if choice == 1:
                name = input("Enter Name: ")
                self.__name = name
            elif choice == 2:
                age = input("Enter Age: ")
                self.__age = age
            elif choice == 3:
                address = input("Enter Address: ")
                self.__address = address

            self.Display()


    def AddTitle(self):
        self.__title = input("What title should be used: ")

    def Display(self):
        print()
        try:
            print(self.__title + self.__name + " is " + self.__age + " years old and lives in " + self.__address)
        except:
            print(self.__name + " is " + self.__age + " years old and lives in " + self.__address)
        print()

    def DisplayName(self):
        print(self.__name)
    
    def GetName(self):
        return self.__name
        

class SpecialPerson(Person):
    pass        


class Group:

    def __init__(self, GroupSize):
        self.__GroupDict = {}
        self.__GroupSize = GroupSize
    
    def GetGroupSize(self):
        return self.__GroupSize

    def AddPersons(self):
        person1 = Person()
        name = person1.GetName()
        self.__GroupDict[name] = person1

    def ShowPersons(self):
        for name in self.__GroupDict:
            self.__GroupDict[name].Display()
        
    def ListPersons(self):
        for name in self.__GroupDict:
            self.__GroupDict[name].DisplayName()
        
    def EditPerson(self, name):
        self.__GroupDict[name] = self.__GroupDict[name].EditPersonDetails()


    def FindPerson(self, name):
        for x in self.__GroupDict:
            if x == name:
                self.__GroupDict[name].Display()
                
    def DisplayfromDict(self, number):
        count = 0
        for x in self.__GroupDict:
            if count == number:
                return self.__GroupDict[x].Display()
            else:
                count += 1


## MAIN ##
Group1 = Group(1)
def main():
    enter = True
    while enter:
        print("")
        print("1. Create person(s)")
        print("2. List person(s)")
        print("3. Display Details of a Person")
        print("4. Display Details of all Persons")
        print("5. Edit Details of a person")
        print("6. Find person (using Name)")
        print("7. Exit")
        print("")

        option = int(input("Enter number here: "))
        if option == 1:
            Group1.AddPersons()
        elif option == 2:
            Group1.ListPersons()
        elif option == 3:
            num = int(input("Enter place number in array"))
            print(Group1.DisplayfromDict(num))
        elif option == 4:
            Group1.ShowPersons()
        elif option == 5:
            person = input("Enter name of person")
            Group1.EditPerson(person)
        elif option == 6:
            ID = input("Enter persons name")
            Group1.FindPerson(ID)
        else:
            enter = False


main()











