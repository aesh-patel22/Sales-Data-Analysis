import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------
#   MAIN MENU FUNCTION
# -------------------------------
def main_menu():
    print("\n" + "="*50)
    print("       SALES DATA ANALYSIS PROGRAM")
    print("="*50)
    print("1.  Read complete csv file")
    print("2.  Read complete file without index")
    print("------------------------------------------------")
    print("          Data Visualization")
    print("3.  Line Chart")
    print("4.  Bar Plot")
    print("5.  Pie Chart")
    print("6.  Scatter Chart")
    print("------------------------------------------------")
    print("       Data Manipulation")
    print("7.  Sorting the data")
    print("8.  Read Top and Bottom Records")
    print("9.  Make a copy of CSV file")
    print("10. Add New City Record")
    print("11. Search Records by City Name")
    print("------------------------------------------------")
    print("       DataFrame Statistics")
    print("12. Count")
    print("13. Sum")
    print("14. Mean")
    print("15. Max")
    print("16. Min")
    print("17. Median")
    print("------------------------------------------------")
    print("0.  Exit the program")
    print("="*50)


# -------------------------------
#   READING FUNCTIONS
# -------------------------------
def read_csv_complete():
    try:
        df = pd.read_csv("sales.csv")
        print("\nComplete CSV Data:")
        print(df)
    except FileNotFoundError:
        print("Error: sales.csv file not found!")


def read_without_index():
    try:
        df = pd.read_csv("sales.csv", index_col=0)
        print("\nCSV Data without default index:")
        print(df)
    except FileNotFoundError:
        print("Error: sales.csv file not found!")


# -------------------------------
#   VISUALIZATION FUNCTIONS
# -------------------------------
def get_data():
    try:
        df = pd.read_csv("sales.csv")
        return df
    except FileNotFoundError:
        print("Error: sales.csv file not found!")
        return None


def line_plot():
    df = get_data()
    if df is None:
        return

    cities = df['Cities']
    profit = df['Profit']
    margin = df['Margin']
    sales = df['Sales']
    cogs = df['COGS']

    plt.figure(figsize=(10, 6))
    plt.xticks(rotation=45)
    plt.xlabel("Cities")

    print("\nLine Chart Options:")
    print("1. Cities vs Profit")
    print("2. Cities vs Margin")
    print("3. Cities vs Sales")
    print("4. Cities vs COGS")
    print("5. All in one chart")
    choice = int(input("Enter choice (1-5): "))

    if choice == 1:
        plt.plot(cities, profit, marker='o')
        plt.ylabel("Profit")
        plt.title("Cities vs Profit")
    elif choice == 2:
        plt.plot(cities, margin, marker='o')
        plt.ylabel("Margin")
        plt.title("Cities vs Margin")
    elif choice == 3:
        plt.plot(cities, sales, marker='o')
        plt.ylabel("Sales")
        plt.title("Cities vs Sales")
    elif choice == 4:
        plt.plot(cities, cogs, marker='o')
        plt.ylabel("COGS")
        plt.title("Cities vs COGS")
    elif choice == 5:
        plt.plot(cities, profit, marker='o', label="Profit")
        plt.plot(cities, margin, marker='o', label="Margin")
        plt.plot(cities, sales, marker='o', label="Sales")
        plt.plot(cities, cogs, marker='o', label="COGS")
        plt.legend()
        plt.ylabel("Values")
        plt.title("All Metrics Comparison")
    else:
        print("Invalid choice!")
        return

    plt.tight_layout()
    plt.show()


