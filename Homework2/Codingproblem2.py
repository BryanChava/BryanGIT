# BRYAN CHAVARRIA
# 1657040

# part-a

def extract_date(date) -> object:
    crrct_date = 0
    new_date = ""
    from datetime import date

    today = date.today()
    print("Today's date:", today)

    if date.find(",") != -1:
        mnth_day, year = date.split(',')

        if mnth_day.find(" ") != -1:
            month, day = mnth_day.split(" ")

            crrct_date = 1

            day = day.strip()
            month = month.strip()
            year = year.strip()

            if month == "January":
                new_date = "1" + "/"
            elif month == "February":
                new_date = "2" + "/"
            elif month == "March":
                new_date = "3" + "/"
            elif month == "April":
                new_date = "4" + "/"
            elif month == "May":
                new_date = "5" + "/"
            elif month == "June":
                new_date = "6" + "/"
            elif month == "July":
                new_date = "7" + "/"
            elif month == "August":
                new_date = "8" + "/"
            elif month == "September":
                new_date = "9" + "/"
            elif month == "October":
                new_date = "10" + "/"
            elif month == "November":
                new_date = "11" + "/"
            elif month == "December":
                new_date = "12" + "/"
            else:
                crrct_date = 0

            new_date += day + "/"

            new_date += year

    if crrct_date == 1:
        return new_date
    else:
        return ""


date = input()

while (date != "-1"):
    new_date = extract_date

    if new_date != "":
        print(new_date)

    print()
    date = input()
# part-b

file = open('InputDates.txt', 'r')
file_dates = []

file_dates = file.readlines()

file.close()

for i in range(len(file_dates) - 1):
    file_dates[i] = file_dates[i][:-1]

print("Input file content:\n")
for i in file_dates:
    print(i)

print("\nOutput\n")
for i in file_dates:
    if i == "-1":
        break

    new_date = extract_date(i)

    if new_date != "":
        print(new_date)
