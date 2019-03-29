import random
import sys
import time
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
class Vehicle(object):

    def __init__(self, price, type, seats, brand, name, fueleff):

        self.price = price
        self.type = type
        self.seats = seats
        self.name = name
        self.brand=brand
        self.fueleff = fueleff

    def setbrand(self,brand):
        self.brand=brand
    def setprice(self,price):
        self.price = price
    def settype(self,type):
        self.type = type
    def setseats(self, seats):
        self.seats = seats
    def setname(self,name):
        self.name = name
    def setfueleff(self,fueleff):
        self.fueleff = fueleff


def getVehicles():
    # List we will use for all cars and then matching criteria
    vehicleList = []

    # ------------------------------------Database of Cars---------------------------------
    # Hans Fuhrmann Cars
    vehicleList.append(Vehicle(39490, "car", 5, "Dodge", "Challenger", 19))
    vehicleList.append(Vehicle(43095, "car", 5, "Dodge", "Charger", 20))
    vehicleList.append(Vehicle(41345, "suv", 7, "Dodge", "Durango", 22))
    vehicleList.append(Vehicle(57770, "truck", 5, "Ram", "3500", 15))
    vehicleList.append(Vehicle(36140, "truck", 5, "Ram", "1500", 15))
    vehicleList.append(Vehicle(57770, "truck", 6, "Ram", "3500", 15))
    vehicleList.append(Vehicle(36140, "truck", 6, "Ram", "1500", 15))
    vehicleList.append(Vehicle(131800, "car", 5, "BMW", "M6 Gran Coupe", 17))
    vehicleList.append(Vehicle(59765, "suv", 4, "BMW", "i3", 89))
    vehicleList.append(Vehicle(56800, "car", 5, "BMW", "3 series sedan", 26))
    vehicleList.append(Vehicle(86000, "suv", 7, "BMW", "X5", 22))
    vehicleList.append(Vehicle(173465, "car", 4, "BMW", "i8", 40))
    vehicleList.append(Vehicle(139700, "suv", 5, "Porsche", "Cayenne Turbo", 17))
    vehicleList.append(Vehicle(63700, "car", 2, "Porsche", "718 Cayman", 24))
    vehicleList.append(Vehicle(334000, "car", 2, "Porsche", "911 GT2 RS", 24))
    vehicleList.append(Vehicle(116800, "car", 4, "Porsche", "Panemera 4s", 24))
    vehicleList.append(Vehicle(150300, "car", 4, "Porsche", "Taycan", 310))
    vehicleList.append(Vehicle(10095, "car", 4, "Chevy", "Spark", 34))
    vehicleList.append(Vehicle(55795, "car", 4, "Chevy", "Camaro", 24))
    vehicleList.append(Vehicle(65180, "suv", 9, "Chevy", "Suburban", 18))
    vehicleList.append(Vehicle(52690, "truck", 6, "Chevy", "Silverado", 20))
    vehicleList.append(Vehicle(52690, "truck", 5, "Chevy", "Silverado", 20))
    vehicleList.append(Vehicle(40685, "truck", 5, "Chevy", "Colorado", 23))
    # Jae Ung Kim(Volvo, Buick, Subaru, Honda)
    vehicleList.append(Vehicle(59750, "suv", 5, "Volvo", "XC90", 21))
    vehicleList.append(Vehicle(46800, "suv", 5, "Volvo", "XC60", 20))
    vehicleList.append(Vehicle(40300, "suv", 5, "Volvo", "XC40", 23))
    vehicleList.append(Vehicle(59950, "car", 5, "Volvo", "S90", 22))
    vehicleList.append(Vehicle(166500, "truck", 5, "Volvo", "VNR 640", 15))
    vehicleList.append(Vehicle(50445, "car", 5, "Buick", "Lacrosse", 25))
    vehicleList.append(Vehicle(26500, "suv", 5, "Buick", "Encore", 26))
    vehicleList.append(Vehicle(38400, "suv", 5, "Buick", "Envision", 29))
    vehicleList.append(Vehicle(62200, "suv", 5, "Buick", "Enclave", 27))
    vehicleList.append(Vehicle(44145, "car", 5, "Buick", "Regal GS", 19))
    vehicleList.append(Vehicle(27995, "suv", 5, "Subaru", "Forester", 25))
    vehicleList.append(Vehicle(19995, "car", 5, "Subaru", "Impreza", 27))
    vehicleList.append(Vehicle(24995, "car", 5, "Subaru", "Legacy", 25))
    vehicleList.append(Vehicle(29295, "car", 5, "Subaru", "Outback", 25))
    vehicleList.append(Vehicle(27995, "car", 4, "Subaru", "BRZ", 21))
    vehicleList.append(Vehicle(21190, "car", 5, "Honda", "Civic Coupe", 26))
    vehicleList.append(Vehicle(33390, "car", 5, "Honda", "Accord Hybrid", 49))
    vehicleList.append(Vehicle(27990, "car", 5, "Honda", "Insight Hybrid", 55))
    vehicleList.append(Vehicle(40100, "car", 6, "Honda", "Clarity Plugin Hybrid", 42))
    vehicleList.append(Vehicle(40790, "truck", 5, "Honda", "Ridgeline", 26))
    # Pierre Frigon(Toyota, Mazda, Jeep, Tesla)
    vehicleList.append(Vehicle(16595, "car", 5, "Toyota", "Yaris", 30))
    vehicleList.append(Vehicle(27650, "car", 5, "Toyota", "Prius", 53))
    vehicleList.append(Vehicle(27990, "suv", 5, "Toyota", "RAV4", 25))
    vehicleList.append(Vehicle(37300, "suv", 8, "Toyota", "Highlander", 20))
    vehicleList.append(Vehicle(39625, "truck", 5, "Toyota", "Tundra", 14))
    vehicleList.append(Vehicle(39625, "truck", 6, "Toyota", "Tundra", 14))
    vehicleList.append(Vehicle(15995, "car", 5, "Mazda", "3", 29))
    vehicleList.append(Vehicle(32888, "car", 5, "Mazda", "6", 24))
    vehicleList.append(Vehicle(38888, "suv", 5, "Mazda", "CX-9", 21))
    vehicleList.append(Vehicle(29845, "suv", 5, "Mazda", "cx-5", 24))
    vehicleList.append(Vehicle(46595, "car", 2, "Mazda", "MX-5 RF", 26))
    vehicleList.append(Vehicle(33103, "suv", 4, "Jeep", "Wrangler", 23))
    vehicleList.append(Vehicle(31305, "suv", 5, "Jeep", "Cherokee", 24))
    vehicleList.append(Vehicle(27297, "suv", 5, "Jeep", "Compass", 17))
    vehicleList.append(Vehicle(37862, "suv", 8, "Jeep", "Grand Cherokee", 21))
    vehicleList.append(Vehicle(20745, "suv", 5, "Jeep", "Renegade", 20))
    vehicleList.append(Vehicle(55985, "truck", 5, "Jeep", "Gladiator", 16))
    vehicleList.append(Vehicle(53400, "car", 5, "Tesla", "Model 3", 999))
    vehicleList.append(Vehicle(124600, "car", 7, "Tesla", "Model S", 999))
    vehicleList.append(Vehicle(127700, "suv", 6, "Tesla", "Model X", 999))
    vehicleList.append(Vehicle(257000, "car", 4, "Tesla", "Roadster 2", 999))
    # Kenny Cars
    vehicleList.append(Vehicle(63100, "car", 5, "Mercedes", "E 300 4MATIC Sedan", 29))
    vehicleList.append(Vehicle(47300, "suv", 5, "Mercedes", "GLC 300 4MATIC SUV", 27))
    vehicleList.append(Vehicle(47400, "suv", 5, "Mercedes", "C 300 4MATIC Wagon", 27))
    vehicleList.append(Vehicle(60200, "suv", 5, "Mercedes", "GLC 350e 4MATIC", 74))
    vehicleList.append(Vehicle(60500, "car", 2, "Mercedes", "SLC 300 Roadster", 27))
    vehicleList.append(Vehicle(42900, "suv", 9, "Mercedes", "Sprinter 4x4", 17))
    vehicleList.append(Vehicle(102750, "car", 4, "Lexus", "LC 500", 16))
    vehicleList.append(Vehicle(55350, "suv", 5, "Lexus", "RX 350", 19))
    vehicleList.append(Vehicle(64500, "suv", 5, "Lexus", "RX 450H", 31))
    vehicleList.append(Vehicle(66250, "suv", 7, "Lexus", "RX 350L", 25))
    vehicleList.append(Vehicle(134200, "car", 5, "Lexus", "LS 500H", 31))
    vehicleList.append(Vehicle(72649, "truck", 5, "Ford", "F-150 Raptor", 18))
    vehicleList.append(Vehicle(44099, "truck", 5, "Ford", "Super Duty F-250 XLT", 15))
    vehicleList.append(Vehicle(72649, "truck", 6, "Ford", "F-150 Raptor", 18))
    vehicleList.append(Vehicle(44099, "truck", 6, "Ford", "Super Duty F-250 XLT", 15))
    vehicleList.append(Vehicle(394330, "car", 5, "Ford", "Taurus SEL", 26))
    vehicleList.append(Vehicle(17168, "car", 5, "Ford", "SE HATCH", 39))
    vehicleList.append(Vehicle(76049, "car", 8, "Ford", "Expedition Limited MAX", 21))
    vehicleList.append(Vehicle(36900, "suv", 5, "Audi", "Q2", 37))
    vehicleList.append(Vehicle(44536, "car", 5, "Audi", "A3", 33))
    vehicleList.append(Vehicle(93206, "car", 5, "Audi", "RS 5 Coupé", 27))
    vehicleList.append(Vehicle(48003, "car", 5, "Audi", "A4 Avant", 27))
    vehicleList.append(Vehicle(68537, "car", 5, "Audi", "S4 Avant", 30))
    # Tayler Verhaegen(Nissan, KIA, Volkswagen, Cadillac)
    vehicleList.append(Vehicle(36498, "truck", 5, "Nissan", "Titan", 15))
    vehicleList.append(Vehicle(33198, "suv", 7, "Nissan", "Pathfinder", 20))
    vehicleList.append(Vehicle(27998, "car", 5, "Nissan", "Altima", 27))
    vehicleList.append(Vehicle(26798, "suv", 5, "Nissan", "Rouge", 33))
    vehicleList.append(Vehicle(24498, "truck", 4, "Nissan", "Frontier", 17))
    vehicleList.append(Vehicle(20095, "suv", 5, "KIA", "Soul", 26))
    vehicleList.append(Vehicle(14795, "car", 5, "KIA", "Rio", 29))
    vehicleList.append(Vehicle(22495, "car", 5, "KIA", "Forte", 31))
    vehicleList.append(Vehicle(39995, "car", 5, "KIA", "Stinger", 22))
    vehicleList.append(Vehicle(28495, "suv", 7, "KIA", "Sedona", 18))
    vehicleList.append(Vehicle(24475, "car", 4, "Volkswagen", "Bettle", 43))
    vehicleList.append(Vehicle(22500, "car", 5, "Volkswagen", "Golf", 30))
    vehicleList.append(Vehicle(32995, "car", 5, "Volkswagen", "Passat", 45))
    vehicleList.append(Vehicle(29225, "suv", 5, "Volkswagen", "Tiguan", 38))
    vehicleList.append(Vehicle(47995, "car", 5, "Volkswagen", "Arteon", 39))
    vehicleList.append(Vehicle(87595, "suv", 8, "Cadillac", "Escalade", 14))
    vehicleList.append(Vehicle(44895, "suv", 5, "Cadillac", "XT5", 19))
    vehicleList.append(Vehicle(86870, "car", 5, "Cadillac", "CT6 Plug In", 62))
    vehicleList.append(Vehicle(46995, "car", 5, "Cadillac", "CTS", 14))
    vehicleList.append(Vehicle(68645, "car", 5, "Cadillac", "ATS", 22))
    # Bonus cars
    vehicleList.append(Vehicle(1150000, "car", 2, "Mclaren", "P1", 34))
    vehicleList.append(Vehicle(232000, "suv", 5, "Lamborghini", "Uras", 14))
    vehicleList.append(Vehicle(274390, "car", 2, "Lamborghini", "Huracan", 12))
    vehicleList.append(Vehicle(443804, "car", 2, "Lamborghini", "Aventador", 11))
    vehicleList.append(Vehicle(515000, "truck", 4, "Mercedes", "G63 AMG", 13))
    vehicleList.append(Vehicle(1499, "car", 1, "John Deere", "Ride-along Mower", 4))
    vehicleList.append(Vehicle(5, "car", 2, "Cardboard", "Box", 999))
    vehicleList.append(Vehicle(7000, "car", 4, "Toyota", "Celica", 32))



    # ------------------------------------------End of Database-------------------------------------------------------------------
    return vehicleList
