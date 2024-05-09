# Project Overview:

### Database Initialization: 
Utilizing DDL scripts, the project begins with the initialization of a SQLite database where the schema is defined, and tables are created.

### Data Ingestion: 
Data from the provided CSV files is successfully imported into the newly established database, ensuring all data is ready for querying.

### Query Execution and Reporting: 
The application facilitates user interaction, allowing the selection and execution of SQL queries to generate the required reports. This is controlled through a straightforward interface that prompts the user to select a report to be generated based on predefined questions.

---

# File descriptions :

## DB_initialise.py

This script serves as the foundation of the project. It creates a SQLite database, establishes a file on the local system, and generates three tables: series_average, seasons_full, and episode_ratings using predefined DDL statements. It also handles the ingestion of CSV data from the raw CSV data directory into these tables. The script ensures that after data loading, the database connection is properly committed and closed. This script needs to be run initially to set up the database for the application.

## DDL_scripts.py

Contains all the CREATE TABLE queries which define the schema for the tables mentioned above. The column names and types are carefully chosen to ensure data integrity and efficient query execution. This modular approach allows easy maintenance and updates to the database schema if required.

## SQL_queries.py

This script hosts a dictionary (question_set_dictionary) that maps questions to their corresponding SQL queries. This encapsulation facilitates easy updates to the queries and provides a clear association between the questions posed and their SQL solutions.

## Query_executor.py

Acts as the interface for the application. It allows users to interact with the database by selecting which report they wish to generate based on the pre-defined questions. The script executes the appropriate SQL queries and displays the results to the user. This component enhances the usability of the application, making it accessible even to those unfamiliar with SQL.

## Example_run_notebook.ipynb

To demonstrate the application's capabilities, this Jupyter notebook contains examples of running Query_executor.py. It showcases how the application responds to user inputs (1, 2, or 3) to generate respective reports. This notebook is crucial for understanding the application flow and verifying its functionality.

---

# Setup and Running the Application

- For the first time, please run DB_initialise once to create the database instance, which will create a imdb_data.db file, which contains the entire data
- Then you can use the query_executor.py file to run commands from the command line. 
- Alternatively, you can use the example_run_notebook.ipynb file to run in an interactive notebook format

---

Author : Saif. Raja
Email : saifuddin.raja24@gmail.com
Cell : +91 7775029864