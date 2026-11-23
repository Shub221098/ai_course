import pandas as pd
import numpy as np

properties = pd.DataFrame({
    "property_id": [101, 102, 103, 104, 105, 106, 107, 108, 108],
    "title": [
        "Luxury 3 BHK",
        "2 BHK Flat",
        "Premium Villa",
        "Affordable 2 BHK",
        "Luxury Villa",
        "3 BHK Apartment",
        "Budget Flat",
        "Sea View Villa",
        "Sea View Villa"
    ],
    "city": [
        "Surat",
        " surat ",
        "Mumbai",
        "Delhi",
        None,
        "SURAT",
        "Surat",
        "Mumbai",
        "Mumbai"
    ],
    "type": [
        "Flat",
        "Flat",
        "Villa",
        "Flat",
        "Villa",
        "Apartment",
        "Flat",
        "Villa",
        "Villa"
    ],
    "price": [
        5000000,
        4500000,
        12000000,
        np.nan,
        9000000,
        7000000,
        2500000,
        15000000,
        15000000
    ],
    "bedrooms": [
        3,
        2,
        4,
        2,
        5,
        3,
        1,
        5,
        5
    ],
    "area_sqft": [
        1500,
        1100,
        3000,
        900,
        3500,
        1800,
        700,
        4000,
        4000
    ]
})

builders = pd.DataFrame({
    "builder_id": [1, 2, 3, 4],
    "builder_name": [
        "Karma Builders",
        "ABC Developers",
        "XYZ Group",
        "Prime Infra"
    ]
})


property_builder = pd.DataFrame({
    "property_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "builder_id": [1, 2, 1, 3, 2, 1, 4, 3]
})


############# Numpy Practice #############

prices = np.array([
    5000000,
    4500000,
    12000000,
    4000000,
    9000000,
    7000000
])

# Find:

# minimum price
print(np.min(prices)) # or prices.min()
# maximum price
print(np.max(prices)) # or prices.max()
# average price
print(np.mean(prices)) # or prices.mean()
# median price
print(np.median(prices))
# standard deviation
print(np.std(prices)) # or prices.std()

# Increase prices by 10%
prices = prices * 1.10
print(prices)


# Find properties priced above ₹70 lakh. Use a Boolean mask.
# boolean mask
mask = prices > 7000000
print(prices[mask])

# Create a discount of 5% on every property.Calculate: original price, discount amount, final price

print("\nOriginal Prices: ")
print(prices)
discount_prices = prices * 0.05
print("\nDiscount Prices: ")
print(discount_prices)

final_prices = prices - discount_prices
print("\nFinal Prices: ")
print(final_prices)

area = np.array([1000, 1500, 2000, 2500, 3000])

# Calculate price per sqft using: price_per_sqft = price / area

price_per_sqft = prices[:len(area)] / area
print(price_per_sqft)

# Use np.where(): price >= 1 crore → "Premium", price >= 50 lakh → "Mid" , otherwise → "Budget"

# Solution 1:- 
categories_list = ["Premium" if p >= 10000000 else "Mid" if p >= 5000000 else "Budget" for p in prices]
categories = np.array(categories_list)
print(categories)

# Solution 2:-
categories_list = np.where(prices > 10000000, "Premium", np.where(prices > 5000000, "Mid", "Budget"))
print(categories_list)

# Solution 3:- 
categories = [prices > 10000000, prices > 5000000]
conditions = ["Premium", "Mid"]
fetch_categories = np.select(categories, conditions, default="Budget")
print(fetch_categories)

# Solution 4:- 
def classify(price):
    if price >= 10000000: return "Premium"
    elif price >= 5000000: return "Mid"
    return "Budget"

v_classify = np.vectorize(classify)
categories = v_classify(prices)
print(categories)

############# Pandas Practice #############

# Find rows, columns, column names, data types from properties

print("\n Count of (Rows, Colums)")
print(properties.shape)

print("\nColums Information")
print(properties.columns)

print("\nColumns datatypes")
print(properties.dtypes)

print("\nInformation of table.")
print(properties.info)

# Find missing values? Also calculate missing percentage for every column.

# Count of missing values
missing_count = properties.isna().sum()

