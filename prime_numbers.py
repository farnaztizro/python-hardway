
this_number = 2

while(this_number < 51):
    is_prime_number = True
    counter = 2
    
    while(counter < this_number - 1):
        if(this_number % counter == 0):
            is_prime_number = False
            break
        counter = counter + 1
        
    if(is_prime_number):
        print(this_number)

    
    this_number = this_number+1


