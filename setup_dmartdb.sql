USE DMartDB;
GO

-- Create insert stored procedure
IF OBJECT_ID('sp_InsertSalesData', 'P') IS NOT NULL
    DROP PROCEDURE sp_InsertSalesData;
GO

CREATE PROCEDURE sp_InsertSalesData
    @OrderID nvarchar(255),
    @OrderDate date,
    @CustomerName nvarchar(255),
    @Country nvarchar(255),
    @State nvarchar(255),
    @City nvarchar(255),
    @Region nvarchar(255),
    @Segment nvarchar(255),
    @ShipMode nvarchar(255),
    @Category nvarchar(255),
    @SubCategory nvarchar(255),
    @ProductName nvarchar(255),
    @Discount float,
    @Sales float,
    @Profit float,
    @Quantity int,
    @Feedback bit
AS
BEGIN
    INSERT INTO SalesData
    (
        OrderID, OrderDate, CustomerName, Country, State, City, Region,
        Segment, ShipMode, Category, SubCategory, ProductName,
        Discount, Sales, Profit, Quantity, Feedback
    )
    VALUES
    (
        @OrderID, @OrderDate, @CustomerName, @Country, @State, @City, @Region,
        @Segment, @ShipMode, @Category, @SubCategory, @ProductName,
        @Discount, @Sales, @Profit, @Quantity, @Feedback
    )
END
GO

-- Create get stored procedure
IF OBJECT_ID('sp_GetSalesData', 'P') IS NOT NULL
    DROP PROCEDURE sp_GetSalesData;
GO

CREATE PROCEDURE sp_GetSalesData
AS
BEGIN
    SELECT * FROM SalesData
END
GO
