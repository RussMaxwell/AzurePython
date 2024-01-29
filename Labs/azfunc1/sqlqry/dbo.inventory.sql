SET DATEFORMAT ymd
SET ARITHABORT, ANSI_PADDING, ANSI_WARNINGS, CONCAT_NULL_YIELDS_NULL, QUOTED_IDENTIFIER, ANSI_NULLS, NOCOUNT ON
SET NUMERIC_ROUNDABORT, IMPLICIT_TRANSACTIONS, XACT_ABORT OFF
GO

CREATE TABLE inventory (
    AutoID nvarchar(50) PRIMARY KEY,
    Make nvarchar(max) NOT NULL, 
    Model nvarchar(max) NOT NULL,
	Year nvarchar(50) NOT NULL,
	Color nvarchar(50) NOT NULL,
	Mileage nvarchar(50) NOT NULL,
	Date_Received datetime NOT NULL,
	Sold nvarchar(50),
	Selling_Agent nvarchar(50),
	modified_Date datetime
);

INSERT autos.dbo.inventory(AutoID, Make, Model, Year, Color, Mileage, Date_Received, Sold, Selling_Agent, modified_Date) VALUES (N'1', N'Ford', N'Mustang', N'2015', N'Silver', N'75000', '2023-09-29 20:23:05.700', N'Yes', NULL, '2023-10-02 21:11:32.597')
INSERT autos.dbo.inventory(AutoID, Make, Model, Year, Color, Mileage, Date_Received, Sold, Selling_Agent, modified_Date) VALUES (N'2', N'Ford', N'Bronco', N'2021', N'Black', N'25000', '2023-09-29 20:23:37.900', N'No', NULL, '2023-10-02 21:11:19.860')
INSERT autos.dbo.inventory(AutoID, Make, Model, Year, Color, Mileage, Date_Received, Sold, Selling_Agent, modified_Date) VALUES (N'3', N'Toyota', N'Camry', N'2018', N'Pink', N'90000', '2023-09-29 20:33:04.237', N'No', NULL, '2023-10-03 18:44:27.567')
INSERT autos.dbo.inventory(AutoID, Make, Model, Year, Color, Mileage, Date_Received, Sold, Selling_Agent, modified_Date) VALUES (N'4', N'Nissan', N'Rogue', N'2022', N'White', N'15000', '2023-09-29 20:33:58.893', N'No', NULL, '2023-10-02 21:19:41.390')
INSERT autos.dbo.inventory(AutoID, Make, Model, Year, Color, Mileage, Date_Received, Sold, Selling_Agent, modified_Date) VALUES (N'5', N'Nissan', N'GTR', N'2015', N'Black', N'12000', '2023-09-29 20:34:36.720', N'No', NULL, '2023-10-02 21:11:19.860')
INSERT autos.dbo.inventory(AutoID, Make, Model, Year, Color, Mileage, Date_Received, Sold, Selling_Agent, modified_Date) VALUES (N'6', N'Chevy', N'Camaro', N'2018', N'Orange', N'62000', '2023-09-29 20:35:07.520', N'No', NULL, '2023-10-02 21:11:19.860')
INSERT autos.dbo.inventory(AutoID, Make, Model, Year, Color, Mileage, Date_Received, Sold, Selling_Agent, modified_Date) VALUES (N'7', N'Hyundai', N'Veloster', N'2017', N'White', N'78000', '2023-09-29 23:24:37.880', N'No', NULL, '2023-10-02 21:11:19.860')
INSERT autos.dbo.inventory(AutoID, Make, Model, Year, Color, Mileage, Date_Received, Sold, Selling_Agent, modified_Date) VALUES (N'8', N'Honda', N'Accord', N'2021', N'Brown', N'53000', '2023-09-29 23:27:11.547', N'No', NULL, '2023-10-02 21:11:19.860')
GO