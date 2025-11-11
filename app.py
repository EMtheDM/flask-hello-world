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


@app.route("/db_create")
def db_create():
    try:
        conn = psycopg2.connect(
            "postgresql://emthedm_lab10db_user:YfR3U6na5R67hlYC4Vdmf40iYGbCHrAC@dpg-d47mupi4d50c7389sdc0-a/emthedm_lab10db")
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Basketball(
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
        conn = psycopg2.connect(
            "postgresql://emthedm_lab10db_user:YfR3U6na5R67hlYC4Vdmf40iYGbCHrAC@dpg-d47mupi4d50c7389sdc0-a/emthedm_lab10db")
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


@app.route("/db_select")
def db_select():
    try:
        conn = psycopg2.connect(
            "postgresql://emthedm_lab10db_user:YfR3U6na5R67hlYC4Vdmf40iYGbCHrAC@dpg-d47mupi4d50c7389sdc0-a/emthedm_lab10db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM Basketball;')
        records = cur.fetchall()
        conn.close()

        response = "<h2>Basketball Table Data</h2>"
        response += "<table border='1' style='border-collapse: collapse; padding: 8px;'>"
        response += "<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"

        for row in records:
            response += "<tr>"
            for cell in row:
                response += f"<td style='padding: 6px 12px;'>{cell}</td>"
            response += "</tr>"

        response += "</table>"
        return response

    except Exception as e:
        return f"Error selecting data: {e}"


@app.route("/db_drop")
def db_drop():
    try:
        conn = psycopg2.connect(
            "postgresql://emthedm_lab10db_user:YfR3U6na5R67hlYC4Vdmf40iYGbCHrAC@dpg-d47mupi4d50c7389sdc0-a/emthedm_lab10db")
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS Basketball;')
        conn.commit()
        conn.close()
        return "Basketball table dropped successfully!"
    except Exception as e:
        return f"Error dropping table: {e}"
