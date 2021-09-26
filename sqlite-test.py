import sqlite3

def CreateDb() -> None:
    with sqlite3.connect('test.db') as con:
        cur = con.cursor()
        cur.execute('CREATE TABLE new_table (ind INTEGER PRIMARY KEY, words text)')

def AddValue(words: str) -> None:
    with sqlite3.connect('test.db') as con:
        cur = con.cursor()
        cur.execute('INSERT INTO new_table(words) VALUES (?)', (words,))
        con.commit()

def ReadAll() -> None:
    with sqlite3.connect('test.db') as con:
        cur = con.cursor()

        for row in cur.execute('SELECT * FROM new_table ORDER BY ind'):
            print(row)

def main() -> None:
    # CreateDb()
    AddValue('First Words')
    AddValue('Second Words')
    ReadAll()

main()
