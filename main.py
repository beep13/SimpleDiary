from database import add_entry, get_entries

menu = """Please select one of the following options:
1) Add a new entry
2) View your diary
3) Exit

Please choose 1, 2, or 3: """
welcome = "welcome! i'm happy to see you :)"


def prompt_new_entry():
    entry_date = input("what's the date? ")
    entry_content = input("tell me what's goin' on: ")

    add_entry(entry_date, entry_content)


def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


print(welcome)

user_input = input(menu)

while user_input != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("invalid :'( try again")
    user_input = input(menu)

