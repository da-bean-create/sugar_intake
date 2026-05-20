import pandas as pd

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
print(raw_data())

def search_data():
    filtered_df = df.copy()

    while True:
        print("\nAvailable columns:")
        print(df.columns.tolist())

        column = input("Enter column to search: ")

        if column not in df.columns:
            print("Invalid column name.")
            continue

        value = input("Enter value to search in '{column}':")
        filtered_df = filtered_df[
            filtered_df[column]
            .astype(str)
            .str.contains(value, case=False, na=False)
        ]

        again = input("Add another filter? (yes/no): ").lower()

        if again != "yes":
            break

    print("Filtered Results:")
    print(filtered_df)