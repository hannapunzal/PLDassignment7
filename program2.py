# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid

import time

def passwordRequirements(): # TO CHECK IF THE REQUIREMENTS ARE MET
    global askPassword
    print("Password requirements: \n     at least 15 characters\n     at least one (1) uppercase letter\n     at least one (1) number\n     at least one (1) special character")
    time.sleep(3)
    askPassword = input("Enter password: ")
    characters = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ".", "|", ";", ":", "'", "?", ",", "/", "<", ">", "~", "`")
    val = True
    if len(askPassword) < 15:
        val = False
    if not any(char.isupper() for char in askPassword):
        val = False   
    if not any(char.isdigit() for char in askPassword):
        val = False
    if not any(char in characters for char in askPassword):
        val = False
    return val

def passwordValidator(): # WITH CONFIRMATION FOR HIGHER ACCURACY AND SAFETY
    if (passwordRequirements()):
        confirmation = input("The password you entered is valid.\nPlease enter the password again for confirmation: ")
        if confirmation == askPassword:
            print("Program finished. Thank you!")
        else:
            reconfirmation = input("The password you entered did not match with the first password.\nPlease retry: ")
            if reconfirmation == askPassword:
                print("The passwords matched. Thank you for using this program!")
            else:
                print("The passwords did not match. Please try again later after closing this program.")
    else:
        print("The password you entered is invalid. Please restart the program if you wish to continue.")
      
passwordValidator()