def bar_plot():
    df = get_data()
    if df is None:
        return

    cities = df['Cities']
    profit = df['Profit']
    margin = df['Margin']
    sales = df['Sales']
    cogs = df['COGS']

    plt.figure(figsize=(12, 6))
    plt.xticks(rotation=45)
    plt.xlabel("Cities")

    print("\nBar Chart Options:")
    print("1. Cities vs Profit")
    print("2. Cities vs Margin")
    print("3. Cities vs Sales")
    print("4. Cities vs COGS")
    print("5. Stacked Bar (not recommended)")
    print("6. Grouped Bar Chart")
    choice = int(input("Enter choice (1-6): "))

    if choice == 1:
        plt.bar(cities, profit)
        plt.ylabel("Profit")
        plt.title("Cities vs Profit")
    elif choice == 2:
        plt.bar(cities, margin)
        plt.ylabel("Margin")
        plt.title("Cities vs Margin")
    elif choice == 3:
        plt.bar(cities, sales)
        plt.ylabel("Sales")
        plt.title("Cities vs Sales")
    elif choice == 4:
        plt.bar(cities, cogs)
        plt.ylabel("COGS")
        plt.title("Cities vs COGS")
    elif choice == 5:
        plt.bar(cities, profit, label="Profit")
        plt.bar(cities, margin, bottom=profit, label="Margin")
        plt.bar(cities, sales, bottom=profit+margin, label="Sales")
        plt.bar(cities, cogs, bottom=profit+margin+sales, label="COGS")
        plt.legend()
        plt.ylabel("Values")
        plt.title("Stacked Bar Chart")
    elif choice == 6:
        x = np.arange(len(cities))
        width = 0.2
        plt.bar(x - 1.5*width, profit, width, label="Profit")
        plt.bar(x - 0.5*width, margin, width, label="Margin")
        plt.bar(x + 0.5*width, sales, width, label="Sales")
        plt.bar(x + 1.5*width, cogs, width, label="COGS")
        plt.xticks(x, cities, rotation=45)
        plt.legend()
        plt.ylabel("Values")
        plt.title("Grouped Bar Chart")
    else:
        print("Invalid choice!")
        return

    plt.tight_layout()
    plt.show()


def pie_plot():
    df = get_data()
    if df is None:
        return

    print("\nPie Chart Options (shows distribution per city):")
    print("1. Profit Distribution")
    print("2. Margin Distribution")
    print("3. Sales Distribution")
    print("4. COGS Distribution")
    choice = int(input("Enter choice (1-4): "))

    if choice == 1:
        plt.pie(df['Profit'], labels=df['Cities'], autopct='%1.1f%%')
        plt.title("Profit Distribution by City")
    elif choice == 2:
        plt.pie(df['Margin'], labels=df['Cities'], autopct='%1.1f%%')
        plt.title("Margin Distribution by City")
    elif choice == 3:
        plt.pie(df['Sales'], labels=df['Cities'], autopct='%1.1f%%')
        plt.title("Sales Distribution by City")
    elif choice == 4:
        plt.pie(df['COGS'], labels=df['Cities'], autopct='%1.1f%%')
        plt.title("COGS Distribution by City")
    else:
        print("Invalid choice!")
        return

    plt.axis('equal')
    plt.show()


def scatter_chart():
    df = get_data()
    if df is None:
        return

    plt.figure(figsize=(10, 6))
    plt.xticks(rotation=45)
    plt.xlabel("Cities")

    plt.scatter(df['Cities'], df['Profit'], color='blue', label="Profit")
    plt.scatter(df['Cities'], df['Margin'], color='red', label="Margin")
    plt.scatter(df['Cities'], df['Sales'], color='green', label="Sales")
    plt.scatter(df['Cities'], df['COGS'], color='orange', label="COGS")

    plt.title("Scatter Chart - All Metrics")
    plt.legend()
    plt.tight_layout()
    plt.show()


# -------------------------------
#   MANIPULATION FUNCTIONS
# -------------------------------
def data_sorting():
    df = get_data()
    if df is None:
        return

    print("\nSort by:")
    print("1. Cities")
    print("2. Profit")
    print("3. Margin")
    print("4. Sales")
    print("5. COGS")
    ch = int(input("Choice: "))

    if ch == 1:
        print(df.sort_values("Cities"))
    elif ch == 2:
        print(df.sort_values("Profit"))
    elif ch == 3:
        print(df.sort_values("Margin"))
    elif ch == 4:
        print(df.sort_values("Sales"))
    elif ch == 5:
        print(df.sort_values("COGS"))
    else:
        print("Invalid choice")


