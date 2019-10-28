import json

class User:

    def getloginData(self):
        log = input("choose between user/manager: ")
        user = "user"
        manager = "manager"
        if log == user:
            print(user)
        elif log == manager:
            print(manager)
        return log

    def __init__(self, FirstName, LastName, phoneNumber, Gender, Age):
        self.FullName = FirstName + " " + LastName
        self.phone = phoneNumber
        self.email = FirstName + "_" + LastName + "@email.com"
        self.gender = Gender
        self.age = Age
        self.ParkingPlace = []
        self.Time = []
        self.Price = []

    def getUserPersonalInfo(self):
        print(self.FullName)
        print(self.phone)
        print(self.email)
        print(self.gender)
        print(self.age)
        print("___________")

    def getUserParkingInfo(self,):
        self.ParkingPlace =

class Parking:

    def jsonUse(self):
        with open("parking.json") as data_file:
            file = json.load(data_file)
            PlaceID = file['parking_place']['parking_ID']
            TimeRange = file['parking_place']['Time_range']
            return PlaceID, TimeRange

    def askForPlace(self, initialParkPlaceData):
        place_code = initialParkPlaceData["parking_place"]["parking_ID"]
        print(place_code)
        current_place = input("Choose your parking place: ")

        while True:
            if int(current_place) not in range(0, 10):
                print("Your Data is Wrong, Please Try Again")
                current_place = input("Choose your parking place: ")
            if int(current_place) in range(0, 10):
                current_place_key = "00" + current_place
            else:
                break
            print(initialParkPlaceData["parking_place"]["parking_ID"][current_place_key])
            return initialParkPlaceData["parking_place"]["parking_ID"][current_place_key]

    def getTimeRange(self, TimeRange):
        Time = input("Please write your Time Range: ")
        while True:
            if Time in TimeRange:
                return Time
            else:
                Time = input("Your input is wrong please try again: ")


def main():
    Us1 = User("Erik", "Gyulbudaghyan","Male", 37493340147)
    
    Us1 = getUserPersonalInfo()
    print(Us1)

    current_place = askForPlace(parkPlace)
    print(current_place)

    Time = getTimeRange(TimeRange)
    print(Time)

main()
