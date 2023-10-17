CREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users 
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),
        FIRSTNAME CHAR(50),
        LASTNAME CHAR(50),
        UNIQUE (TELEGRAM_ID)
        )
"""

INSERT_USER_QUERY = """
INSERT INTO telegram_users VALUES(?,?,?,?,?)
"""