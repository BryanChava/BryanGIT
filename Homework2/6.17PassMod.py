# BRYAN CHAVARRIA
# 1657040



password = input()


check_pass = ''


for letter in password:


    if(letter=='i'):

        check_pass+="!"


    elif(letter=='a'):

        check_pass += "@"


    elif (letter == 'm'):

        check_pass += "M"


    elif (letter == 'B'):

        check_pass += "8"


    elif (letter == 'o'):

        check_pass += "."


    else:

        check_pass += letter



check_pass += "q*s"

print(check_pass)
