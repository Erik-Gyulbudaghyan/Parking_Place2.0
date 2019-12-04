class Login:

    def __init__(self):
        self.User = None

    def getloginData(self):
        if self.User == None:
            Log = input("For Login as user please write <User>: ")
            self.User = Log

    def printLoginData(self):
        print(self.User)

class User:

    def __init__(self):
        self.FullName = None
        self.phone = None
        self.email = None
        self.gender = None
        self.age = None

    def askUserPersonalName(self):
        if self.FullName == None and self.email == None:
            AskName = input("Please write your name: ")
            AskSurname = input("Please write your surname: ")
            self.FullName = AskName + " " + AskSurname
            self.email = AskName + "_" + AskSurname + "@gmail.com"

    def askUserPersonalInfo(self):
        if self.phone == None and self.age == None and self.gender == None:
            AskNumber = input("Please Input your Phone Number (+374 ........): ")
            self.phone = "+374" + AskNumber
            AskAge = input("Please write your age: ")
            self.age = AskAge
            AskGender = input("Please write your Gender (Male/Female): ")
            self.gender = AskGender

    def printUserPersonalInfo(self):
        print(self.FullName)
        print(self.phone)
        print(self.email)
        print(self.gender)
        print(self.age)
        print("___________")

    def __str__(self):
        return self.FullName + "/ " + self.phone + "/ " + self.email + "/ " + self.gender + "/ " + self.age

Initial_Capacity = 10

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BST:

    def __init__(self):
        self.rootval = None

    def __str__(self):
        if self.rootval ==None:
            return "Root is Empty"
        else:
            return str(self.rootval.data)

    def addNodeInfo(self, node):
        if self.rootval == None:
            self.rootval = node
        elif self.rootval.data == node.data:
            print("This data is not already exists")
        else:
            self.addInTree(node, self.rootval)

    def addInTree(self, node, Roots):
        if node.data<Roots.data:
            if Roots.left_child == None:
                Roots.left_child=node
            else:
                self.addInTree(node,Roots.left_child)
        else:
            if Roots.right_child == None:
                Roots.right_child=node
            else:
                self.addInTree(node,Roots.right_child)

    def printInOrder(self):
        if self.rootval != None:
            print("\n_______________")
            self.printInOrderResult(self.rootval)

    def printInOrderResult(self, Roots):
        if Roots != None:
            self.printInOrderResult(Roots.left_child)
            print(str(Roots.data), end=" ")
            self.printInOrderResult(Roots.right_child)

    def printParkingPlaceInfo(self):
        if self.printInOrderResult != None:
            print("\n_______________")
            ParkingPlaceInfo = ("place N1/ " + "place N2/ " + "place N3/ " + "place N4/ " + "place N5/ " + "place N6/ " + "place N7/ " + "place N8/ " + "place N9/ " + "place N10/ ")
            print(ParkingPlaceInfo)

class Parking:

    def __init__(self):
        self.ParkingPlace = None

    def AskForParkingPlace(self):
        if self.ParkingPlace == None:
            print("\n_______________")
            AskForPlace = input("Choose your Place: ")
            self.ParkingPlace = AskForPlace

    def printParkingPlace(self):
        print(self.ParkingPlace)

    def __str__(self):
        return self.ParkingPlace

class LinkedList2:

    def __init__(self):
        self.headval = None

    def listPrint(self):
        printval = self.headval
        while printval is not None:
            print(printval.data)
            printval = printval.next

