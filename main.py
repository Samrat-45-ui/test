my_list = []
def ask_num():
    print("This program will ask you to enter five numbers and multiply them.")
    print(" Let's enter some numbers.")
    for _ in range(5):
        num = input("Enter the a number: ")
        my_list.append(num)
