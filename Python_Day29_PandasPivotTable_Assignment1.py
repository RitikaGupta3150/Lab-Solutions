"""
Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.
Input:Download the file salesdata.csv From LMS Output:
"""

# Importing the necessary libraries
import pandas as pd

# Reading the sales data from the CSV file
df = pd.read_csv("C:/Users/asus/Downloads/salesdata.csv")


# Creating a Pivot table to find total sale amount region-wise, manager-wise, and salesman-wise
pivot_table = pd.pivot_table(df, 
                             values='Sale_amt',  # Summarizing the Sale_amt column
                             index=['Region', 'Manager', 'SalesMan'],  # Grouping by Region, Manager, and SalesMan
                             aggfunc='sum')  # Aggregating the sales by sum

# Display the resulting Pivot table
print(pivot_table)

"""
ANSWER=

                           Sale_amt
Region  Manager SalesMan           
Central Douglas John       124016.0
        Hermann Luis       206373.0
                Shelli      33698.0
                Sigal      125037.5
        Marth   Steven      14000.0
        Martha  Steven     185690.0
        Timothy David      140955.0
East    Douglas Karen       48204.0
        Martha  Alexander  236703.0
                Diana       36100.0
West    Douglas Michael     66836.0
        Timothy Stephen     88063.0

"""
