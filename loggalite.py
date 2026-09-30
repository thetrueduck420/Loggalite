#!/usr/bin/python3
from datetime import datetime
import sqlite3 as sql
import os

Home = os.path.expanduser("~")
LoggalitePath = f"{Home}/.loggalite"
DatabasePath = f"{LoggalitePath}/logs.db"

# Logo (little messed up, since i had to make the backslashes print actual backslashes, instead of escape sequences)
Logo = """ _                             _ _ _       
| |                           | (_) |      
| |     ___   __ _  __ _  __ _| |_| |_ ___ 
| |    / _ \\ / _` |/ _` |/ _` | | | __/ _ \\
| |___| (_) | (_| | (_| | (_| | | | ||  __/
\\_____/\\___/ \\__, |\\__, |\\__,_|_|_|\\__\\___|
              __/ | __/ |                  
             |___/ |___/                   
    By On Andrei! """

# Connects to the database
# Im aware that this function doesnt NEED to be here, i just like organisation
def OpenDb():
    Connection = sql.connect(DatabasePath)
    Database = Connection.cursor()
    return Connection, Database

# Sets up the database (if it hasnt already been set up)
def Setup():
    print("\033[32m")

    if not os.path.exists(LoggalitePath):
        os.mkdir(LoggalitePath)

    Connection, Database = OpenDb()

    Database.execute("""
                     CREATE TABLE IF NOT EXISTS LOGS (
                        Time TEXT,
                        Title TEXT,
                        Text TEXT
                     )""")
    Connection.commit()

    return Connection, Database

# Allows the user to select what they wanna do
def SelectionInterface():
    Options = {"entry": "Creates a new entry", "reading": "Select a log, and read it"}

    print("Options:")
    for Option in Options.keys():
        print(f"{Option}: {Options[Option]}")

    Selection = ""

    while not Selection in Options.keys():
        Selection = input("OPTION[: ")

        if not Selection in Options.keys():
            print("SELECTION-INTERFACE]: Invalid Option!")

    return Selection

# Allows the user to write an entry
def Entry():
    Title = input("TITLE[: ")
    print("LOGGALITE]: Type \"__END__\" to end this entry.")

    Text = ""

    while not "__END__" in Text:
        Text += input("[: ")

        if not "__END__" in Text:
            Text += "\n"

    Text = Text.replace("__END__", "")

    return Title, Text

# Inserts an entry into the database
def NewEntry(Title, Entry, Database):
    Time = datetime.today().strftime("%Y-%m-%d_%H:%M:%S")

    Database.execute(f"INSERT INTO LOGS VALUES (\'{Time}\', \'{Title}\', \'{Entry}\')")

# List all logs
def ListLogs(Database):
    Resolution = Database.execute("SELECT Time, Title From LOGS ORDER BY Time")
    return Resolution.fetchall()

# Allows the user to read entries
def Reading(Database):
    LogList = ListLogs(Database)
    Dates = []
    
    for Row in LogList:
        Dates.append(Row[0])
        print(Row)

    Selection = ""

    while not Selection in Dates:
        Selection = input("LOG-DATE[: ")

        if not Selection in Dates:
            print("READING-MODE]: Invalid date!")

    Resolution = Database.execute(f"SELECT Text, Title FROM LOGS WHERE Time = \'{Selection}\'")
    Log = Resolution.fetchone()

    print("", end="\n" * 2)
    
    print("READING-MODE]: LOG START.")
    print("_____________________________________________")

    print(f"TITLE: {Log[1]}")
    print(Log[0])

    print("_____________________________________________")
    print("READING-MODE]: LOG END.")

def main():
    Connection, Database = Setup()
    print(Logo)
    Option = SelectionInterface()

    match Option:
        case "entry":
            Title, Text = Entry()
            NewEntry(Title, Text, Database)
            Connection.commit()

        case "reading":
            Reading(Database)

    Connection.close()

    
    
if __name__ == "__main__":
    main()
