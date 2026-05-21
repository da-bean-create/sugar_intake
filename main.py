from data_module import (
  raw_data,
  search_data,
  show_full_dataset,
  add_data_entry,
  save_data_entry,
  delete_data,
  dataset_representation,
  view_visualisation,
  view_visualisation2
)

def main_menu():
  while True:
    print("=====================")
    print("------Main Menu------")
    print("=====================")
    print(" 1. View Raw Dataset")
    print(" 2. Dataset Representation")
    print(" 3. Add/Delete Data Entry")
    print(" 4. Exit")
    print("=====================")
    print("                     ")
    
    user_choice = input("Select an Option: ")
    if user_choice == "1":
      print(raw_data)
      print("===============================")
      print("---------Raw Data Menu---------")
      print("===============================")
      print(" 1. Filter Data")
      print(" 2. Show Full Dataset")
      print(" 3. Return to Main Menu")
      print("================================")
      print("                                ")
      
      user_choice2 = input("Choose an Option: ")
      if user_choice2 == "1":
         search_data(raw_data)
      elif user_choice2 == "2":
         show_full_dataset(raw_data)
      elif user_choice2 == "3":
        continue
      else:
        print("Invalid selection. Returning to Main Menu...")
        continue
    
    elif user_choice == "2":
      print("===============================")
      print("------Dataset Representation------")
      print("===============================")
      print(" 1. Distribution of Sugary Snacks Per Day")
      print(" 2. Comparison of Daily Sugar Consumption and Thoughts on OBESITY")
      print(" 3. Return to Main Menu")
      print("=================================")
      png = input("Which visualisation would you like to view? ").lower()
      if png == "1":
        view_visualisation()
      elif png == "2":
        view_visualisation2()
      else:
        print("Invalid selection.")
        print("Returning to Main Menu...")
        continue
    elif user_choice == "3":
     password = input("Enter Password to Access Add/Delete Data Entry: ")
     if password != "THEbestAssignment3ver":
      print("Incorrect Password. Returning to Main Menu...")
      continue
     else: 
      print("===============================")
      print("---Add/Delete Data Entry---")
      print("===============================")
      print(" 1. Add New Entry")
      print(" 2. Delete Existing Entry")
      print(" 3. Return to Main Menu")
      print("===============================")
      print("                                ")

      user_choice3 = input("Choose an Option: ")
      if user_choice3 == "1":
        entry = add_data_entry()
        save_data_entry(entry)
      elif user_choice3 == "2":
        delete_data()
      else:
        print("Returning to the Main Menu...")
        continue
    elif user_choice == "4":
      print("Exiting Program...")
      break
    else:
      answer = input("Invalid Selection. Would You Like to Return to the Main Menu?(yes/no) ").lower()
      if answer == "yes":
        continue
      else:
        print("Exiting Program...")
        break

main_menu()