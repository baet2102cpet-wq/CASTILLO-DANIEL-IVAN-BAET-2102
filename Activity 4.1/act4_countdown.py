#MYRON V. CABALI
#BAET 2102
#COUNTDOWN TIMER

n = int(input("Enter n: "))

while n <= 0:
    n = int(input("Enter n: "))

while n >= 1:
    print(n, end=" ")
    n -= 1

print("Liftoff!")