class Time:

    def __init__(self):
        self.Time = None
        self.Price = None

    def AskForTime(self):
        if self.Time == None and self.Price == None:
            AskTime = input("Please Choose your time range: ")
            self.Time = AskTime

    def getTimeinfo(self):
        if self.Time == "1" or "2":
            self.Time = ("range 0-2 Hours")
            self.Price = ("100")

    def getTimeinfo2(self):
        if self.Time == "3" or "4" or "5":
            self.Time = ("range 2-5 Hours")
            self.Price = ("300")

    def getTimeinfo3(self):
        if self.Time == "6" or "7" or "8" or "9" or "10":
            self.Time = ("range 5-10 Hours")
            self.Price = ("500")

    def getTimeinfo4(self):
        if self.Time == "11" or "12" or "13" or "14" or "15" or "16":
            self.Time = ("range 10-16 Hours")
            self.Price = ("800")

    def getTimeinfo5(self):
        if self.Time == "17" or "18" or "19" or "20":
            self.Time = ("range 16-20 Hours")
            self.Price = ("1500")

    def getTimeinfo6(self):
        if self.Time == "21" or "22" or "23" or "24":
            self.Time = ("range 20-24 Hours")
            self.Price = ("2000")

    def printTimeAndPrice(self):
        print(self.Time)
        print(self.Price)

    def __str__(self):
        return self.Time

class Manager:

    def __init__(self):
        self.Manager = None
        self.FullName = None
        self.ID = None

    def LoginManager(self):
        if self.Manager == None:
            Login = input("For Login as Manager please write <Manager>: ")
            self.Manager = Login

    def getManagerInfo(self):
        if self.FullName == None:
            AskForName = input("Please write your Name: ")
            AskForSurname = input("Please write your Surname: ")
            self.FullName = AskForName + "-" + AskForSurname

    def getManagerID(self):
        if self.ID == None:
            AskID = input("Please write your ID: ")
            self.ID = AskID

    def printInfo(self):
        print(self.FullName)
        print(self.ID)

    def ParkingInformation(self):
        AskInfo = input("To see the list of users please write Yes: ")
        if AskInfo == "Yes":
            print("List of Current Users: ")


def main():

    Log = Login()

    Log.getloginData()
    Log.printLoginData()

    Us1 = User()

    Us1.askUserPersonalName()
    Us1.askUserPersonalInfo()
    Us1.printUserPersonalInfo()


    PlaceTree = BST()
    print(PlaceTree)

    myNode = Node(2)
    PlaceTree.addNodeInfo(myNode)
    myNode = Node(5)
    PlaceTree.addNodeInfo(myNode)
    myNode = Node(3)
    PlaceTree.addNodeInfo(myNode)
    myNode = Node(1)
    PlaceTree.addNodeInfo(myNode)
    myNode = Node(8)
    PlaceTree.addNodeInfo(myNode)
    myNode = Node(4)
    PlaceTree.addNodeInfo(myNode)
    myNode = Node(7)
    PlaceTree.addNodeInfo(myNode)
    myNode = Node(10)
    PlaceTree.addNodeInfo(myNode)
    myNode = Node(6)
    PlaceTree.addNodeInfo(myNode)
    myNode = Node(9)
    PlaceTree.addNodeInfo(myNode)
    PlaceTree.printInOrder()
    PlaceTree.printParkingPlaceInfo()

    Usr1 = Parking()
    Usr1.AskForParkingPlace()
    Usr1.printParkingPlace()

    TimeList = LinkedList2()
    TimeList.headval = Node("range 0-2 Hours: 100 AMD")
    t2 = Node("range 2-5 Hours: 300 AMD")
    t3 = Node("range 5-10 Hours: 500 AMD")
    t4 = Node("range 10-16 Hours: 800 AMD")
    t5 = Node("range 16-20 Hours: 1500 AMD")
    t6 = Node("range 20-24 Hours: 2000 AMD")

    TimeList.headval.next = t2

    t2.next = t3
    t3.next = t4
    t4.next = t5
    t5.next = t6

    TimeList.listPrint()

    Uss1 = Time()
    Uss1.AskForTime()
    Uss1.getTimeinfo()
    Uss1.getTimeinfo2()
    Uss1.getTimeinfo3()
    Uss1.getTimeinfo4()
    Uss1.getTimeinfo5()
    Uss1.getTimeinfo6()
    Uss1.printTimeAndPrice()

    print("_________________")

    manager = Manager()
    manager.LoginManager()
    manager.getManagerInfo()
    manager.getManagerID()
    manager.printInfo()
    manager.ParkingInformation()

    print("_________________")

    print(Us1.printUserPersonalInfo(), Usr1.printParkingPlace(), Uss1.printTimeAndPrice())

main()
