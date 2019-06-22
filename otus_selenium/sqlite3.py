import sqlite3


# def sqlite3_mas():
def sqlite3_mas(log):
    # log = 'hello'
    conn = sqlite3.connect('/home/yury/maslov2.db')
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE Logs (logs char)')
    cursor.execute("INSERT INTO Logs (logs) VALUES (?)", (log,))

    conn.commit()

    # cursor.execute('SELECT * FROM Logs')
    # result = cursor.fetchall()
    # print(result)

    conn.close()


# sqlite3_mas()
