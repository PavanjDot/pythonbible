known_users = ["Pavan", "Nikita", "Akshata", "Sumanth", "Dinesh"]



while True:
    print("Hi! My name is Travis")
    name = input("What's You'r Name:  ").strip().capitalize()
    if name in known_user:
        print("Hello {}!".format(name))
        remove = input("would you like to Remove from the system (y/n)?: ").lower()

        if remove = "y":
            known_user.remove(name)
            print(know_user)
    else:
         print("Hmm i don't think ")
