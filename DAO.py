import sqlite3
import connection as conn

def get_gifts_all(connection):
  try:

    cursor = connection.cursor()
    purchases = []
    query = 'SELECT name, item, price, status FROM purchases'
    cursor.execute(query, ())
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()

    for row in rows:
      purchases.append(dict(zip(columns, row)))

    return purchases


  except Exception as e:
    print(f"An error occurred: {e}")
    return None
  finally:
    cursor.close()


