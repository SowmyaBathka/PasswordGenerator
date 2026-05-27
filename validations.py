def validate_length(length):
    if not length.isdigit():
        print("Please enter a valid numeric password length.")
        return False
    
    length = int(length)

    if length<4:
        print("Password length must be atleast 4.")
        return False
    
    return True 

def validate_count(count):
    if not count.isdigit():
        print("Please enter a valid numeric count.")
        return False 
    
    count = int(count)

    if count<=0:
        print("Number of passwords must be greater than zero.")
        return False 
    
    return True 

def validate_yes_no(choice):
    choice=choice.strip().lower()

    if choice not in ["yes","no"]:
        print("Please enter only yes or no.")
        return False 
    
    return True 