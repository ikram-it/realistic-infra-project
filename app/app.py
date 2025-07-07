from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# Get database connection string from environment variable
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost:5432/mydatabase')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/')
def hello():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1;') # Simple query to test DB connection
        db_status = "Database connection successful!"
        cur.close()
        conn.close()
    except Exception as e:
        db_status = f"Database connection failed: {e}"

    return f"<h1>Hello from Flask App!</h1><p>{db_status}</p>"

@app.route('/health')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)