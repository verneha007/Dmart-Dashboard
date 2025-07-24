import pandas as pd
import pyodbc

# Adjust path to your Excel file:
excel_file = r'C:\Users\Neha Verma\Documents\DMart Data Store.xlsx'

# Read Excel
df = pd.read_excel(excel_file)

# Show original column names to confirm
print("Original columns in Excel file:")
print(df.columns)

# Rename columns to match database fields
df.rename(columns={
    'Order ID': 'OrderID',
    'Order Date': 'OrderDate',
    'Customer Name': 'CustomerName',
    'Ship Mode': 'ShipMode',
    'Sub-Category': 'SubCategory',
    'Product Name': 'ProductName',
    'Feedback?': 'Feedback'
}, inplace=True)

# Show new column names to confirm
print("Renamed columns:")
print(df.columns)

# Connect to SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'DATABASE=DMartDB;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Insert each row using stored procedure
for index, row in df.iterrows():
    cursor.execute("""
        EXEC sp_InsertSalesData
            @OrderID=?, @OrderDate=?, @CustomerName=?, @Country=?, @State=?,
            @City=?, @Region=?, @Segment=?, @ShipMode=?, @Category=?,
            @SubCategory=?, @ProductName=?, @Discount=?, @Sales=?, @Profit=?, @Quantity=?, @Feedback=?
    """,
        row['OrderID'],
        row['OrderDate'],
        row['CustomerName'],
        row['Country'],
        row['State'],
        row['City'],
        row['Region'],
        row['Segment'],
        row['ShipMode'],
        row['Category'],
        row['SubCategory'],
        row['ProductName'],
        row['Discount'],
        row['Sales'],
        row['Profit'],
        int(row['Quantity']),
        int(row['Feedback'])  # should be 0 or 1
    )
    print(f"Inserted row {index+1}")

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("✅ Data inserted successfully!")
