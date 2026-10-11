# input და output არის ინგლისური სიტყვები და ითარგმნება როგორც "შესავალი" და "გამოსავალი" შესაბამისად პითონშ output ანუ გამოსავალი ფუნქცია არის Print() და შესავალი ანუ input ფუნქცია არის input()

name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
age = input("Please enter your age: ")
height = input("Please enter your height: ")

print(name, surname, age, height)

favorite_car = input("Please enter your favorite car: ")
favorite_color = input("Please enter your favorite color: ")

print("Favorite car:", favorite_car)
print("Favorite color:", favorite_color)

# data converter ანუ მონაცემების კონვერტერი არის შესაძლებლობა რომ გადაიყვანო ერთი მონაცემის ტიპი მეორეში მაგალითად გადავიყვანოთ string ტიპის მონაცემი int ტიპის მონაცემში

int("2011") # აქ მე ჩავწერე string ტიპის მონაცემი რიცხვის სახით და გადავიყვანე int ტიპის მონაცემში ანუ რიცხვში რაც უფლებას გვაძლევს შევასრულოთ მათემატიკური ოპერაციებიმაგალითად 

salery = input("Please enter your salary: ")
salery = int(salery) # აქ მე გადავიყვანე string ტიპის მონაცემი int ტიპის მონაცემში და მას შემიძლია გამოვაკლო ან მივუმატო რიცხვი
taxes = 200

print(salery - taxes) # აქ მე გამოვიტანე ეკრანზე რამდენი რჩება მომხმარებელს ბიუჯეტიდან გადასახადების გადახდის შემდეგ

# ასევე შეგვიძლია გადავიყვანოთ int ტიპის მონაცემი string ტიპის მონაცემში მაგალითად
age = 25
str(age) # ასე ხდება უკვე შექმნილი int ტიპის ცვლადის string ტიპში გადაყვანა რაც საშუალებას გვაძლევს შევაერთოთ ტექსტთან და გამოვიტანოთ ეკრანზე
print("I am " + str(age) + " years old.") # აქ მე გადავიყვანე int ტიპის მონაცემი string ტიპის მონაცემში და შევაერთე ტექსტთან

# ასევე შეგვიძლია პირდაპირ string ტიპის მონაცემი მოვთხოვოთ მომხმარებელს

age = input("Please enter your age: ")
print("I am " + age + " years old.") # აქ მე პირდაპირ მოვთხოვე მომხმარებელს string ტიპის მონაცემი და შევიყვანე ტექსტში რის გამოც აღარ დამჭირდა ტექსტში str() ფუნქციის გამოყენება

# ასევე არსებობს ფუნქცია float() რომელიც არის რიცხვი ათ წილადების სახით მაგალითად 

liter = float(input("Please enter how much liter gas you put in your motorcycle: "))
print("You put " + str(liter) + " liter gas in your motorcycle.") # აქ მე მოვთხოვე მომხმარებელს float ტიპის მონაცემი და შევიყვანე ტექსტში რის გამოც დამჭირდა ტექსტში str() ფუნქციის გამოყენება

# ან შეგვიძლია პირდაპირ float ტიპის მონაცემი შევქმნათ მაგალითად 

weight = float("72.5")
print(weight + 1.5)  # აქ მე შევქმენი ცვლადი რომელიც არის float ტიპის მონაცემი და მას მივუმატე 1.5 რის გამოც ეკრანზე გამოვიდა 74.0 რადგან float ტიპის მონაცემი არის რიცხვი ათ წილადების სახით
# და ბოლოს არის ფუნქცია list() რომელიც არის მონაცემების ტიპი რომელიც შეიცავს მონაცემებს სიაში მაგალითად

favorite_bikes = list(["bmw", "honda", "yamaha"]) # აქ მე შევქმენი list ტიპის ცვლადი რომელიც შეიცავს მონაცემებს სიაში
print("My favorite bikes are: " + str(favorite_bikes)) # აქ მე გამოვიტანე ეკრანზე list ტიპის ცვლადი რმელიც შეიცავს მონაცემებს სიაში რის გამოც დამჭირდა ტექსტში str() ფუნქციის გამოყენება

# ასევე შეგვიძლია პირდაპირ list ტიპის მონაცემი შევქმნათ და გამოვიტანოთ სათითაო ასოებად

numbers = list("hello")
print(numbers)

# ასევე list ფუნქციის გამოყენება შეგვიძლია list ის გარეშე ანუ მარტო [] გამოყენებით მაგალითად
fruits = ["apple", "banana", "cherry"]
print(fruits)

# ასევე არსებობს ფუნქცია type() რომელიც პირდაპირ გვიჩვენებს მონაცემის ტიპს მაგალითად
name = input("Please enter your name: ")
print(type(name)) # აქ მე გამოვიტანე ეკრანზე მომხმარებლის მიერ შეყვანილი მონაცემის ტიპი რომელიც არის string ტიპის რადგან ის ტექსტია და ამას type ფუნქცია გვიჩვენებს

# ასევე შეგვიძლია ეს გამოვიყენოთ უკვე შექმნილ ცვლადზე მაგალითად

age = 25
print(type(age))

# აქ მე გამოვიტანე ეკრანზე უკვე შექმნილი ცვლადის ტიპი რომელიც არის int ტიპის რადგან ის რიცხვია და ამას type ფუნქცია გვიჩვენებს

# ასევე შეგვიძლია ეს გავაკეთოთ string ტიპის მონაცემზე მაგალითად
name = "გიორგი"
print(type(name))

number1 = int(input("Please enter first number: "))
number2 = int(input("Please enter second number: "))
number3 = int(input("Please enter third number: "))

average = (number1 + number2 + number3) / 3
print("The average of the three numbers is:", average)

# ინფორმაციის მოძიებისთვის გამოვიყენე gemini და ავახსნევინე ისე როგორც ბატონმა ლუკამ გვაჩვენა ანუ ვუთხარი რო ისე აეხსნა როგორც ბავშვს აუხსნიდა და გადმოვეცი ჩემი სიტყვებით