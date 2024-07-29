import pandas as pd

international_sales_file_path = '/datasets/sales/International_Sales.csv'
local_sales_file_path = '/datasets/sales/Sales_Data_Orders.csv'
int_df = pd.read_csv(international_sales_file_path)
loc_df = pd.read_csv(local_sales_file_path)

int_df['Order ID'] = int_df['Order ID'].astype(str)
int_df['Order ID'] = int_df['Order ID'].str.strip()

# print(int_df.info())
# print(int_df.columns)
# print(loc_df.columns)

# drop unecessary columns
int_df = int_df.drop(columns=['Customers','Region', 'Country', 'Item Type', 'Sales Channel','Order Priority', 'Unit Cost','Total Cost'])
loc_df = loc_df.drop(columns=['Row ID', 'Customer ID', 'Ship Mode', 'Segment', 'Postal Code', 'Product ID', 'Discount'])

# print(int_df.columns)
# print(loc_df.columns)

# print(int_df.sample(7))
# print(loc_df.sample(7))

# create unit price columns for local sales data
loc_df['Unit Price'] = loc_df['Sales'] / loc_df['Quantity']


# print(int_df.columns)
# print(loc_df.columns)


# rename columns to match international sales data
loc_df.rename(columns={'Sales': 'Total Revenue', 'Quantity': 'Units Sold', 'Profit': 'Total Profit'}, inplace=True)

# adjust columns locations for both data frames to match
loc_df = loc_df.iloc[:, [0, 1,  2, 4, 6, 3, 5 ]]
int_df = int_df.iloc[:, [1, 0, 2, 3, 4, 5, 6]]

# merge the two data frames
merged_df = pd.concat([int_df, loc_df], axis=0, ignore_index=True)
# merged_df.tail(7)

# export the merged data frame to a csv file
merged_df.to_csv('/datasets/sales/merged_sales.csv', index=True)