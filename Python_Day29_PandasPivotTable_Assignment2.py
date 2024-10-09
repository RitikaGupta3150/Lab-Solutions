"""
Write a Pandas program to create a Pivot table and find the item wise unit sold.
Input:Download the file salesdata.csv From LMS
"""
# Importing the necessary libraries
import pandas as pd

# Reading the sales data from the CSV file
df = pd.read_csv("C:/Users/asus/Downloads/salesdata.csv")
# Creating a Pivot table to find the total units sold for each item
pivot_table = pd.pivot_table(df, 
                             values='Units',  # Using 'Units' column for the total units sold
                             index='Item',  # Grouping by 'Item'
                             aggfunc='sum')  # Aggregating by sum to get total units sold

# Display the resulting Pivot table
print(pivot_table)

"""
ANSWER=

              Units
Item               
Cell Phone      278
Desk             10
Home Theater    722
Television      716
Video Games     395

"""
