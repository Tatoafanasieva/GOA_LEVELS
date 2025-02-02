# 1) შექმენით 2 ცვლადი num1 და num2, მომხმარებელს შემოატენინეთ რიცხვდა შემდეგ მოახდინოთ ყველა ლოგიკური ოპერატორის მაგალიტები.

num1 = 15
num2 = 20
print(num1 < num2)
print(num2 > num1)
print(num2 >= num1)
print(num2 <= num1)
print(num2 == num1)
print(num2 != num1)

# 2) შემოატანინეთ მომხმარებელს ასაკი, და თუ ის არის 8 წლის გამოიტანოს" ბავშვი ხარ ", თუ მისი ასაკი უდრის 14 გამოიტანოს " შენ ხარ თინეიჯერი ".თუ მისი ასაკი უდრის 18 გამოიტანოს " შენ ხარ სრულწლოვანი".

child = int(input("enter your age: "))
teen = int(input("enter your age: "))
adult = int(input("enter your age: "))

if child == 8:
    print("U are cild")
if teen == 14:
    print("u are teen")
if adult == 18:
    print("u are adult")

# 2) გამოთვალე მართკუთხედის პერიმეტრი, შექმენით 2 ცვლადი "width" და "height" და მომხმარებელს შემოატანინეთ სიმაღლე და სიგანე.პერიმეტრის გამოთვლა როგორ ხდება:"width" მიმატებული "height" და გამრავლებული 2 ზე.

width = int(input(" enter width: "))
height = int(input(" enter height: "))
print((width + height) * 2 )

# 3)  შექმენი 2 ცვლადი name და მომხმარებელს შემოატანინეთ სახელი. შემდეგ შექმენით მეორე ცვლადი num და შემოატანინეთ მომხმარებელს რაიმე რიცხვი, შემდეგ name გაამრავლეთ num ზე, და საბოლოოდ დაპრინტეთ შედეგი. 

name = input("enter your name: ")
num = int(input("enter random num: "))
print(name * num)

# 4) გამოთვალეთ მომხმარებლის ასაკი, შექმენი ცვლადი birthyear და მომხმარებელს შემოატანინე დაბადების წელი, შემდეგ შექმენი მეორე ცვლადი date და შემოიტანოს მომხმარებელმა რომელი წელია, შემდეგ date-ს გამოაკელით birthyear, და გაიგებთ მომხმარებლის ასაკს. 

birthyear = int(input("enter your birth year: "))
date = int(input("what year is it now? : "))
print(date - birthyear)

