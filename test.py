import threading
from tkinter import *
import sqlite3
from flask import Flask, render_template_string
from wtforms import SelectField
from flask_wtf import FlaskForm
import webbrowser

flask_app = Flask(__name__)
flask_app.secret_key = 'SHH!'


def prepare_data():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE foo
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          bar TEXT)''')

    sql = 'INSERT INTO foo (bar) values (?)'

    for i in range(5):
        cursor.execute(sql, (i + 1,))
    return (cursor)


def process_data(cursor):
    cursor.execute('SELECT * from foo')
    data = list()
    for row in cursor.fetchall():
        data.append(row)

    return (data)


def show_data(parent, data):
    listbox = Listbox(parent)
    listbox.pack()
    for row in data:
        listbox.insert(END, row[0])


class TkApp:
    def __init__(self, master):
        cursor = prepare_data()
        data_processed = process_data(cursor)
        show_data(master, data_processed)
        self.button = Button(master, text="Show in webbrowser",
                             command=self.btn_callback)
        self.button.pack()

    def btn_callback(self):
        webbrowser.open("http://localhost:5001")


class FlaskMyForm(FlaskForm):
    select_field = SelectField('Select', choices=[('1', '1')])


@flask_app.route('/', methods=['POST', 'GET'])
def flask_index():
    cursor = prepare_data()
    data_processed = process_data(cursor)
    form = FlaskMyForm()
    form.select_field.choices = data_processed
    html = """
    <html>
    <form action="" method="post">
    <b>OK</b>
    {{form.select_field}}
    </form>
    </html>
    """
    return render_template_string(html, form=form)


def flask_main():
    flask_app.run(debug=False, host="localhost", port=5001)


def tk_main():
    root = Tk()
    app = TkApp(root)
    root.mainloop()


if __name__ == "__main__":
    flask_thread = threading.Thread(target=flask_main)
    flask_thread.daemon = True
    flask_thread.start()
    tk_main()
