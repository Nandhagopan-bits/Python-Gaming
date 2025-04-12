# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    d=input("Name:")
    a=int(input("salary:"))
    b=int(input("Age:"))
    if(a>=20000 or b<=25):
        print("Your eligible for loan ")
        c=int(input('Enter your loan amount:'))
        if(c<=50000):
            print("Your eligible for loan")
            print("yor loan amount accepted")
        else:
            print("The maximum amount is 50000")
    else:
        print("Your not eligible")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
