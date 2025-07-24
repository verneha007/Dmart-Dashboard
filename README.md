# Dmart-Dashboard

📊 DMart Dynamic Sales Dashboard 

📌 Project Overview
This project automates the daily process of loading DMart's sales data (from Excel files) into a SQL Server database and visualizing it in Power BI. It helps management monitor performance and make sales improvement decisions.

🧰 Tools & Technologies
Excel – Daily input file from operations (same format every day)

Python 3.x – Reads Excel and pushes data into SQL via stored procedure

MS SQL Server Express – Stores historical sales data

Power BI Desktop – Connects to SQL and provides dynamic dashboards

🔄 Daily Workflow
Drop Excel File: Save DMart Data Store.xlsx into the project folder.

Run Python Script: It will call sp_InsertSalesData to upload data to the DB.

Open Power BI & Refresh: Dashboard updates using sp_GetSalesData.

🛠️ Setup Instructions
1. SQL Database Setup
Run setup_dmartdb.sql in SQL Server Management Studio (SSMS).

Creates database DMartSalesDB

Creates SalesData table

Adds insert (sp_InsertSalesData) and read (sp_GetSalesData) stored procedures

2. Python Script
Script reads Excel and inserts data into SQL using the stored procedure.

Required Python libraries: pandas, pyodbc, openpyxl, numpy

No need to modify SQL after setup.

3. Power BI
Connect Power BI to SQL Server:

Use EXEC sp_GetSalesData as the query

Design visuals like:

Sales trends

Top stores/products

Filters: Store, Date, Product

Save the .pbix file for future refreshes


