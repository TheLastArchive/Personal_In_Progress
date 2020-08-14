
def check_email(email):

    f = open("data.txt", 'r')
    storage = f.read()
    f.close()
    if email in storage.strip():
        return True
        
    return False

def check_password(email, password):

    f = open("data.txt", 'r')
    storage = f.readlines()
    for num, line in enumerate(storage, 0):
        if (email + '\n') in line:
            if storage[num + 1] == password + '\n':
                return True
        else:
            num += 1
    f.close()
    return False

def save_data(email, password):

    f = open("data.txt" , 'a')
    f.write(email + '\n' + password + '\n')
    f.close()
    print("Account has been created!")

def login():

    email = input("Please enter your email address: ")
    
    while(check_email(email) == False):
        print("Incorrect email, please try again.")
        email = input("Please enter your email address: ")

    password = input("Please enter your password: ")
    while (check_password(email, password) == False):
        print("Incorrect password, please try again.")
        password = input("Please enter your password: ")
    print("Login in successful.")

def new_user():

    email = input("Please enter your email address: ")
    while(check_email(email) == True):
        print("This email address has already been registered.")
        ans = input("Press enter to try again or 'l' to login: ")
        if ans == 'l':
            login()
            return
        email = input("Please enter your email address: ")
    
    password = input("Please enter your password: ")
    while check_password(email, password) == True:
        print("This password has already been taken.")
        password = input("Please try another: ")

    save_data(email, password)

if __name__ == "__main__":

    ans = input("Welcome! Would you like to login(l) or create an account(c)?: ")
    if ans.lower() == "l":
        login()
    elif ans.lower() == "c":
        new_user()
    else:
        print("Invalid input")