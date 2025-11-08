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
