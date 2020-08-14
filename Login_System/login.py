
def check_email(email):

    x = False

    f = open("data.txt", 'r')
    storage = f.readlines()
    f.close()

    if email in storage:
        x = True
    
    return x

#def check_password(email, password):

def save_data(email, password):

    f = open("data.txt" , 'a')
    f.write(email + " / " + password)
    f.close()
    print("Account has been created!")


def login():

    email = input("Please enter your email: ")
    x = False
    while x == False:
        if check_email(email) == True:
            x = True
            y = False
            print("Please enter your password")
            password = input
            while y == False:
                if check_password(email, password) == True:
                    y = True
                    return "Login successful!"
                else:
                    print("Incorrect password, please try again.")
        else:
            print("This email does not exist")
            print("Would you like to try again(y), create an account(c), or exit(e)?")
            if input.lower() == "c":
                new_user()
                break
            elif input.lower() == "e":
                print("Goodbye!")
                break
            elif input.lower() == "y":
                pass
            else:
                print("Invalid input")

def new_user():

    print("Please enter your email: ")
    email = input()
    if check_email(email) == False:
        x = False
        while x == False:
            print("Please enter a password: ")
            password = input()
            print("Please confirm your password: ")
            confirm_pass = input()
            if password == confirm_pass:
                x = True
                save_data(email, password)
            else:
                print("These passwords do not match, please try again")
    else:
        print("This email has already been taken, would you like to log in? (y/n): ")
        if input.lower() == "y":
            login()
            pass
        elif input.lower() == "n":
            pass
        else:
            print("Invalid input")


if __name__ == "__main__":

    ans = input("Welcome! Would you like to login(l) or create an account(c)?: ")
    if ans.lower() == "l":
        login()
    elif ans.lower() == "c":
        new_user()
    else:
        print("Invalid input")