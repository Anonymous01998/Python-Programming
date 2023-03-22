#NAME - Goutham Selvakumar
#DATE - 02/16/2022
#LINK - "https://www.loom.com/share/7fe46be5238d405da522fd42d1d9eec9"
# "I have not given or recieved any unauthorized assistance on this assignment."

def Palindrome():
    file = open('Palindrome_Dates.txt','w')
    returnedDates = getDates()
    for day in returnedDates:
        file.write(day + '\n')

def getDates():
    palindrome_dates = []
    for year in range (2001, 2101):
        for day in range (1, 29):
            if format_txt(day) == str(year)[2:4][::-1]:
                palindrome_dates.append('{}/{}/{}'.format(format_txt(day),'02',str(year)))
        return palindrome_dates

def format_txt(day):
    if day >= 10:
        return str(day)
    else:
        return str(0) + str(day)

Palindrome()

    
