# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
input_1 = int(input("Enter first number: "))
operation = input("Enter operator(+)(-)(*)(/)(**): ")
input_2 = int(input("Enter second number: "))


def calculate(input1, input2, operator):
    if operator == "+":
        return input1 + input2
    elif operator == "-":
        return input1 - input2
    elif operator == "*":
        return input1 * input2
    elif operator == "/":
        return input1 / input2
    elif operator == "**":
        return input1 ** input2
    else:
        return "Error"


print(calculate(input_1, input_2, operation))