#Variables for saving user information and stopping condition for end of program
vehicleList = getVehicles()

endcondition = False
#----------------------------------------Text input and responses for text-matching-----------------------------------------------

greetings_i = ("yes", "yup","car","truck","suv","sure","ok","okay","perhaps","great")
greetings_r = ("Excellent, let's start with your name", "That's great to hear, what can I call you?", "Before I help you, could you please enter your name?")
greetings2_i=("no","nah","thanks","good", "okay", "ok","great")
greetings2_r=("Well have an excellent day!","I'm sorry to hear that, goodbye", "That's unfortunate",":(")
good_i = ("excellent", "good", "great", "alright", "fine", "well","aight","dec", "amazing")
good_r = ("That's awesome, let's get into some car details then.", "I love the enthusiasm, let's get you behind the wheel of a new car!", ":)")
bad_i=("no","nah","bad","not","laid","been","hanging","sad","mad","depressed","lonely","down")
bad_r=("That's awful, maybe a car can cheer you up!","That's depressing, let's get you a car and get you outta here", "Aw, well I'm sure a car will cheer you up!",":(")
welcome = ("Welcome to Autobot, can I assist you today?", "Hello, my name is Autobot, can I help you find a vehicle today?", "Good day! My name is Autobot, can we get you rolling in a new vehicle?")
seats_i = ("seats", "seating", "seats,", "seating,")
seats_r = ("How many seats would you like?", "Most of our cars have anywhere from 2 to 8 seats, how many will you need?")
fuel_i = ("fuel", "fuel efficiency", "fuels", "fuel,", "fuel efficiency,", "fuels,")
fuel_r = ("What is the worst fuel efficiency you would be okay with? \n (Anything above 100mpg is considered electric)")
price_i = ("price", "cost", "amount", "price,", "cost,", "amount,")
price_r = ("What is the maximum you would like to spend?", "How much are you looking to spend?")
type_i = ("type", "function", "type,", "function,")
type_r = ("Are you looking for a car, truck or suv?", "Are you a car, truck, or suv kind of person?")
brand_i = ("brand", "brand,", "make", "make,")
brand_r = ("What brand are you after?", "What brand are you interested in?")
ending_i = ("yes", "thanks", "good", "yea", "yeah","sure","cool","absolutely","okay","ok")
#---------------------------Functions for text-finding given a sentance as input---------------------------------------
#ToString method for a vehicle
def tostring(Vehicle):
    print("Here is a/an "+Vehicle.type+". \nIt is a 2019 "+Vehicle.brand+" "+Vehicle.name+", it seats "+str(Vehicle.seats)+" \nand gets "+str(Vehicle.fueleff)+
          " miles to the gallon. \nYou can walk away with this "+Vehicle.type+" for $"+str(Vehicle.price))
    if (Vehicle.fueleff > 100):

        print("This vehicle is also electric!")

