name = input("Enter your name: ")
health = 100
location = "home"

health-= 20 # player loses health
print(f"{name}, your health is now {health}.")

def show_status(name, health, location):
    print(f"{name}, you have {health} and in your location.")

show_status(name, health, location)

while True:
    choice = input("You have a flu. Are you going to school (y) or not (n)? ")
    if choice == 'y':
        health -= 50
        print("You chose to go to school.")
        break
    elif choice == 'n':
        print("You chose to stay at home.") 
        break
    else:
        print("Wrong choice!")

show_status(name, health, location)

choice = input("Your mother wants you to rest and drink medicine, but you want to play Mobile Legends. Are you going to obey her (y) or play all night 👎? ")
if choice == 'y':
    health += 10
    print("You chose to obey her.")
elif choice == 'n':
    health -= 10
    print("You chose to play and disobey her.")
else:
    print("Wrong choice!")
show_status(name, health, location)

choice = input("Your friends invite you out for a walk to get fresh air. Do you want to go with them (y) or stay home (n)? ")
if choice == 'y':
    health += 10
    print("You chose to go out with your friends.")
elif choice == 'n':
    health -= 15
    print("You chose to stay at home.")
else:
    print("Wrong choice!")
show_status(name, health, location)

while health >= 0:
    choice = input("Do you want to play again? Yes (y) or No (n)? : ").lower()
    if choice == 'y':
        health -= 100
        print(f"{name}, you need to rest, and your health is now {health}.You need to be confine.")
        break
    else:
        health +=5
        print(f"{name}, you are now okay, and your health is now {health}.") 
    


