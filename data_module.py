import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

raw_data = pd.DataFrame([
                        [1, "2", "", "ice cream", "Moderate Decrease", "censored", "ban obesity", ""],
                        [2, "7+", "50g+", "pizza", "Large Increase", "good", "no thoughts", ""],
                        [3, "0-1", "10-19g", "sweet potato, dark chocolate, fruit, scones", "No Change", "bad", "exercise", ""],
                        [4, "5-6", "", "soft drink, ice cream, lollies, chocolate, chips", "Moderate Increase", "preventable", "diet", ""],
                        [5, "3-4", "", "chocolate, sweets, hot chocolate, chips, french fry", "No Change", "no thoughts", "diet", ""],
                        [6, "2", "", "fruit, sugar", "Small Decrease", "Bad", "excercise", ""],
                        [7, "3-4", "", "chocolate, chocolate milk", "No Change", "bad.", "diet", ""],
                        [8, "3-4", "45-49g", "chocolate, lollies, chips, cake", "No Change", "bad.", "diet", ""],
                        [9, "3-4", "10-19g", "chocolate", "No Change", "bad", "ban obesity", ""],
                        [10, "3-4", "45-49g", "chocolate, cake, bread, doughnuts, Lollies", "No Change", "bad", "diet", ""],
                        [11, "3-4", "40-49g", "cookie, dairy, chocolate milk, muffin", "No Change", "no thoughts", "diet", "Australian"],
                        [12, "7+", "50g+", "chocolate, sugar, soft drink, dairy, lollies", "Small Increase", "bad", "ban obesity", ""],
                        [13, "3-4", "50g+", "soft drink, chocolate, ice cream", "Moderate Increase", "bad", "diet", "Middle Eastern"],
                        [14, "2", "20-29g", "muffin, chips, fruit", "Small Increase", "Bad", "diet", "Australian"],
                        [15, "7+", "50g+", "chocolate, chips, lollies", "No Change", "bad", "diet", "Australian"],
                        [16, "5-6", "50g+", "soft drink, ice cream, chocolate", "Large Increase", "bad", "diet", "Australian"],
                        [17, "3-4", "10-19g", "ice cream, soft drink, pancakes, chocolate", "Moderate Decrease", "bad", "diet", "Australian"],
                        [18, "7+", "50g+", "censored", "Large Increase", "censored", "ban obesity", "South African"],
                        [19, "7+", "50g+", "censored", "Large Increase", "censored", "ban obesity", "Asian"],
                        [20, "3-4", "0-9g", "chocolate, ice cream, lollies, wafer", "Small Decrease", "bad", "diet", "Australian"],
                        [21, "5-6", "30-39g", "fruit, chocolate, biscuits", "Moderate Increase", "preventable", "diet", "Asian"],
                        [22, "2", "20-29g", "honey, fruit, chocolate, alcohol", "Small Decrease", "bad", "diet", "Australian"],
                        [23, "3-4", "30-39g", "chocolate, bread, lollies", "No Change", "bad", "excercise", "Asian"],
                        [24, "2", "20-29g", "lollies, cookie, chocolate", "No Change", "preventable", "excercise", "Asian"],
                        [25, "0-1", "10-19g", "fruit, dairy, bread", "Moderate Decrease", "no thoughts", "diet", "Asian"],
                        [26, "2", "20-29g", "soft drink, sugar, ice cream, biscuit, chips", "Small Decrease", "bad", "diet", "Asian"],
                        [27, "0-1", "20-29g", "lollies, chocolate milk", "Small Decrease", "bad", "diet", "Asian"],
                        [28, "0-1", "0-9g", "cereal, muffin, yoghurt and biscuits", "Small Increase", "bad", "diet", "Asian"],
                        [29, "0-1", "30-39g", "lollies, chocolate", "Small Increase", "bad", "no thoughts", "Australian"],
                        [30, "3-4", "40-49g", "soft drink, chocolate, lollies, hot chocolate", "No Change", "preventable", "diet", "Asian"],
                        [31, "3-4", "30-39g", "cookie, fruit, dark chocolate, honey", "Small Decrease", "bad", "diet", "Australian"],
                        [32, "2", "10-19g", "fruit, lollies, ice cream, biscuits, soft drink", "No Change", "bad", "diet", "Asian"],
                        [33, "2", "20-29g", "chips, jam, pizza, juice, fruits", "Small Decrease", "Not good D:", "diet", "Australian"],
                        [34, "2", "20-29g", "chocolate, cookies, ice cream", "Small Decrease", "bad", "diet", "Australian"],
                        [35, "3-4", "20-29g", "fruit, lollies, fast food", "No Change", "parents fault", "awareness", "Australian"],
                        [36, "2", "30-39g", "cookies, chocolate, lollies, juice, cereal", "Moderate Decrease", "no thoughts", "diet", "Australian"],
                        [37, "2", "10-19g", "soft drink, chocolate, candy, lollies, apple pie", "No Change", "parents fault", "diet", "Australian"],
                        [38, "0-1", "0-9g", "sugar", "Moderate Decrease", "bad", "diet", "Asian"],
                        [39, "2", "20-29g", "chocolate, fruits, crépes", "Small Increase", "addiction", "exercise", "Australian"],
                        [40, "3-4", "40-49g", "lollies, chocolate, bread, chips, cookies", "No Change", "bad", "exercise", "Asian"],
                        [41, "3-4", "30-39g", "cookie, chips, fruit, fast food, ice cream", "Moderate Increase", "bad", "diet", "Asian"],
                        [42, "5-6", "50g+", "fruit, lollies, chocolate", "Moderate Decrease", "bad", "diet", "Asian"],
                        [43, "5-6", "50g+", "chocolate, lollies, gum", "No Change", "bad", "diet", "Australian"],
                        [44, "3-4", "20-29g", "cookies, brownies, cakes, ice cream, cookies", "Small Increase", "bad", "diet", "Middle Eastern"],
                        [45, "3-4", "30-39g", "soft drink, lollies, biscuits", "Small Decrease", "bad", "awareness", "European"]
                        ],
                        columns = ["ID", "No Of Sugary Snacks Per Day", "Daily Sugar Consumption", "Commonly Eaten Treats", "Sugar Consumption Compared to Last Year", "Thoughts on OBESITY", "OBESITY Prevention Methods", "Ethnicity"]
                        )


