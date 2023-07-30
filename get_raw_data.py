import os
import time
from datetime import datetime, timedelta

import mysql.connector
import requests


STOCKS = ["IBM", "AAPL"]
API_KEY = os.getenv("API_KEY")
db_conf = {
    "host": os.getenv("DB_HOST"),
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE"),
}
db_conn = None


def get_records(stock: str):
    # Initial records
    records = []
    # Get current date
    curr = datetime.today()
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={API_KEY}"
    res = requests.get(url)
    # If API status_code is not 200, end the script
    if res.status_code != 200:
        raise Exception(f"API error: {res.content}")
    data = res.json()
    if data.get("Time Series (Daily)"):
        for k, v in data["Time Series (Daily)"].items():
            _date = datetime.strptime(k, "%Y-%m-%d")
            diff = curr - _date
            # Check if the date is within 2 weeks
            if diff <= timedelta(days=14):
                records.append(
                    {
                        "symbol": stock,
                        "date": _date.strftime("%Y-%m-%d"),
                        "open_price": v.get("1. open", "0.0000")[:-2],
                        "close_price": v.get("4. close", "0.0000")[:-2],
                        "volume": v.get("5. volume", "0"),
                    }
                )
    return records


def insert_db(data: list):
    # Get connection
    conn = _connect()
    # Check database connection
    if conn is None:
        raise Exception("Can not connect to database!")
    # Check if data is empty
    if len(data) == 0:
        return "No data"
    _cursor = conn.cursor()
    for d in data:
        # Skip data without symbol or date
        if not d.get("symbol") or not d.get("date"):
            continue
        table = "financial_data"
        op = d["open_price"]
        cp = d["close_price"]
        v = d["volume"]
        values = (d["symbol"], d["date"], op, cp, v)
        query = f"INSERT INTO {table} (symbol, date, open_price, close_price, volume) VALUES {values} ON DUPLICATE KEY UPDATE open_price={op}, close_price={cp}, volume={v}"
        try:
            _cursor.execute(query)
            conn.commit()
        except Exception as e:
            print("Insert failed: ", e)
    _cursor.close()
    return "Finished"


def _connect():
    global db_conn
    # If no connection or connection is break, re-connect
    if db_conn is None or not db_conn.is_connected():
        db_conn = mysql.connector.connect(**db_conf)
    return db_conn


def wait_for_db():
    while True:
        try:
            _ = _connect()
            return
        except Exception:
            print("Database not ready yet, waiting...")
            time.sleep(1)


if __name__ == "__main__":
    wait_for_db()
    for s in STOCKS:
        # Get stock records within 2 weeks
        records = get_records(s)
        # Insert the records into database
        result = insert_db(records)
        print(f"{s} {result}")
