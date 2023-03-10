from flask import Flask, request
import sqlite3
import time

app = Flask(__name__)

# Connect to the database
conn = sqlite3.connect('email_tracker.db')
c = conn.cursor()

# Create the email tracking table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS email_tracking
             (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, time INTEGER, count INTEGER)''')
conn.commit()

# Close the database connection
conn.close()

# Endpoint for tracking email opens
@app.route('/email-open', methods=['GET'])
def track_email_open():
    # Get the email parameter from the query string
    email = request.args.get('email')
    
    # Get the current timestamp
    timestamp = int(time.time())
    
    # Connect to the database
    conn = sqlite3.connect('email_tracker.db')
    c = conn.cursor()
    
    # Check if the email has been tracked before
    c.execute('SELECT count FROM email_tracking WHERE email=?', (email,))
    row = c.fetchone()
    if row is None:
        # Insert a new row for the email
        c.execute('INSERT INTO email_tracking (email, time, count) VALUES (?, ?, ?)', (email, timestamp, 1))
    else:
        # Update the existing row
        count = row[0] + 1
        c.execute('UPDATE email_tracking SET time=?, count=? WHERE email=?', (timestamp, count, email))
    
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()
    
    # Return a 1x1 transparent GIF image
    return ('', 204, {'Content-Type': 'image/gif', 'Content-Length': '42'})

if __name__ == '__main__':
    app.run(debug=True)
