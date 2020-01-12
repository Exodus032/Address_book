def write():
    number = input("What is their number?\n:")
    name = input("What is their name\n:")
    desc = input("Description, what do they do / who are they \n:")

    f = open("Addressbook.txt", "a")
    f.write(name + " ")
    f.write(number + " ")
    f.write(desc + " ")
    f.write("\n")
    f.close()
    main()
def everything():
    f = open("Addressbook.txt", "r")
    lines = f.read()
    print(lines)
    f.close()
    main()
def search():
    info = input("Who would you like to search for?\n")
    f = open("Addressbook.txt", "r")
    for line in f.readlines():
        if info in line:
            print("Name, number, description")
            print(line)
    f.close()
    main()
def main():
    main_question = int(input("""
    1. Add a contact
    2. Search for a contact
    3. Look at all contacts \n:
    """))
    if main_question == 1:
        write()
    elif main_question == 2:
        search()
    elif main_question == 3:
        everything()
while True:
    try:
        main()
    except:
        continue
