def start():
    fizzbuzz = []
    number = 0 
    print ("please note if the sequence is lower than 15 then you will not get a complete fizzbuzz sequence")
    freq = input("enter frequency of the fizzbuzz sequence")
    try:
        freq = int(freq)
        for i in range (freq):
            number = number + 1
            if (number % 3 == 0) and (number % 5 == 0):
                print ("FIZZBUZZ")
                fizzbuzz.append("FIZZBUZZ")
            elif number % 3 == 0:
                print ("FIZZ")
                fizzbuzz.append("FIZZ")
            elif number % 5 == 0:
                print ("BUZZ")
                fizzbuzz.append("BUZZ")
            else:
                print (number)
                fizzbuzz.append(number)
        veiw = input ("would you like to veiw the string ver of the seequence? y/n")
        if veiw == "y":
            print ("")
            print (fizzbuzz)
        elif veiw == "n":
            close()
        else:
            print ("incorrect value entered try again!")
            start()
            

            
    except:
        print ("enter a number retard")
        print ("")
        start()
        
    
start()
