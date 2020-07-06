# write your code here
bot_name = "Amamek"
birth_year = 2020
print("Hello! My name is {0}.".format(bot_name))
print("I was created in {0}.".format(birth_year))

print("Please, remind me your name.")
user_name = input()
print("What a great name you have, {0}!".format(user_name))

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remaider3 = int(input())
remaider5 = int(input())
remaider7 = int(input())
user_age = (remaider3 * 70 + remaider5 * 21 + remaider7 * 15) % 105
print("Your age is {0}: that's a good time to start programming!".format(user_age))

print("Now I will prove to you that I can count to any number you want.")
number = int(input())
i = 0
while i <= number:
    print(str(i), "!")
    i += 1

print("Let's test your programming knowledge.")

