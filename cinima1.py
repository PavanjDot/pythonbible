films = {
    "Finding Dory":[3, 5],
    "Bourne":[18, 5],
    "Tarzan":[15, 5],
    "Ghost Buster":[12, 5]
}

while True:
    choice = input("Which film do you want to watch?: ").strip().title()

if choice in films:
    age = int(input("How old are you?: "))
 #check user age
         if age >= films[choice][0]:
            print("Enjoy the movie")

#check seats

                seats = int(input("How many Seats?: ").strip())
                       num_seats=films[choice][1]

                  if num_seats > 0:
                        print("Enjoy the film")
                        films[choice][1]=films[choice][1]-1
                  else:
                     print("Sorry we are sold out ")
                     else:
                             print("Your too Yong to watch {} ").format(choice)

                             else:
                                     print("We dont have that movie")