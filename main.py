menu = """Please select one of the following options:
1) Add a new entry
2) View your diary
3) Exit

Please choose 1, 2, or 3: """
welcome = "welcome! i'm happy to see you :)"

print(welcome)
user_input = input(menu)
while user_input != "3":
    if user_input == "1":
        print("Adding...")
    elif user_input == "2":
        print("Viewing...")
    else:
        print("invalid :'( try again")
    user_input = input(menu)

