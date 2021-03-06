# Bryan Wilfredo Chavarria
# 1657040
# Python Project CIS2348 Final Project Pt.1 (source)
# header info here
import csv
from operator import itemgetter

manufacturerList = []
priceList = []
serviceDatesList = []

# creating lists to append data from csv files

with open("ManufacturerList.csv") as manufacturerFile:
    readManufacList = csv.reader(manufacturerFile)
    for line in readManufacList:
        manufacturerList.append(line)

with open("PriceList.csv") as priceFile:
    readPriceList = csv.reader(priceFile)
    for line in readPriceList:
        priceList.append(line)

with open("ServiceDatesList.csv") as serviceDatesFile:
    readServiceDatesList = csv.reader(serviceDatesFile)
    for line in readServiceDatesList:
        serviceDatesList.append(line)
# opening and appending data to created lists


myManufacturerList = (sorted(manufacturerList, key=itemgetter(0)))
myPriceList = (sorted(priceList, key=itemgetter(0)))
myServiceDateList = (sorted(serviceDatesList, key=itemgetter(0)))
# creates new myList version of lists which are sorted alphabetically per required output

for myNum in range(0, len(myManufacturerList)):
    myManufacturerList[myNum].append(priceList[myNum][1])
for myNum in range(0, len(myManufacturerList)):
    myManufacturerList[myNum].append(serviceDatesList[myNum][1])
myList = myManufacturerList
# appends any needed prices and service dates from priceList and serviceDatesList onto new list
# myList now ready for future use with inventories

myFullInventory = (sorted(myList, key=itemgetter(1)))
with open("FullInventory.csv", "w") as myFile:
    writeFullInv = csv.writer(myFile)
    for myNum in range(0, len(myFullInventory)):
        writeFullInv.writerow(myFullInventory[myNum])
# initializing full inventory list and sorting alphabetically per required output
# opening fullinventory csv to write all info to new fullinventory file sorted alphabetically per required output

itemType = myList
towerList = []
laptopList = []
phoneList = []
# creating lists for itemType and each category of item type to further break down inventory

for myNum in range(0, len(itemType)):
    if itemType[myNum][2] == "tower":
        towerList.append(itemType[myNum])
    elif itemType[myNum][2] == "phone":
        phoneList.append(itemType[myNum])
    elif itemType[myNum][2] == "laptop":
        laptopList.append(itemType[myNum])
# searching for unique item types and appending to correlating list


with open("LaptopInventory.csv", "w") as myFile:
    writeLaptopInv = csv.writer(myFile)
    for myNum in range(0, len(phoneList)):
        writeLaptopInv.writerow(laptopList[myNum])

with open("PhoneInventory.csv", "w") as myFile:
    writePhoneInv = csv.writer(myFile)
    for myNum in range(0, len(phoneList)):
        writePhoneInv.writerow(phoneList[myNum])

with open("TowerInventory.csv", "w") as myFile:
    writeTowerInv = csv.writer(myFile)
    for myNum in range(0, len(towerList)):
        writeTowerInv.writerow(towerList[myNum])
# writing file for each item type that contains all info of inventories, sorted by item ID per required output

damagedList = []
for myNum in range(0, len(itemType)):
    if itemType[myNum][3] == "damaged":
        damagedList.append(itemType[myNum])
damagedList = (sorted(damagedList, key=itemgetter(4), reverse=True))
with open("DamagedInventory.csv", "w") as myFile:
    writeDamagedInv = csv.writer(myFile)
    for myNum in range(0, len(damagedList)):
        writeDamagedInv.writerow(damagedList[myNum])
# initializing damaged category list and writing/sorting from most expensive to least per required output
pastServiceList = []
for myNum in range(0, len(itemType)):
    if itemType[myNum][3] == "past service":
        damagedList.append(itemType[myNum])
pastServiceList = (sorted(pastServiceList, key=itemgetter(4), reverse=True))
with open("PastServiceDateInventory.csv", "w") as myFile:
    writePastServiceInv = csv.writer(myFile)
    for myNum in range(0, len(pastServiceList)):
        writePastServiceInv.writerow(pastServiceList[myNum])
# initializing PastServiceDate category list and writing/sorting from oldest to most recent per required output
# end
# start of user entry
userManufacturer = str(input("Enter your manufacturer: "))
userType = str(input("Please enter your item type: "))
userItem = []
while userManufacturer != "q":
    for myNum in range(0, len(myList)):
        if userManufacturer in myList[myNum] and userType in myList[myNum]:
            userItem.append(myList[myNum])

    if len(userItem) != 0:
        userItem = sorted(userItem, key=itemgetter(4), reverse=True)
        print("Your item is: ", userItem[0])
    else:
        print("No such item in Inventory")

    userManufacturer = str(input("Enter your manufacturer, or q to exit query: "))
    userType = str(input("Please enter your item type: "))
# executes main code for final list and user display of item and information
# q is exit value for loop/program and will give you final result after entry
# end
