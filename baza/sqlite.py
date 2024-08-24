import sqlite3

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users(
        full_name TEXT,
        telegram_id INTEGER UNIQUE,
        phone_number TEXT
        );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, telegram_id: int, full_name: str, phone_number: str):
        sql = """
        INSERT INTO Users(telegram_id, full_name, phone_number) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(telegram_id, full_name, phone_number), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def all_users_id(self):
        return self.execute("SELECT telegram_id FROM Users;", fetchall=True)
    
    def get_user(self, telegram_id):
        # self.cursor.execute('''
        #     SELECT * FROM users WHERE telegram_id = ?
        # ''', (telegram_id,))
        # return self.cursor.fetchone()
        sql = "SELECT * FROM users WHERE telegram_id = ?"
        return self.execute(sql, parameters=(telegram_id,), fetchone=True)

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
import sqlite3
from data import config

# class Database:
#     def __init__(self):
#         self.connection = sqlite3.connect(config.DB_PATH)
#         self.cursor = self.connection.cursor()
#         self.create_tables()

#     def create_tables(self):
#         self.cursor.execute('''
#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 telegram_id INTEGER UNIQUE,
#                 first_name TEXT,
#                 username TEXT
#             )
#         ''')
#         self.connection.commit()

#     def add_user(self, telegram_id, first_name, username=None):
#         try:
#             self.cursor.execute('''
#                 INSERT INTO users (telegram_id, first_name, username) VALUES (?, ?, ?)
#             ''', (telegram_id, first_name, username))
#             self.connection.commit()
#         except sqlite3.IntegrityError:
#             pass

#     


#     def count_users(self):
#         self.cursor.execute("SELECT COUNT(*) FROM Users;")
#         return self.cursor.fetchone()
#         # Foydalanuvchilar sonini hisoblash
#         # return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)
#     # def count_users(self):
#     #     self.cursor.execute('''
#     #         SELECT COUNT(*) FROM users
#     #     ''')
#     #     return self.cursor.fetchone()

#     def all_users_id(self):
#         self.cursor.execute("SELECT telegram_id FROM Users;")
#         return self.cursor.fetchall()
#         # Barcha foydalanuvchilar ID larini tanlash
#         # return self.execute("SELECT telegram_id FROM Users;", fetchall=True)
#     # def all_users_id(self):
#     #     self.cursor.execute('''
#     #         SELECT telegram_id FROM users
#     #     ''')
#     #     return self.cursor.fetchall()

#     def close(self):
#         self.connection.close()
        
