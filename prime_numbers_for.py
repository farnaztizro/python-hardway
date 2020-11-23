for this_number in range(2,51):
    is_prime_number = True

    
    for counter in range(2,this_number):
        if(this_number % counter == 0):
            is_prime_number = False
            break
        
    if(is_prime_number):
        print(this_number)
    