def search_data(raw_data):
    filtered_df = raw_data.copy()
    columns_map = {col.lower(): col for col in raw_data.columns}

    while True:
        print("Available columns:")
        print(raw_data.columns.tolist())

        column_input = input("Enter column to search: ").strip().lower()
        if column_input not in columns_map:
            print("Invalid column name.")
            continue

        column = columns_map[column_input]
        value = input(f"Enter value to search in '{column}': ").strip()

        filtered_df = filtered_df[
            filtered_df[column]
            .astype(str)
            .str.contains(value, case=False, na=False)
        ]

        again = input("Add another filter? (yes/no): ").strip().lower()

        if again != "yes":
            break

    print("Filtered Results:")
    print(filtered_df)


def show_full_dataset(dataframe):
    print("Full Dataset:")
    print(dataframe.to_string(index=False))


def add_data_entry():
    global raw_data

    print("=== Add New Data Entry ===")

    new_entry = {}

    for column in raw_data.columns:
        if column == "ID":
            new_entry[column] = len(raw_data) + 1
            continue

        value = input(f"Enter value for '{column}': ").strip()
        new_entry[column] = value

    print("New Entry Preview:")
    print(new_entry)
    return new_entry

def save_data_entry(new_entry):
    save_answer = input("Would you like to save this entry? (yes/no): ").strip().lower()
    if save_answer == "yes":
        raw_data.loc[len(raw_data)] = [new_entry[col] for col in raw_data.columns]
        print("Entry saved successfully.")
    else:
        print("Entry discarded.")

def delete_data():
    global raw_data

    print("=== Delete Data Entry ===")

    delete_id = input("Enter the ID of the entry to delete: ")

    matching_rows = raw_data[raw_data["ID"].astype(str) == delete_id]

    if matching_rows.empty:
        print("No entry found with that ID.")
        return
    print("Entry Found:")
    print(matching_rows)

    confirm = input("Are you sure you want to delete this entry? (yes/no): ").lower()

    if confirm == "yes":
        raw_data = raw_data[raw_data["ID"].astype(str) != delete_id]

        # Reset dataframe index
        raw_data.reset_index(drop=True, inplace=True)

        print("Entry deleted successfully.")

    else:
        print("Deletion cancelled.")


def _display_or_save_plot(filename):
    try:
        plt.tight_layout()
        plt.savefig(filename, dpi=150)
        path = os.path.abspath(filename)
        print(f"Saved plot to: {path}")
        print("Open this file in VS Code or your file manager to view the image.")
    except Exception as e:
        print(f"Failed to save plot: {e}")
    finally:
        plt.close()


def dataset_representation(raw_data):
    while True:
        print("=== Dataset Representation ===")
        print("1. View Summary Statistics")
        print("2. View Data Distribution")
        print("3. Return to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            print(raw_data.describe(include='all'))
        elif choice == "2":
            raw_data['No Of Sugary Snacks Per Day'].value_counts().plot(kind='bar')
            plt.title('Distribution of No Of Sugary Snacks Per Day')
            plt.xlabel('No Of Sugary Snacks Per Day')
            plt.ylabel('Frequency')
            _display_or_save_plot('dataset_distribution.png')
        else:
            print("Returning to Main Menu...")


def view_visualisation():

    ethnicity_counts = raw_data["Ethnicity"].value_counts()

    plt.bar(
        ethnicity_counts.index,
        ethnicity_counts.values
    )

    plt.title("Ethnicity Counts")
    plt.xlabel("Ethnicity")
    plt.ylabel("Count")

    _display_or_save_plot('visualisation1.png')

def view_visualisation2():

    pivot = raw_data.groupby(["Daily Sugar Consumption", "Thoughts on OBESITY"]).size().unstack(fill_value=0)
    pivot.plot(kind='bar', stacked=True)

    plt.title("Daily Sugar Consumption vs Thoughts on OBESITY")
    plt.xlabel("Daily Sugar Consumption")
    plt.ylabel("Number of Responses")

    _display_or_save_plot('visualisation2.png')