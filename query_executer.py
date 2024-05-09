import sqlite3
from sql_queries import question_set_dict


def run_query(query):
    # Connect to the SQLite database
    conn = sqlite3.connect('imdb_data.db')
    cur = conn.cursor()
    
    cur.execute(query)
    
    results = cur.fetchall()
    
    conn.close()
    
    return results

def main():
    # Display options to the user
    print("Please choose a report to generate:")
    for key in question_set_dict:
        print(key[-1], "-", question_set_dict[key]['question'])

    # Take user input
    choice = input("Enter your choice (1, 2, or 3): ")
    key = 'question_' + choice
    print("You chose:", key)

    if key in question_set_dict:
        query = question_set_dict[key]['query']
        results = run_query(query)
        print("Results:\n" )
        for line in results:
            print(line)
        
    else:
        print("Invalid choice. Please run the program again with a valid option.")

if __name__ == "__main__":
    main()