
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


    def EditPersonDetails(self, person):
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
        self.__GroupArray = []
        self.__GroupSize = GroupSize
    
    def GetGroupSize(self):
        return self.__GroupSize

    def AddPersons(self):
        groupsize = self.GetGroupSize(groupsize)
        for x in range():
            self.__GroupArray.append(Person)

    def ShowPersons(self):
        groupsize = self.GetGroupSize()
        for num in range(groupsize):
            self.__GroupArray[num].Display()
        
    def ListPersons(self):
        groupsize = self.GetGroupSize()
        for num in range(groupsize):
            self.__GroupArray[num].DisplayName()
        
    def EditPerson(self, placenum):
        self.__GroupArray[placenum] = self.__GroupArray[placenum].EditPersonDetails()


    def FindPerson(self, name):
        for x in range (self.GetGroupSize()):
            if name == self.__GroupArray[x].GetName():
                print(self.__GroupArray[x])
                
    def DisplayfromArray(self, number):
        print(self.__GroupArray[number])


## MAIN ##
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
            Newperson = Person()
        elif option == 2:
            Group.ListPersons()
        elif option == 3:
            person= int(input("Enter place number in array"))
            Group.DisplayfromArray(person)
        elif option == 4:
            Group.ShowPersons()
        elif option == 5:
            person = int(input("Enter place number of person"))
            Group.EditPerson(person)
        elif option == 6:
            ID = int(input("Enter persons name"))
            Group.FindPerson(ID)
        else:
            enter = False


main()











