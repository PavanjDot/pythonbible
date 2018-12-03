class Pound:

    value = 1.00
    colour = "gold"
    num_edges=1
    diameter = 22.5 #mm
    thickness = 3.15#mm
    heads = True


coin1 = Pound()
print(coin1.value)
print(coin1.colour)
coin1.colour = "Greenish"
print(coin1.colour)

coin1.value = 2.25
print(coin1.value)
