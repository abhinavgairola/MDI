import sqlite3
import csv
from tabulate import tabulate

class CSVtoSQL:
    """
    A utility class for handling CSV data and interacting with an SQLite database.

    This class provides methods to infer the delimiter and column data types from a CSV file,
    write the contents of the CSV file into an SQLite in-memory database table,
    and execute SQL queries on the database to retrieve and format the results.

    The CSVtoSQL class is designed to facilitate database management and SQL operations,
    making it easier to work with CSV data and perform database-related tasks in Python.

    Usage:
        1. Use the `csv_sniffer` method to infer the delimiter and column data types from a CSV file.
        2. Use the `write_csv_to_sql` method to create an SQLite table and import the CSV data into the table.
        3. Use the `execute_and_format` method to execute SQL queries on the database and format the results.

    Note: The class assumes that the CSV file is well-formed and does not handle data validation or cleaning.

    Dependencies:
        - csv module (part of the Python standard library)
        - sqlite3 module (part of the Python standard library)
        - tabulate module (install using `pip install tabulate`)

    Example:
        csv_data = CSVtoSQL()
        delimiter, headers, column_data_types = csv_data.csv_sniffer('data.csv')
        conn, cursor = csv_data.write_csv_to_sql(delimiter, headers, column_data_types, 'my_table', 'data.csv')
        result_table = csv_data.execute_and_format(conn, 'SELECT * FROM my_table')
        print(result_table)
    """

    @staticmethod
    def csv_sniffer(csv_file):
        """
        Infers the delimiter and column data types from a CSV file.

        Parameters:
            csv_file (str): The path to the CSV file.

        Returns:
            tuple: A tuple containing the delimiter, headers, and inferred column data types.
        """

        with open(csv_file, "r") as file:
            sample_data = file.read(1024)  
            dialect = csv.Sniffer().sniff(sample_data)
            delimiter = dialect.delimiter

            file.seek(0) 
            csv_reader = csv.reader(file, delimiter=delimiter)
            headers = next(csv_reader)
            sample_row = next(csv_reader)
            column_data_types = [type(cell).__name__ for cell in sample_row]

            return delimiter, headers, column_data_types

    @staticmethod
    def write_csv_to_sql(delimiter, head, col_type, tab_name, csv_file="name",encoding="utf-8"):
        """
        Write the contents of a CSV file to an SQLite in-memory database table.

        Parameters:
            delimiter (str): The delimiter used in the CSV file.
            head (list): The list of column headers.
            col_type (list): The list of column data types.
            tab_name (str): The name of the table to be created.
            csv_file (str): The path to the CSV file.
            encoding (str, optional): The encoding of the CSV file. Default is "utf-8".

        Returns:
            tuple: A tuple containing the connection and cursor objects.
        """

       
        conn = sqlite3.connect(":memory:")

        
        cursor = conn.cursor()
        table_name = tab_name
        column_definitions = ", ".join(f"`{header}` {data_type}" for header, data_type in zip(head, col_type))
        create_table_query = f"CREATE TABLE `{table_name}` ({column_definitions})"
        cursor.execute(create_table_query)

       
        encodings = ["utf-8", "latin-1", "iso-8859-1", "cp1252"]
        
       
        for encoding in encodings:
            try:
                with open(csv_file, "r", encoding=encoding) as file:
                    csv_reader = csv.reader(file, delimiter=delimiter)
                    next(csv_reader)  # Skip the header row

                    for row in csv_reader:
                        cursor.execute(f"INSERT INTO `{table_name}` VALUES ({','.join(['?'] * len(row))})", row)

                break 

            except UnicodeDecodeError:
                continue

        conn.commit()

        return conn, cursor

    @staticmethod
    def execute_and_format(conn, query):
        """
        Execute an SQL query on a SQLite connection and format the results as a table.

        Parameters:
            conn (sqlite3.Connection): The SQLite connection object.
            query (str): The SQL query to execute.

        Returns:
            tuple: A tuple containing the formatted table as a string and the rows of the result together with headers.
        """
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

   
        headers = [description[0] for description in cursor.description]

 
        rows = [list(row) for row in result]

        return tabulate(rows, headers, tablefmt="grid", stralign='center'),rows,headers
    
    @staticmethod
    def describe(conn, table_name):
        """
        Retrieve the column information for a table in the database and format it as a table.

        Parameters:
            conn (sqlite3.Connection): The SQLite connection object.
            table_name (str): The name of the table to describe.

        Returns:
            str: The formatted table containing the column information.
        """
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        result = cursor.fetchall()

        headers = ["Column Name", "Data Type", "Nullable"]

        rows = [[column[1], column[2], "Yes" if column[3] else "No"] for column in result]

        table = tabulate(rows, headers, tablefmt="grid")

        return table