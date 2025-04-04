import pandas as pd
import matplotlib.pyplot as plt



def get_sales_data():
    sales_data = {}

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for day in days:
        while True:
            try:
                sale = int(input(f"Enter sale for {day}: $"))
                sales_data[day] = sale
                break
            except ValueError:
                print("Invalid Input. Please,Enter Valid Input!")
    return sales_data


def update_day_sale(sales_data):
    while True:
        day_to_update = input("Enter the day you want to update or type 'Skip' to continue :").title()
        if day_to_update == 'Skip':
            break
        if day_to_update in sales_data:
            while True:
                try:
                    print(f"Current sale for {day_to_update} is $ {sales_data[day_to_update]}")
                    new_sale = int(input(f"Enter the new sale for the {day_to_update}: $"))
                    sales_data[day_to_update] = new_sale
                    print(f"Updated sale of the {day_to_update} is now ${new_sale}")
                    break
                except ValueError:
                    print("Invalid Input! Please enter valid input.")
        else:
            print("Invalid day! Enter a valid day.")

    return sales_data


def analyze_sales(data):

    best_day =  max(data,key=data.get)

    worst_day = min(data, key=data.get)
    total_sales_weekly = sum(data.values())
    n= len(data)
    avg = round(total_sales_weekly/n,2)
    return  best_day, worst_day, total_sales_weekly, avg

#prepare data for dataframe
def generate_dataframe(data, best_day, worst_day):

    records = []
    for day, sale in data.items():
        records.append({
            "Day" : day,
        "Sale" : sale,
            "Best Day Sale": best_day if day ==best_day else " ",
            "Worst Day Sale": worst_day if day == worst_day else " "
        })
    return pd.DataFrame(records)


def save_to_csv(df, filename="sales_data_weekly.csv", index=False):
    df.to_csv(filename,index =index)
    print(f"Weekly Sales Data CSV saved as {filename}")


def visualize_sales(data):
    days = list(data.keys())
    sales = list(data.values())

    best_day = max(data, key=data.get)
    worst_day = min(data, key=data.get)
    colors = ["green" if day == best_day else "red" if day == worst_day else "skyblue" for day in days]

    plt.figure(figsize=(10,5))

    #Bar chart
    plt.subplot(1,2,1)
    plt.bar(days, sales, color= colors)
    plt.title("Weekly Sales Bar Chart")
    plt.xlabel("Days")
    plt.ylabel("Sales")

    #Line Chart
    plt.subplot(1,2,2)
    plt.plot(days, sales, marker='o',
    linestyle= '-', color='green')
    plt.title("Weekly Sales Trend - Line Chart")
    plt.xlabel("Days")
    plt.ylabel("Sales")

    plt.tight_layout()
    plt.show()



#main program

sales = get_sales_data()
print(sales)

sales = update_day_sale(sales)
best_day, worst_day, total, avg = analyze_sales(sales)

print(f"Total sales revenue of the week: ${total}")
print(f"Average sales for week: ${avg}")
print(f"Best sale day is '{best_day}' and amount is ${sales[best_day]}")
print(f"Worst sales day is {worst_day} and amount is ${sales[worst_day]}")

df = generate_dataframe(sales, best_day, worst_day)
save_to_csv(df)
visualize_sales(sales)