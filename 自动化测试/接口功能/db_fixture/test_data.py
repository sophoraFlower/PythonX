import sys
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB



# create data
datas = {
    'data1': [
        {},
        {},
    ],
    'data2': [
        {},
        {},
    ],
}


# Insert table datas
def init_data():
    db = DB()
    for table, data in datas.items():
        if table:
            db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()

if __name__ == '__main__':
    init_data()