from random import randrange
#Method that takes random car from list. Once we have narrowed down the list, we can use this to show the user a possible car match
def getcar(list):
    index = randrange(len(list))
    vehicle = list.pop(index)
    tostring(vehicle)
    return vehicle
def check_greeting(sentance):
    words = sentance.split()
    for word in words:
        if word.lower() in greetings_i:
            print (random.choice(greetings_r))
def check_greeting2(sentance):
    words = sentance.split()
    for word in words:
        if word.lower() in greetings2_i:
            print (random.choice(greetings2_r))
def check_good(sentance):
    words = sentance.split()
    for word in words:
        if word.lower() in good_i:
            print (random.choice(good_r))
def check_bad(sentance):
    words = sentance.split()
    for word in words:
        if word.lower() in bad_i:
            print (random.choice(bad_r))
def check_name(username):
    name_r = ("Nice to meet you " + username, "Pleasure to meet you " + username, "Well " + username + ", I am at your service")
    print(random.choice(name_r))
def check_seats(sentance):
    words = sentance.split()
    for word in words:
        if word.lower() in seats_i:
            print(random.choice(seats_r))
            seats = input("Seats:")
            time.sleep(1)
            print(" . ")
            time.sleep(1)
            print(" . ")
            time.sleep(1)
            uservehicle.setseats(seats)
