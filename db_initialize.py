import sqlite3
import pandas as pd

# Connect to SQLite database (this will create the database file if it does not exist)
conn = sqlite3.connect('imdb_data.db')

# Create a cursor object using the connection
cur = conn.cursor()



from DDL_scripts import \
    ddl_query__series_average , ddl_query__seasons_full , ddl_query__episode_ratings

# Execute the DDL statements
cur.execute(ddl_query__series_average)
cur.execute(ddl_query__seasons_full)
cur.execute(ddl_query__episode_ratings)



data_paths = {
    "series_average": "raw_csv_data/all-series-ep-average.csv",
    "seasons_full": "raw_csv_data/top-seasons-full.csv",
    "episode_ratings": "raw_csv_data/all-episode-ratings.csv"
    }


for table_name, file_path in data_paths.items():
    df = pd.read_csv(file_path)
    
    # Convert the 'Rating Count' column from string to integer
    # this is needed for the SQL table to be created correctly
    #    this was discvered in the EDA stage
    if 'Rating Count' in df.columns:
        df['Rating Count'] = df['Rating Count'].str.replace(',', '')
        df['Rating Count'] = df['Rating Count'].astype(int)

    # Remove any unnamed columns which are likely redundant indexes from CSV
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # convert all df column names to lowercase
    df.columns = map(str.lower, df.columns)

    # Write the data to SQL (this replaces the table content if it exists)
    df.to_sql(table_name, conn, if_exists='replace', index=False)


conn.commit()

conn.close()
