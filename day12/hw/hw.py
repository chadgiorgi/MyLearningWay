num = int(input("please enter number"))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

num = 24
if num % 2 == 0:
    print("even")
else:
    print("odd")

a = 15
b = 30 
if a > b:
    print("A is bigger ")
elif a < b:
    print("B is bigger ")
else:
    print("equal")

score = 75
if score >= 90:
    print("Excellent")
elif score >= 70 and score <= 89:
    print("Good")
elif score >= 50 and score <= 69:
    print("Avarage")
elif score < 50:
    print("Failed")

a = 12
b = 45 
c = 27

if a > b and a > c:
    print("ყველაზე დიდი რიცხვი არის a =", a)
elif b > a and b > c:
    print("ყველაზე დიდი რიცხვი არის b =", b)
elif c > a and c > b:
    print("ყველაზე დიდი რიცხვი არის c =", c)

price = 400
if price > 300:
    print("30% ფასდაკლება")
    percente = price * 30 / 100
elif price > 200:
    print("20% ფასდაკლება")
    percente = price * 20 / 100
elif price > 100:
    print("10% ფასდაკლება")
    percente = price * 10 / 100 
else:
    print("Regular Price")
print(price - percente)