# Percentage of missing values (Total rows = 9)
missing_percentage = (properties.isna().sum() / len(properties)) * 100

# Combine them into a neat summary table
missing_summary = pd.DataFrame({
    'Missing Count': missing_count,
    'Percentage (%)': missing_percentage.round(2)
})
print(missing_summary)

# Find exact duplicate rows. Then check duplicate property_id.

# Show the actual exact duplicate rows
print("Exact Duplicate Rows:")
print(properties[properties.duplicated()])

# Show rows that have a duplicate property_id
print("\nRows with Duplicate property_id:")
print(properties[properties.duplicated(subset="property_id")])

# Use describe() and inspect: price, bedrooms, area_sqft
print(properties[["price", "bedrooms", "area_sqft"]].describe())


# Convert:

# "Surat"
# " surat "
# "SURAT"

# into: Surat
# Handle missing city as: Unknown

properties["city"] = properties["city"].fillna("Unknown").str.strip().str.title()
print(properties)


# Find the missing price. Calculate: mean, median. Compare them. Then fill the missing price using median.

# Identify the row with missing price
print(properties[properties["price"].isna()])

# Calculate mean
mean_price = properties["price"].mean()
median_price = properties["price"].median()
print(mean_price)
print(median_price)

# Fill the missing price using median
properties["price"] = properties["price"].fillna(median_price)
print("\nUpdated missing price with median value")

print(properties[["property_id", "title", "price"]])


# Remove duplicate property records based on: property_id
properties = properties.drop_duplicates(subset="property_id", keep="first")
print(properties)

print("\nVerifying any missing values still exist or duplicate exist")

print(properties.isna().sum())
print(properties.duplicated())

# Find all Properties in Surat

surat_properties = properties[properties["city"].isin(["Surat"])]
print(surat_properties)

# Find properties: price > 50 lakh

range_properties = properties[properties["price"] > 5000000]
print(range_properties)

# Find properties: Surat AND price > 50 lakh

condition_properties = properties[(properties["city"] == "Surat") & (properties["price"] > 5000000)]
print(condition_properties)

# Find Flat and Apartment
type_properties = properties[properties["type"].isin(["Flat", "Apartment"])]
print(type_properties)

# Find properties where: bedrooms >= 3 AND area_sqft >= 1500

filtered_properties = properties[(properties["bedrooms"] > 3) & (properties["area_sqft"] >= 1500)]
print(filtered_properties)

# Find properties between: ₹50 lakh and ₹1 crore

btwn_properties = properties[properties["price"].between(5000000, 10000000)]
print(btwn_properties)

# Using iloc, get: first 3 rows

get_first_three_rows = properties.iloc[:3]
print(get_first_three_rows)

# Using iloc, get: first row's price
first_row_price = properties.iloc[0, 4]
print(first_row_price)
get_first_row_price = properties["price"].iloc[:1]
print(get_first_row_price)

# Using loc, get: title, price for properties costing more than ₹70 lakh.
get_title_price = properties.loc[properties["price"] > 7000000, ["title", "price"]]
print(get_title_price)

# Using loc, update all "Flat" properties: bedrooms = 3, Don't create a copy.

properties.loc[properties["type"] == "Flat", "bedrooms"] = 3
print(properties[["title", "type", "bedrooms"]])

# Find properties whose title contains: "Luxury"

title_property = properties[properties["title"].str.contains("Luxury")]
print(title_property)

# Find properties whose title contains: "BHK"

title_bhk = properties[properties["title"].str.contains("BHK")]
print(title_bhk)

# Create a new column: title_length using: str.len()

properties["title_length"] = properties["title"].str.len()
print(properties)

# Create: normalized_title using: strip title case

properties["normalized_title"] = properties["title"].str.strip().str.title()
print(properties[["title", "normalized_title"]])

# Create Price per sqft => price_per_sqft = price / area_sqft, Use Pandas/NumPy.

properties["price_per_sqft"] = properties["price"] / properties["area_sqft"]

print(properties)

# Create Property Category: price_category
# Rules:

# >= 1 crore       → Premium
# >= 50 lakh       → Mid Range
# < 50 lakh        → Budget

# Use either:

# np.where()

# or apply().

