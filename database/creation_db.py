mport sqlite3
import pandas as pd

sqlite_file = 'database/creation_garage.sql'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

with open('database/scheduling.sql', 'r') as f:
    sql = f.read()

result = pd.read_sql_query(sql, conn)
print(result)