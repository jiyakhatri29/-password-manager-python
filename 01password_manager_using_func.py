#we'll create a function to store the password if no password was entered previously.
def save_password():
    web=input("Enter your website name : ")
    user=input("Enter your user name : ")
    password=input("Enter your password : ")
    
    with open("password.txt", "a") as f:
        f.write(f"{web} | {user} | {password} \n")
        
    print("Password Saved!")   
    
    
def view_password():
    try:
        with open("password.txt", "r") as f:
            print("\n Saved Passwords: \n")
            for line in f:
                print(f"{line.strip()}")
    except FileNotFoundError:
        print("No password entered: ")
               
               
while True:
    Message = input("Do you wanted to view/add password write '1' for view '2' for add or 'Q' to quit: ")
    if Message =='1':
        view_password()
    elif Message =='2':
        save_password() 
    elif Message=="Q":
        print("Good Bye!!") 
        break
    else:
        print("Enter correct choice!!")          