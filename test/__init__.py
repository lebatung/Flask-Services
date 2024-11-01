import pyodbc

try:
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost,1433;'
        'DATABASE=ATTP_laptrinh2022;'
        'UID=sa;'
        'PWD=123456'
    )
    print("Kết nối thành công!")
except pyodbc.Error as e:
    print("Không thể kết nối:", e)
