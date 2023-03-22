#Goutham Selvakumar
#01/12/2022
#"https://www.loom.com/share/851c8dc031354dd79acfc7195fd2cc83"
#"I have not given or received any unauthorized assistance on this assignment"


def correctFile():
    '''Ask the user if the student submitted it as a single uncompressed .py file'''
    ans = eval(input("If the student submitted it as a single uncompressed .py file?(True/False)"))
    return ans

def includesnamedate():
    '''Ask the user if the student include the author's name and date'''
    ans = eval(input("If the student includes the author's name and date?(True/False)"))
    return ans

def includesHonorStatement():
    '''Ask the user if the student include the honor statement'''
    ans = eval(input("If the student includes the honor statement?(True/False)"))
    return ans

def includesLink():
    '''Ask the user if the student include a link to an unlisted 3-minute Youtube video'''
    ans = eval(input("If the student includes a link to an unlisted 3-minute Youtube video?(True/False)"))
    return ans

def meetSpecification():
    '''Ask the user how well the code meets the given specifications'''
    ans = eval(input("Out of ten points, how would you evaluate the correctness of the code?"))
    return ans

def codeElegance():
    '''Ask the user how well is the elegance of the code (data structure selection, algorithm efficiency, function implementation, etc.)'''
    ans = eval(input("Out of ten points, how would you evaluate the elegance of the code?"))
    return ans

def codeHygiene():
    '''Ask the user how well of the code hygiene (white space, docstrings, etc)'''
    ans = eval(input("Out of ten points, how would you evaluate the code hygiene?"))
    return ans

def videoQuality():
    '''Ask the user how well the quality of the discussion in the Youtube video'''
    ans = eval(input("Out of ten points, how would you evaluate the video quality?"))
    return ans

def lateAssignment():
    '''Ask the user if the student submitted assignment late'''
    ans = eval(input("Did the student submit the assignment late?(True/False)?"))
    return ans

def lateHours():
    '''Ask the user late submission by how many house'''
    hours = eval(input("How many hours late?"))
    return hours

def computeGrade():
    '''Compute the grade following each questions'''
    if not( correctFile() ): #use a helper function
        return 0 #if the file was incorrect, retun 0

    if not( includesnamedate() ): #use a helper function
        return 0 #no name, return 0

    if not( includesHonorStatement() ): #use a helper function
        return 0 #no honor statement, return 0

    if not( includesLink() ): #use a helper function
        return 0 #no link, return 0

    data1 = meetSpecification(); data2 = codeElegance(); data3 = codeHygiene(); data4 = videoQuality()

    res = data1 + data2 + data3 + data4

    if not( lateAssignment() ): #use a helper function
        return res #submitted not late, return full score
    else:
        hours = lateHours()
        return res * (1-(hours)*0.01) #late assignments lose 1% per hour

    


    
