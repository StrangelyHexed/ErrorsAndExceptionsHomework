# Problem 1: Handle the exception thrown by the code below by using try and except blocks.

class Problem1:
    try:
        for i in ['a', 'b', 'c']:
            print(i**2)
    except TypeError:
        print("Unsupported operand types.\n")



#Problem 2: Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

class Problem2:
    try:
        x = 5
        y = 0

        z = x / y

    except ZeroDivisionError:
        print("Division by zero.")

    finally:
        print("All done.\n")




#Problem 3: Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            answer = int(input("Input an integer: "))
        except:
            print("Incorrect input. Please input an integer.")
            continue
        else:
            answer = answer ** 2
            print("Thank you, your number squared is {}.".format(answer))
            break
ask()
