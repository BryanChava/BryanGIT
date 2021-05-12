# BRYAN CHAVARRIA
# 1657040
# FINAL PROJ. PART 2

import csv
from operator import itemgetter

# substitution and creating lists to pull the csv data. mnL = manufacturerlist, peL= price list, sdL= service list.
mnL = []
peL = []
sdL = []

# applying the data to the lists above from each cvs file, and appending each one.
with open("ManufacturerList.csv") as manufacturerlist:
    manuL = csv.reader(manufacturerlist)
    for line in mnL:
        mnL.append(line)
with open("PriceList.csv") as pricelist:
    priL = csv.reader(pricelist)
    for line in peL:
        peL.append(line)
with open("ServiceDatesList.csv") as servicelist:
    serL = csv.reader(servicelist)
    for line in serL:
        sdL.append(line)

# making sortment to each list by the order ID which will allow them to be lined up correctly.
mnL2 = (sorted(mnL, key=itemgetter(0)))
peL2 = (sorted(peL, key=itemgetter(0)))
sdL2 = (sorted(sdL, key=itemgetter(0)))

# appending each of the missed service dates and prices to the main list through certain ranges.
for i in range(0, len(mnL2)):
    mnL2[i].append(peL[i][1])

for i in range(0, len(mnL2)):
    mnL2[i].append(sdL[i][1])

finalList = mnL2

fullInventory = (sorted(finalList, key=itemgetter(1)))

# making the full inventory file along with the full inventory list in order to write them in.
with open('FullInventory.csv', 'w') as file1:
    filewrite = csv.writer(file1)
    for i in range(0, len(fullInventory)):
        filewrite.writerow(fullInventory[i])
# making conversion for itemtype as finalList, and allowing substitution for tower list, laptop list, and phone list.
itemtype = finalList
towerlist = []
laptoplist = []
phonelist = []

# checking each of the list for a certain item types and appending each of them seperately into their own lists.
for i in range(0, len(itemtype)):
    if itemtype[i][2] == "tower":
        towerlist.append(itemtype[i])
    elif itemtype[i][2] == "phone":
        phonelist.append(itemtype[i])
    elif itemtype[i][2] == "laptop":
        laptoplist.append(itemtype[i])

# writing a file for each item with the csv files within a certain range.
with open('LaptopInventory.csv', 'w') as file1:
    liswrite = csv.writer(file1)
    for i in range(0, len(laptoplist)):
        liswrite.writerow(laptoplist[i])

with open('PhoneInventory.csv', 'w') as file1:
    phowrite = csv.writer(file1)
    for i in range(0, len(phonelist)):
        phowrite.writerow(phonelist[i])

with open('TowerInventory.csv', 'w') as file1:
    tiswrite = csv.writer(file1)
    for i in range(0, len(towerlist)):
        tiswrite.writerow(towerlist[i])

# making a list specifically for damaged products and applying the ranges.
damagedlist = []

for i in range(0, len(itemtype)):
    if itemtype[i][3] == "damaged":
        damagedlist.append(itemtype[i])
damagedlist = (sorted(damagedlist, key=itemgetter(4), reverse=True))

# making a damaged products file
with open('DamagedInventory.csv', 'w') as file1:
    damawrite = csv.writer(file1)
    for i in range(0, len(damagedlist)):
        damawrite.writerow(damagedlist[i])

# creating user input and asking them what type of manufacturer and what item type.
usermanufacture = str(input("Enter your manufacturer: "))
usertype = str(input("Please enter your item type: "))
useritem = []

# creating the exit value as the letter "q" so the input does not equal to a, and so the program can be executed.
while usermanufacture != "q":
    for i in range(0, len(finalList)):
        if usermanufacture in finalList[i] and usertype in finalList[i]:
            useritem.append(finalList[i])
    if len(useritem) != 0:
        useritem = sorted(useritem, key=itemgetter(4), reverse=True)
        print("Your Item is: ", useritem[0])
# if there is nothing that was added to the list, then the "else" will take place
# that will let the user know that the product does not exist.
    else:
        print("No such item in Inventory")
    usermanufacture = str(input("Enter your manufacturer, or q to exit query: "))
    usertype = str(input("Please enter your item type: "))
