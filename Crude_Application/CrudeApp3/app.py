from flask import Flask, render_template, request, redirect, url_for
import sqlite3  # Or your preferred database library

app = Flask(__name__)

# Database connection (modify connection string if needed)
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Sample table creation (replace with your schema)
c.execute('''CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, details TEXT)''')
conn.commit()

@app.route('/')
def index():
    c.execute('SELECT * FROM items')
    data = c.fetchall()  # Fetch all items from database
    return render_template('index.html', items=data)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        details = request.form['details']  # Add details field
        c.execute('INSERT INTO items (name, details) VALUES (?, ?)', (name, details))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        name = request.form['name']
        details = request.form['details']  # Update details field
        c.execute('UPDATE items SET name = ?, details = ? WHERE id = ?', (name, details, id))
        conn.commit()
        return redirect(url_for('index'))
    c.execute('SELECT * FROM items WHERE id = ?', (id,))
    data = c.fetchone()
    return render_template('update.html', item=data)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    c.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
