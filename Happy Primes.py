#NAME: GOUTHAM SELVAKUMAR
#DATE: 01/25/2022
#LINK: "https://www.loom.com/share/46171bd693f241da933eb8142b718b58"
#"I HAVE NOT GIVEN OR RECIEVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMNENT"

def get_num():
    '''Let the user enter a positive integer value'''
    n = int(input("Please enter a positive integer:"))
    return n

def get_sum(number):
    '''Get the sum of squares of the number's digits'''
    sum_digits = 0
    for i in number:
        sum_digits += (int(i)) ** 2
    return sum_digits

def check_happy(number):
    '''Check if the number is happy'''

    #if the number is 1 return happy
    if number == 1:
        return True
    #a list is done for checked happy and sad number
    checked_numbers = [number]
    number_list=list(str(number))

    #run the loop until the number is 1
    while number!= 1:
        number = get_sum(number_list)  #sum of square's of the number's digits
        if number in checked_numbers:
            return False
        checked_numbers.append(number)
        number_list = list(str(number))

    return True

def check_prime(number):
    '''Check if the number is Pirme'''
    #number 1 is not a prime
    if number == 1:
        return False
    for i in range(2, number):
        if number%i == 0:
            return False
        return True

def printnumber(isHappy,isPrime):
    if isHappy:
        #check the number whether prime or non-prime
        if isPrime:
            print('Happy Prime')
        else:
            print('Happy Non-Prime')
    else:  #continues the loop for the sad prime or sad non-prime
         if isPrime:
             print('Sad Prime')
         else:
             print('Sad Non-Prime')

def main():
    n = get_num()
    res1 = check_happy(n) ; res2 = check_prime(n)
    printnumber(res1,res2)
    
            
