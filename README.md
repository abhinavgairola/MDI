# CSVtoSQL

A utility class for handling CSV data and interacting with an SQLite database.

The `CSVtoSQL` class provides an efficient solution for managing CSV data and performing database operations using SQLite. It simplifies the process of working with CSV files and executing SQL queries, enabling seamless integration of CSV data into an SQLite database.

## Key Features

- **CSV Data Analysis:** The `csv_sniffer` method automatically infers the delimiter and column data types from a CSV file. It intelligently detects the structure and characteristics of the data, saving time and effort in manual analysis.

- **Data Import:** The `write_csv_to_sql` method creates an in-memory SQLite database table and imports the contents of a CSV file into the table. It handles the creation of the table schema and efficiently inserts the data, ensuring a smooth and streamlined data import process.

- **SQL Query Execution and Formatting:** The `execute_and_format` method executes SQL queries on the SQLite database and formats the result as a table. It provides a clean and organized representation of query results, making it easy to analyze and interpret the data.

## Simplify Database Management and SQL Operations

The `CSVtoSQL` class simplifies database management and SQL operations related to CSV data. It eliminates the need for manual schema creation, data type inference, and complex import processes. By automating these tasks, it saves valuable time and effort, allowing users to focus on data analysis and deriving meaningful insights.

The class provides a convenient and efficient way to handle CSV data and leverage the power of SQL for data manipulation and analysis. Whether it's importing large CSV files, executing complex SQL queries, or formatting query results, the `CSVtoSQL` class streamlines the entire process, making it an essential tool for database management and SQL tasks.

## Usage Example

Here's an example of how to use the `CSVtoSQL` class:

```python
csv_data = CSVtoSQL()
delimiter, headers, column_data_types = csv_data.csv_sniffer('data.csv')
conn, cursor = csv_data.write_csv_to_sql(delimiter, headers, column_data_types, 'my_table', 'data.csv')
result_table, rows = csv_data.execute_and_format(conn, 'SELECT * FROM my_table')
print(result_table)
print(rows)
```

# SQL Operations Jupyter Notebook
This `Jupyter Notebook` demonstrates various `SQL` operations using `SQLite` in `Python`. It provides examples of creating a database, creating tables, inserting data into tables, executing `SQL` queries, and visualizing query results.

The notebook starts with setting up the SQLite connection and creating a database. It then demonstrates the creation of tables with appropriate schemas and inserts sample data into the tables. SQL queries are executed to retrieve and manipulate the data, showcasing the power of SQL in data analysis and retrieval.

Finally, the notebook utilizes pandas and matplotlib libraries to visualize the query results in the form of tables and charts, providing a comprehensive view of the data.

This notebook serves as a reference for `SQL` operations in `Python` using `SQLite` and can be a helpful resource for data analysts and developers working with relational databases.
