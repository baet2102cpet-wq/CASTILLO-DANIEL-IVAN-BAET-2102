#DANIEL IVAN CASTILLO
#BAET 2102
#RUNNING TOTAL

total = 0
count = 0

price = float(input("Price (0 to stop): "))

while price != 0:
    total += price
    count += 1
    price = float(input("Price (0 to stop): "))

print(f"Items: {count}  Total: {total:.2f}")

if count > 0:
    average = total / count
    print(f"Average: {average:.2f}")
else:
    print("Average: 0.00")