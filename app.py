import psycopg2
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World from Eric Martin in 3308"


@app.route('/db_test')
def db_test():
    try:
        conn = psycopg2.connect(
            "postgresql://emthedm_lab10db_user:YfR3U6na5R67hlYC4Vdmf40iYGbCHrAC@dpg-d47mupi4d50c7389sdc0-a/emthedm_lab10db")
        conn.close()
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {e}"


@app.route('/db_create')
def db_create():
    try:
        conn = psycopg2.connect(
            "postgresql://emthedm_lab10db_user:YfR3U6na5R67hlYC4Vdmf40iYGbCHrAC@dpg-d47mupi4d50c7389sdc0-a/emthedm_lab10db")
        cur = conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS test_table (
                First VARCHAR(255),
                Last VARCHAR(255),
                City VARCHAR(255),
                Name VARCHAR(255),
                Number INT
                );
        ''')
        conn.commit()
        conn.close()
        return "Basketball table created successfully!"
    except Exception as e:
        return f"Error creating table: {e}"


@app.route("/db_insert")
def db_insert():
    try:
        conn = psycopg2.connect("postgresql://emthedm_lab10db_user:YfR3U6na5R67hlYC4Vdmf40iYGbCHrAC@dpg-d47mupi4d50c7389sdc0-a/emthedm_lab10db")
        cur = conn.cursor()

        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
            ('Eric', 'Martin', 'CU Boulder', 'Buffs', 3308);
        ''')

        conn.commit()
        conn.close()
        return "Basketball table populated successfully!"
    except Exception as e:
        return f"Error inserting data: {e}"
