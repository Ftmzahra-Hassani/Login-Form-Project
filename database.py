import sqlite3
con = sqlite3.connect('D:/exam project/mydata.db')
cur = con.cursor()

def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY KEY,fname TEXT ,lname TEXT ,email TEXT , password TEXT)')
    con.commit()

def sign_up(fname , lname , email , password):
    cur.execute('INSERT INTO login(id , fname , lname , email, password)VALUES(NULL , ?,?,?,?)',(fname , lname , email , password))
    con.commit()
    
def sign_in(email,password):
       cur.execute('SELECT * FROM login WHERE email = ? and password =?',(email , password))
       return cur.fetchall()
       
create_table()

