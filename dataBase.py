import sqlite3


#---------------
# create database 

db = sqlite3.connect("app.db")
cr = db.cursor()


# create history table
cr.execute(
    "CREATE TABLE IF NOT EXISTS accounts(username TEXT,email TEXT,password TEXT,backup_codes TEXT, birth TEXT ,first TEXT , last TEXT,Type TEXT,id INTEGER PRIMARY KEY)"
)

cr.execute('''
    CREATE TABLE IF NOT EXISTS catgory(
        types TEXT
    )
''')
cr.execute(f"SELECT types FROM catgory LIMIT 1")

# Fetch the result
if cr.fetchone() is None:
    cr.execute('''
    INSERT INTO catgory (types) VALUES 
    ('Google'),
    ('Facebook'),
    ('Instagram'),
    ('Riot Games'),
    ('Epic Games'),
    ('Microsoft')
    ''')

id_count_select = cr.execute("SELECT id FROM accounts")
id_count = len(id_count_select.fetchall())
db.commit()
db.close()
print("HERE")
#---------------

