import sqlite3

CREATE_TABLE_DIARY = "CREATE TABLE IF NOT EXISTS diary(id INTEGER PRIMARY KEY, content TEXT);"
ADD_ENTRY = "INSERT INTO diary(id, content) VALUES (?,?);"
VIEW_ALL_ENTRIES = "SELECT * FROM diary;"
UPDATE_CONTENT = "UPDATE diary SET content = ? WHERE id = ?;"
DELETE_ENTRY_BY_ID = "DELETE FROM diary WHERE id = ?;"


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("data.db")
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute(CREATE_TABLE_DIARY)

    def add_entry(self):
        entry_id = input("Enter the entry id: ")
        content = input("Enter the content for the entry: ")
        with self.connection:
            self.connection.execute(ADD_ENTRY, (entry_id, content))

    def view_entries(self):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(VIEW_ALL_ENTRIES)
            return cursor.fetchall()

    def update_entry(self):
        entry_id = input("Enter the entry id to update:")
        content = input("Enter the new content: ")
        with self.connection:
            self.connection.execute(UPDATE_CONTENT, (content, entry_id))
            print("Entry Updated Successfully")

    def delete_entry(self):
        entry_id = input("Enter the id of the entry to delete: ")
        with self.connection:
            self.connection.execute(DELETE_ENTRY_BY_ID, (entry_id,))
            print("Entry Deleted Successfully")

    @staticmethod
    def clear_screen():
        print("\n"*50)


db = Database()
db.create_tables()

menu = """
Select one of the following options:
1) Add new entry for today.
2) View all entries.
3) Update entry
4) Delete entry by ID.
5) Exit

Your selection: """

welcome = """
------------------------------------  
Welcome to the programming diary!
------------------------------------"""
db.clear_screen()
print(welcome)

while (user_input := input(menu)) != "5":
    if user_input == "1":
        db.clear_screen()
        db.add_entry()
    elif user_input == "2":
        db.clear_screen()
        entries = db.view_entries()
        for entry in entries:
            output = f"""
            -------
            ID: {entry[0]} 
            Content: {entry[1]}"""
            print(output)
    elif user_input == "3":
        db.clear_screen()
        db.update_entry()
    elif user_input == "4":
        db.clear_screen()
        db.delete_entry()
    else:
        print("Invalid input please try again.")
