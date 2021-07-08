import sqlite3

def connect():
    connectDB=sqlite3.connect("books.db")
    cur=connectDB.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connectDB.commit()
    connectDB.close()


def insert(title,author,year, isbn):
    connectDB=sqlite3.connect("books.db")
    cur=connectDB.cursor()
    cur.execute("INSERT INTO book VALUES(NULL ,?,?,?,?)",(title,author,year,isbn))
    connectDB.commit()
    connectDB.close()

def view():
    connectDB=sqlite3.connect("books.db")
    cur=connectDB.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    connectDB.close()
    return rows

def search(title="",author="",year="",isbn=""):
    connectDB=sqlite3.connect("books.db")
    cur=connectDB.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    connectDB.close()
    return rows


def delete(id):
    connectDB=sqlite3.connect("books.db")
    cur=connectDB.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    connectDB.commit()
    connectDB.close()


def update(id,title,author,year,isbn):
    connectDB=sqlite3.connect("books.db")
    cur=connectDB.cursor()
    cur.execute("UPDATE book SET title=?, author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id))
    connectDB.commit()
    connectDB.close()

connect()