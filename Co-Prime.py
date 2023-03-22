#NAME: Goutham Selvakumar
#DATE: 01/12/2022
#LINK: "https://www.loom.com/share/58f5468ae40b4a1182dc55872a97e22d"
#"I have not given or recieved any unauthorized assistance on this assignment."

def coprime_test_loop():
    '''Ask the user for two numbers and pass those numbers onto second fucntion coprime(a,b)'''

    while True:
        Firstnum = eval(input("Input first number: "))
        Secondnum = eval(input("Input second number: "))
        if coprime(Firstnum, Secondnum) == 1:
            print('These two numbers are coprime')
        else:
            print('These two numbers are not coprime')
            break
        return coprime_test_loop()

def coprime(a,b):
    while b != 0:
        a, b = b, a%b
        return a 
        
    
