# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a=int(input("A:"))
    b=int(input("B:"))
    operation=input("Add/Sub/Mul/Divi:")
    if(operation=="Add"):
        print(a+b)
    elif(operation=="Sub"):
        print(a-b)
    elif(operation=="Mul"):
        print(a*b)
    elif(operation=="Divi"):
        print(a/b)
    else:
        print("Invailed format")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
