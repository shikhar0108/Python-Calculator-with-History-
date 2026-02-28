history_file = "history.txt"


# show history
def show_history():
    try:
        with open(history_file, "r") as file:
            lines = file.readlines()

            if len(lines) == 0:
                print("History is empty\n")
            else:
                for line in lines:
                    print(line.strip())

    except FileNotFoundError:
        print("No history found\n")


# clear history
def clear_history():
    with open(history_file, "w"):
        pass
    print("History cleared\n")


# save history
def save_to_history(equation, result):
    with open(history_file, "a") as file:
        file.write(equation + " = " + str(result) + "\n")


# calculation
def calculate(user_input):

    try:
        result = eval(user_input)

        if result == int(result):
            result = int(result)

        print(result)

        save_to_history(user_input, result)

    except ZeroDivisionError:
        print("Cannot divide by zero\n")

    except:
        print("Invalid expression\n")


# main program
def main():

    while True:

        user_input = input(
            "\n--- CALCULATOR ---\n"
            "Commands: history | clear history | exit\n"
            "Enter expression: "
        )

        if user_input == "history":
            show_history()

        elif user_input == "clear history":
            clear_history()

        elif user_input == "exit":
            print("Goodbye")
            break

        else:
            calculate(user_input)


main()