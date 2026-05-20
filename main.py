from data_module import(
  raw_data
)

def main_menu():
  while true:
    print("------Data Menu------")
    print(" 1. View Raw Dataset")
    print(" 2. Dataset Representation")
    print(" 3. Update Data Entry")
    print(" 4. Exit")
    
    user_choice = input("Select an Option: ")
    if user_choice == "1":
      print(raw_data())
      print("---------Raw Data Menu---------")
      print(" 1. Filter Data")
      print(" 2. Return to Main Menu")
      user_choice2 = input("Choose an Option: ")
      if user_choice2 == "1":
         column_choice = input("Which Catagorie/s Would you Like to Filter By?")
         
      elif user_choice2 == "2":
        print(main_menu())
    elif user_choice == "2":
      print()
    elif user_choice == "3":
      print()
    elif user_choice == "4":
        update_data()

print(main_menu())