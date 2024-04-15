print("----------------------------------------------")
# --------------------- compound interest ---------------------

while True:
    principle = float(input("Enter the principle amount\n> "))
    if principle < 0:
        print("Principle can't be less than 0!")
    else:
        break

while True:
    rate = float(input("Enter the interest rate\n> "))
    if rate < 0:
        print("Rate can't be less than 0!")
    else:
        break

while True:
    time = int(input("Enter the time in years\n> "))
    if time < 0:
        print("Time can't be less than 0!")
    else:
        break


total = principle * pow(1 + rate / 100, time)

print(f"Balance after {time} year/s: ${total:.2f}")