def top_bottom_records():
    df = pd.read_csv("sales.csv", index_col=0)
    top_n = int(input("How many top records? "))
    print(f"\nTop {top_n} records:")
    print(df.head(top_n))

    bottom_n = int(input("How many bottom records? "))
    print(f"\nBottom {bottom_n} records:")
    print(df.tail(bottom_n))


def make_copy():
    try:
        df = pd.read_csv("sales.csv")
        df.to_csv("sales_copy.csv", index=False)
        print("File copied successfully as 'sales_copy.csv'")
    except FileNotFoundError:
        print("Error: sales.csv not found!")


def add_new_record():
    try:
        df = pd.read_csv("sales.csv")
        print("\nCurrent data:")
        print(df)

        new_city = input("Enter City name: ")
        profit = int(input("Enter Profit: "))
        margin = int(input("Enter Margin: "))
        sales = int(input("Enter Sales: "))
        cogs = int(input("Enter COGS: "))

        new_row = pd.DataFrame([[new_city, profit, margin, sales, cogs]],
                               columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)

        df.to_csv("sales.csv", index=False)
        print("\nNew record added successfully!")
        print(df)
    except Exception as e:
        print("Error:", e)


def search_by_city():
    try:
        df = pd.read_csv("sales.csv")
        city = input("Enter city name to search: ")
        result = df[df['Cities'].str.contains(city, case=False)]
        if result.empty:
            print(f"No records found for '{city}'")
        else:
            print(f"\nRecords for '{city}':")
            print(result)
    except FileNotFoundError:
        print("Error: sales.csv not found!")


# -------------------------------
#   STATISTICS FUNCTIONS
# -------------------------------
def show_count():
    df = pd.read_csv("sales.csv", index_col=0)
    print("\nCount of non-null values:")
    print(df.count())


def show_sum():
    df = pd.read_csv("sales.csv", index_col=0)
    print("\nSum of numeric columns:")
    print(df.sum(numeric_only=True))


def show_mean():
    df = pd.read_csv("sales.csv", index_col=0)
    print("\nMean of numeric columns:")
    print(df.mean(numeric_only=True))


def show_max():
    df = pd.read_csv("sales.csv", index_col=0)
    print("\nMaximum values:")
    print(df.max(numeric_only=True))


def show_min():
    df = pd.read_csv("sales.csv", index_col=0)
    print("\nMinimum values:")
    print(df.min(numeric_only=True))


def show_median():
    df = pd.read_csv("sales.csv", index_col=0)
    print("\nMedian of numeric columns:")
    print(df.median(numeric_only=True))


# -------------------------------
#        MAIN PROGRAM LOOP
# -------------------------------
while True:
    main_menu()
    try:
        choice = int(input("\nEnter your choice (0 to exit): "))
    except ValueError:
        print("Please enter a number!")
        continue

    if choice == 0:
        print("\nThank you for using the program. Goodbye!")
        break

    elif choice == 1:
        read_csv_complete()
    elif choice == 2:
        read_without_index()
    elif choice == 3:
        line_plot()
    elif choice == 4:
        bar_plot()
    elif choice == 5:
        pie_plot()
    elif choice == 6:
        scatter_chart()
    elif choice == 7:
        data_sorting()
    elif choice == 8:
        top_bottom_records()
    elif choice == 9:
        make_copy()
    elif choice == 10:
        add_new_record()
    elif choice == 11:
        search_by_city()
    elif choice == 12:
        show_count()
    elif choice == 13:
        show_sum()
    elif choice == 14:
        show_mean()
    elif choice == 15:
        show_max()
    elif choice == 16:
        show_min()
    elif choice == 17:
        show_median()
    else:
        print("Invalid choice! Please select a valid option.")

    input("\nPress Enter to continue...")
