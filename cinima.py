films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Buster":[12,5]
    }

while True:
    choice = input("What film would you like to watch?: ").strip().title()

 if choice in films:
     
     age = int(input("How old are you?: ").strip())

    if age>=films[choice][0]:
            print("Enjoy the movie")

    else:
            print("Your too Yong to watch {} ").format(choice)

else:
    print("We dont have that movie")
