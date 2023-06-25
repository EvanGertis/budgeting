import openpyxl
import matplotlib.pyplot as plt
import numpy as np

# Load the report file
workbook = openpyxl.load_workbook("results.xlsx")
sheet = workbook.active

# Define a dictionary of data labels and the corresponding cell references in the sheet
retirement_data = {
    "Retirement Savings": "B2",
    "Retirement Goal": "B3"
}

vacation_data = {
    "Vacation Savings": "B5",
    "Vacation Goal": "B6"
}

weekly_spending_data = {
    "Spending": "B8",
    "Savings": "B9"
}

monthly_spending_data = {
    "Spending": "B11",
    "Savings": "B12"
}

# Define a function to extract the data from the cells
def get_data(data):
    raw_data = {label: sheet[cell].value for label, cell in data.items()}
    for label, value in raw_data.items():
        if isinstance(value, float) and np.isnan(value):
            raw_data[label] = 0
    return raw_data

# Define a function to generate a bar chart for the data
def generate_bar_chart(data, title):
    labels = list(data.keys())
    values = list(data.values())
    plt.bar(labels, values)
    plt.title(title)
    plt.ylabel("Value (USD)")
    plt.show()

# Define a function to generate a pie chart for the data
def generate_pie_chart(data, title):
    labels = list(data.keys())
    values = list(data.values())
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.show()

# Call the functions to generate the bar charts and pie charts
generate_pie_chart(get_data(retirement_data), "Retirement Progress")
generate_pie_chart(get_data(vacation_data), "Vacation Savings")
generate_bar_chart(get_data(weekly_spending_data), "Weekly Spending")
generate_bar_chart(get_data(monthly_spending_data), "Monthly Spending")