def check_brand(sentance):
    words = sentance.split()
    for word in words:
        if word.lower() in brand_i:
            print(random.choice(brand_r))
            brand = input("Brand:")
            time.sleep(1)
            print(" . ")
            time.sleep(1)
            print(" . ")
            time.sleep(1)
            uservehicle.setbrand(brand)
def check_fuel(sentence):
   words = sentence.split()
   for word in words:
       if word.lower() in fuel_i:
           print(fuel_r)
           fuel_eff = input("Fuel efficiency level(in mpg): ")
           time.sleep(1)
           print(" . ")
           time.sleep(1)
           print(" . ")
           time.sleep(1)
           uservehicle.setfueleff(fuel_eff)
def check_price(sentence):
   words = sentence.split()
   for word in words:
       if word.lower() in price_i:
           print(random.choice(price_r))
           price = input("Price $:")
           time.sleep(1)
           print(" . ")
           time.sleep(1)
           print(" . ")
           time.sleep(1)
           uservehicle.setprice(price)
def check_type(sentance):
    words = sentance.split()
    for word in words:
        if word.lower() in type_i:
            print(random.choice(type_r))
            type = input("Car, truck, or SUV:")
            time.sleep(1)
            print(" . ")
            time.sleep(1)
            print(" . ")
            time.sleep(1)
            uservehicle.settype(type.lower())
