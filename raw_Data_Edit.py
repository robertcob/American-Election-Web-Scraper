import re

#input '5/7 - 5/9'
#expected output '05-07-2020'
def Convert_Date_Format(old_Date):
    new_Date = '2020'
    number = ''
    num_List= []
    for word in old_Date:
        if word == "-" or word =='':
            break
        elif word == "/" or word ==' ':
            number = int(number)
            num_List.append(number)
            number = ''
        else:
            number += word
    for date_Fig in num_List:
        if date_Fig < 10:
            date_Fig = "-0" + str(date_Fig)
            new_Date += date_Fig
        else:
            date_Fig = "-" + str(date_Fig)
            new_Date += date_Fig
    return new_Date

#sorts the raw data and inputs into seperate textfile
def Sort_Data():
    month_day_regex = r"(\d{,2}/\d{,2} - \d{,2}/\d{,2})"
    new_data = []
    # reading "polling_Data" text file
    with open("polling_Data.txt", "r") as infile:
        for line in infile.readlines():
            line = line.strip()
            if re.match(month_day_regex, line):
                corrected = Convert_Date_Format(line)
                new_data.append(corrected) #do whatever you want

            else:
                new_data.append(line)

    with open("new_polling_data.txt", "w") as outfile:
        for line in new_data:
            outfile.write(line+'\n')