def classify_price(price):
    if price >= 10000000:
        return "Premium"
    elif price >= 5000000:
        return "Mid Range"
    else:
        return "Budget"

# 2. Apply it to the price column
properties["price_category"] = properties["price"].apply(classify_price)

print(properties[["title", "price", "price_category"]])


# Q31 — Large Property

# Create:

# size_category

# Rules:

# area >= 2500 → Large
# area < 2500  → Standard

properties["size_category"] = properties["area_sqft"].apply(lambda x: "Large" if x >= 2500 else "Standard")
print(properties[["property_id", "size_category", "area_sqft"]])

# Find average price by city.

avg_price = properties.groupby("city")["price"].mean()
print(avg_price)

# Find maximum price by city.
max_price = properties.groupby("city")["price"].max()
print(max_price)

# Find number of properties by city.
count_properties = properties.groupby("city")["property_id"].count()
print(count_properties)

# Find average price by property type.
avg_price_type = properties.groupby("type")["price"].mean()
print(avg_price_type)

# Create this summary:

# city
# property_count
# average_price
# minimum_price
# maximum_price

# Use:

# groupby().agg()

summary = properties.groupby("city").agg(
    property_count = ("property_id", "count"),
    average_price = ("price", "mean"),
    minimum_price = ("price", "min"),
    maximum_price = ("price", "max")
)
print(summary)

# Sort the city summary by: average_price descending

sort_summary = summary.sort_values(by="average_price", ascending=False)
print(sort_summary)

# How many properties of each type exist?
type_properties = properties["type"].value_counts()
print(type_properties)

# Create a pivot table:
# city × type
# Values: average price

table = pd.pivot_table(
    data=properties,
    values="price",       # The column to aggregate
    index="city",         # Rows
    columns="type",       # Columns
    aggfunc="mean"        # Aggregation strategy
)

print(table)

# Create a pivot table:
# city × type
# Values: property count

table2 = pd.pivot_table(
    data=properties,
    values="property_id",
    index="city",
    columns="type",
    aggfunc="count"
)
print(table2)

# Merge: properties + property_builder using: property_id

new_table = pd.merge(
    properties,
    property_builder,
    on="property_id"
)
print(new_table)

final_merge = pd.merge(
    new_table,
    builders,
    on="builder_id"
)

print(final_merge[["property_id",
"title",
"city",
"type",
"price",
"bedrooms",
"area_sqft",
"builder_id",
"builder_name"]])

# Find the: Most expensive property and Return the complete row.
most_expensive_property = final_merge.loc[final_merge["price"].idxmax()]

print("Most Expensive Property Record:")
print(most_expensive_property)

# Find the: Cheapest property Complete row. Use: idxmin()

cheapest_property = final_merge.loc[final_merge["price"].idxmin()]
print(cheapest_property)

# Find the: Top 3 most expensive properties Use: nlargest()

nlargest_property = final_merge.nlargest(3, columns="price")
print(nlargest_property)

# Find the: Top 3 least expensive properties Use: nsmallest()

nsmallest_property = final_merge.nsmallest(3, columns="price")
print(nsmallest_property)

# Find: Which city has the highest average property price? Don't manually inspect the values. Let Pandas determine it.

highest_average_city = final_merge.groupby("city")["price"].mean().idxmax()
highest_average_value = final_merge.groupby("city")["price"].mean().max()

print(highest_average_city)
print(highest_average_value)

# Find: Which builder has the highest number of properties? You will need: merge, groupby, sort
builder_highest_property = final_merge.groupby("builder_name")["property_id"].count().sort_values(ascending=False)
print(builder_highest_property)

# Find: Average price per sqft for each city.
avg_price = final_merge.groupby("city")["price_per_sqft"].mean()
print(avg_price)

# Q50 🔥🔥🔥

# Find:

# The most expensive property per city.

# Hint:

# You'll need to think about:

# groupby
# idxmax
# loc

max_price = final_merge.groupby("city")["price"].idxmax()

most_expensive_per_city = final_merge.loc[max_price]
most_expensive_per_city = most_expensive_per_city.sort_values(by="price", ascending=False)

print(most_expensive_per_city[["city", "title", "type", "price", "builder_name"]])