import json

class User:
    pass

class Parking:

    def jsonUse(self):
        with open("parking.json") as data_file:
            file = json.load(data_file)
            PlaceID = file['parking_place']['parking_ID']
            TimeRange = file['parking_place']['Time_range']
            return PlaceID, TimeRange

    def getloginData(self):
        log = input("choose between user/manager: ")
        user = "user"
        manager = "manager"
        if log == user:
            print(user)
        elif log == manager:
            print(manager)
        return log

    def __init__(self, FullName, phone, email, gender, age):
        self.FullName = FullName
        self.phone = phone
        self.email = email
        self.gender = gender
        self.age = age

    def getUserInfo(self, FirstName, LastName, phoneNumber, Age, Gender):
        self.FullName = FirstName + LastName
        self.email = FirstName + "_" + LastName
        self.phone = phoneNumber
        self.age = Age
        self.gender = Gender
        print(self.FullName, self.email, self.phone, self.age, self.gender)

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
    FirstName = input("Please input here your Name: ")
    LastName = input("Please input here your Surname: ")
    phoneNumber = input("Please write here your Phone Number: ")
    Age = input("Please insert here your age: ")
    Gender = input("Choose your gender (Male\Female): ")
    return FirstName, LastName, phoneNumber, Age, Gender


main()
