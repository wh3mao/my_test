print("math test")
print("you are ready?")
x = "yes"
y = "no"
question_1 = "200"
question_2 = "6"
question_3_1 = "no"
question_3_2 = "yes"
question_4 = "3.14"
question_5 = "naruto"
user_input = input().lower()
if user_input == x:

    print("Question 1")
    print("100 + 100")
    user_input = input().lower()
    if user_input == question_1 :
        print("True")
    else:
        print("False")
    if user_input == question_2:
        print("Question 2")
    print("2 + 2 * 2")
    user_input = input().lower()
    if user_input == question_2:
        print("True")
    else:
        print("False")
if user_input == question_2:
    print("Question 3")
    print("Is it true that √2∈Q2∈Q")
    user_input = input().lower()
    if user_input == question_3_1:
        print("True")
    elif user_input == question_3_2:
        print("False")
    elif user_input == question_5:
        print("False")
        if user_input == question_5:
         print("Question 4")
    print("What is pure π ?")
    user_input = input().replace(",", ".")
    if user_input == question_4:
        print("True")
    else:
        print("False")
        print("Question 5")
        print("Who was the 7th Hokage in Naruto anime?")
        user_input = input().lower()
        if user_input == question_5:
            print("True")
        else:
            print("False")
elif user_input == y:
    print("bue")
else:
    print("Wrong answer")