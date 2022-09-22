import random

# Thank you Sniperkaos for the help in making the program know if the answer's right or not

print("Welcome to ND22's MathA")
print(" ")
print("Possible commands:")
print("!add")
print("!subtract")
print("!multiply")
print("!divide")
print(" ")

while True:

    command = input("Command: ")
    print(" ")

    # Addition

    if command == "!add":
        num1 = (random.randint(1, 9))
        print(" ")
        num2 = (random.randint(1, 9))
        result = float(num1) + float(num2)
        
        print(f"What is {num1} + {num2}?")
        
        answer = input("Answer: ")
        if (not (answer is None)):
            if float(answer) == result:
                print(" ")
                print("Correct!");
            else:
                print(" ")
                print("WRONG!");

    # Subtraction

    if command == "!subtract":
        num1 = (random.randint(1, 9))
        print(" ")
        num2 = (random.randint(1, 9))
        result = float(num1) - float(num2)
        
        print(f"What is {num1} - {num2}?")
        
        answer = input("Answer: ")
        if (not (answer is None)):
            if float(answer) == result:
                print(" ")
                print("Correct!");
            else:
                print(" ")
                print("WRONG!"); 

    # Multiplication

    if command == "!multiply":
        num1 = (random.randint(1, 9))
        print(" ")
        num2 = (random.randint(1, 9))
        result = float(num1) * float(num2)
        
        print(f"What is {num1} * {num2}?")
        
        answer = input("Answer: ")
        if (not (answer is None)):
            if float(answer) == result:
                print(" ")
                print("Correct!");
            else:
                print(" ")
                print("WRONG!");

    # Division

    if command == "!divide":
        num1 = (random.randint(1, 9))
        print(" ")
        num2 = (random.randint(1, 9))
        result = float(num1) / float(num2)
        
        print(f"What is {num1} / {num2}?")
        
        answer = input("Answer: ")
        if (not (answer is None)):
            if float(answer) == result:
                print(" ")
                print("Correct!");
            else:
                print(" ")
                print("WRONG!");
    else:
        print(" ")

