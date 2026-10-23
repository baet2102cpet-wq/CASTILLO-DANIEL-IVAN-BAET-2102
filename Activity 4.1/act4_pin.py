#DANIEL IVAN CASTILLO
#BAET 2102
#PIN LOCK

correct_pin = "1234"
tries = 0

while tries < 3:
    pin = input("PIN: ")
    tries += 1

    if pin == correct_pin:
        print("Access granted")
        break
    elif tries == 3:
        print("Card blocked")