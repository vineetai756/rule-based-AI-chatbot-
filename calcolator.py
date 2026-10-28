# advanced python calculator project
import operator

#dictionary: maps symbols to opration names and function 
operations = {
    "+": ("additon", operator.add),
    "-": ("subtraction", operator.sub),
    "*": ("multiplication",operator.mul),
    "/": ("division", operator.truediv),
    "%": ("moduls", operator.mod),
    "**": ("power", operator.pow)
}

#using tuple :fixed menu options

menu = (
    "calculate",
    "show calculation history",
    "show available oprators",
    "show used oprators",
    "Exit"
)

#List: stores calculation history
history = []

#set : stores unique oprators used
used_operators = set()

#function: performs a calculation 
def calculator(a, symbol, b):
    if symbol not in operations:
        raise ValueError("Invalid operator")

    if symbol in ("/", "%") and b==0:
        raise ZeroDivisionError("cannot divide by zero")

    operation_name, operation_function = operations[symbol]
    result = operation_function(a,b)

    return result

#function : Displays the menu

def show_menu():
    print("\n=====ADVANCED CALCULATOR=====")


    for number , item in enumerate(menu, start=1):
        print(f"{number}. {item}")

# function: display history
def show_history():
    print("\n======CALCULATOR HISTORY======")

    if not history:
        print("no calculation yet.")
        return

    for number , record in enumerate(history, start=1):
        print(f"{number}.{record}")

# function :: runs the application
def main():
    while True:
        show_menu()
        choice = input("enter your choice (1-5):").strip()

        if choice == "1":
            try:
                num1 = float(input("enter first number:"))
                symbol = input(
                    "enter oprator(+,-,*,/,%,**):"
                
                ).strip()

                num2 = float(input("enter second number:"))

                result = calculator(num1, symbol, num2)
                operation_name = operations[symbol][0]

                #strimg; formate the calculatiom neatly
                record= f"{num1:g} {symbol} {num2:g} = {result:g}"

                #list: save calculation 
                history.append(record)

                #set ; save uniue oprator
                used_operators.add(symbol)

                print(f"operation: {operation_name}")
                print(f"result:{result:g}")

            except ValueError as error:
                print("input error:", error)

            except ZeroDivisionError as error:
                print("matherror", error)
        elif choice =="2":
            show_history()

        elif choice=="3":
            print("\nAvailable operators:")
            for symbol, details in operations.items():
                print(f"{symbol} : {details[0]}")

        elif choice =="4":
            print("unique operatore", used_operators)

        elif choice == "5":
            print("thank you for using the calculator!")
            break
        else:
            print("Invalid choice. please enter 1 to 5.")


#prigram entry point
if __name__ == "__main__":
    main()


            


        



                                