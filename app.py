import connection as conn
import DAO as content
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def display_purchases():
  try:
    connection = conn.initConnection()
    purchases_data = content.get_gifts_all(connection)
    return render_template('index.html', purchases=purchases_data)
  except Exception as e:
    return '<font color="red"><h1> Ошибка: '+str(e)+'</h1></font>'


if __name__ == '__main__':
  app.run(host='0.0.0.0')