def runagain():
    ending_r = ("My pleasure " + username + ", have a great day!", "Well have a wonderful day " + username,"I'm glad I could help, bye for now!")
    sentance = input("Would you like to search for another vehicle?")
    time.sleep(1)
    print(" . ")
    time.sleep(1)
    print(" . ")
    time.sleep(1)
    words = sentance.split()
    for word in words:
        if word.lower() in greetings_i:
            print("\n")
            return True

        print(random.choice(ending_r))
        sys.exit()
def check_ending(sentance, username,vehicle):

    ending_r = ("My pleasure " + username + ", have a great day!", "Well have a wonderful day " + username,"I'm glad I could help, bye for now!")
    words = sentance.split()
    for word in words:
        if word.lower() in ending_i:
            finance = input("Would you like to know lease option for this vehicle?")
            time.sleep(1)
            print(" . ")
            time.sleep(1)
            print(" . ")
            time.sleep(1)
            # entering okay does'nt work

            words = finance.split()
            for word in words:
                if word.lower() in ending_i:
                    years = input("In how many years would you like to pay off your " + vehicle.name + "?")
                    time.sleep(1)
                    print(" . ")
                    time.sleep(1)
                    print(" . ")
                    time.sleep(1)
                    months = int(years) * 26
                    print("The rate would be $"+str(round(vehicle.price/months,2))+" bi-weekly for the next "+str(years)+" year/years")


            return True
    return False

#-----------------------------sentiment analysis----------------------------------


def word_feats(words):
    return dict([(word, True) for word in words])


positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)']
negative_vocab = ['bad', 'terrible', 'useless', 'hate', ':(', 'not', 'tired']
neutral_vocab = ['car', 'the', 'sound', 'was', 'is', 'price', 'did', 'know', 'words', 'not', 'okay']

positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

train_set = negative_features + positive_features + neutral_features

classifier = NaiveBayesClassifier.train(train_set)

# Predict


def predict(sentence):
    neg = 0
    pos = 0
    output = ""
    sentence = sentence
    sentence = sentence.lower()
    words = sentence.split(' ')
    for word in words:
        classResult = classifier.classify(word_feats(word))
        if classResult == 'neg':
            neg = neg + 1
        if classResult == 'pos':
            pos = pos + 1

    if abs(pos-neg) < 0.2:
        output = "I see, starting with a normal day..."
    elif pos > neg:
        output = "I can tell you're having a good day"
    elif neg > pos:
        output = "Sorry to hear that you're feeling sad"

    print(output)

    # for testing purpose
    # print('Positive: ' + str(float(pos) / len(words)))
    # print('Negative: ' + str(float(neg) / len(words)))

    # NER function


def extract_entities(text):
        entities = []
        for sentence in sent_tokenize(text):
            chunks = ne_chunk(pos_tag(word_tokenize(sentence)))
        entities.extend([chunk for chunk in chunks if hasattr(chunk, 'label')])
        return entities




# -------------------------------------------Code for actual program-----------------------------------------------
print(random.choice(welcome))
print("We currently have "+str(len(vehicleList))+" vehicles in our inventory.")
sentance = input()
time.sleep(1)
print(" . ")
time.sleep(1)
print(" . ")
time.sleep(1)
check_greeting(sentance)
check_greeting2(sentance)
username = input("Name:")
time.sleep(1)
print(" . ")
time.sleep(1)
print(" . ")
time.sleep(1)
check_name(username)
print(extract_entities(username))
sentance = input("How is your day going?\n")
time.sleep(1)
print(" . ")
predict(sentance)

time.sleep(1)
print(" . ")
time.sleep(1)
check_bad(sentance)
check_good(sentance)
endconditionmain = False
while(endconditionmain==False):
    uservehicle = Vehicle(9999999, "", 0, "", "", 999)
    endcondition = False
    vehicleList = getVehicles()
    print("What are some important aspects you want in \nyour vehicle?")

    sentance = input(
        "Currently we support the following features: \n -Fuel Efficiency \n -Seating \n -Price \n -Type of vehicle\n -Brand\n")

    check_seats(sentance)

    check_brand(sentance)

    check_type(sentance)

    check_fuel(sentance)

    check_price(sentance)
    if (int(uservehicle.price) < 9999999):
        vehicleList = [vehicle for vehicle in vehicleList if vehicle.price <= int(uservehicle.price)]
    if (uservehicle.type != ""):
        vehicleList = [vehicle for vehicle in vehicleList if vehicle.type == uservehicle.type]
    if (uservehicle.brand != ""):
        vehicleList = [vehicle for vehicle in vehicleList if vehicle.brand.lower() == uservehicle.brand.lower()]
    if (int(uservehicle.fueleff) < 999):
        vehicleList = [vehicle for vehicle in vehicleList if vehicle.fueleff >= int(uservehicle.fueleff)]
    if (int(uservehicle.seats) > 0):
        vehicleList = [vehicle for vehicle in vehicleList if vehicle.seats == int(uservehicle.seats)]
    time.sleep(1)
    print(" . ")
    time.sleep(1)
    print(" . ")
    time.sleep(1)
    print(" . ")
    time.sleep(1)
    print(" . ")
    time.sleep(1)
    print("\nI have found " + str(len(vehicleList)) + " vehicles that match your criteria!")
    while (endcondition == False):
        print("\n")
        if (len(vehicleList) == 0):
            print("I'm sorry, none of our cars match that criteria")


            break

        vehicle = getcar(vehicleList)
        sentance = input("Are you happy with this vehicle?" )
        time.sleep(1)
        print(" . ")
        time.sleep(1)
        print(" . ")
        time.sleep(1)
        endcondition = check_ending(sentance, username, vehicle)
        if (len(vehicleList) < 1):
            print("I'm sorry, that is all the cars that match the given criteria.")
            break
    runagain()