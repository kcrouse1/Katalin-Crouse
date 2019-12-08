def question1():
    ''' Asks Question #1 of the quiz
    '''
    stop = False 
    while stop == False :
        inputStr = input("Do you greet your roommate when you see them?").lower()
        if(inputStr == "a"):
            stop = True 
        elif(inputStr == "b"):
            stop = True
        else: 
            stop = False
            print("\nTry again")
    return inputStr

def question2():
    ''' Asks Question #2 of the quiz
    '''
    stop = False 
    while stop == False :
        inputStr = input("Do you take out the trash when its full?").lower()
        if(inputStr == "a"):
            stop = True
        elif(inputStr == "b"):
            stop = True
        else : 
            stop = False
            print("\nTry again")
    return inputStr

def question3():
    ''' Asks Question #3 of the quiz
    '''
    stop = False 
    while stop == False :
        inputStr = input("Do you ask if you use their things?").lower()
        if(inputStr == "a"):
            stop = True
        elif(inputStr == "b"):
            stop = True
        elif(inputStr != "a" or "b"): 
            stop = False
            print("\nTry again")
    return inputStr

def question4():
    ''' Asks Question #4 of the quiz
    '''
    stop = False 
    while stop == False :
        inputStr = input("Do you clean up the kitchen after you cook?").lower()
        if(inputStr == "a"):
            stop = True
        elif(inputStr == "b"):
            stop = True
        else : 
            stop = False
            print("\nTry again")
    return inputStr

def question5():
    ''' Asks Question #5 of the quiz
    '''
    stop = False 
    while stop == False :
        inputStr = input("Do you wash your dishes?").lower()
        if(inputStr == "a"):
            stop = True
        elif(inputStr == "b"):
            stop = True
        else: 
            stop = False
            print("\nTry again")
    return inputStr

def question6():
    ''' Asks Question #6 of the quiz
    '''
    stop = False 
    while stop == False :
        inputStr = input("Do you make sure to not leave a mess in the bathroom?").lower()
        if(inputStr == "a"):
            stop = True
        elif(inputStr == "b"):
            stop = True
        else : 
            stop = False
            print("\nTry again")
    return inputStr

def question7():
    ''' Asks Question #7 of the quiz
    '''
    stop = False 
    while stop == False :
        inputStr = input("Do you spill the tea with your roommates?").lower()
        if(inputStr == "a"):
            stop = True
        elif(inputStr == "b"):
            stop = True
        else: 
            stop = False
            print("\nTry again")
    return inputStr

def question8():
    ''' Asks Question #8 of the quiz
    '''
    stop = False 
    while stop == False :
        inputStr = input("Do you give them credit for their work?").lower()
        if(inputStr == "a"):
            stop = True
        elif(inputStr == "b"):
            stop = True
        else :
            stop = False
            print("\nTry again")
    return inputStr