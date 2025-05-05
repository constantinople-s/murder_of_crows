import sqlite3


class SqlProcessor:
    def __init__(self, db_name='zerno.db'):
        self.db_name = db_name
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS Blocks(
                            ID string PRIMARY KEY,
                            view integer, 
                            value integer)
                        ''')
            conn.execute('''CREATE TABLE IF NOT EXISTS Person(
                            id string PRIMARY KEY,
                            name string,
                            birth_year integer,
                            ip_addr string)
                        ''')
            conn.execute('''CREATE TABLE IF NOT EXISTS Votes(
                            ID string,
                            person_id string,
                            PRIMARY KEY(ID, person_id),
                            FOREIGN KEY(person_id) REFERENCES Person(id) ON DELETE CASCADE)
                        ''')
            
    def add_block(self, block):
        with sqlite3.connect(self.db_name) as conn:
            try:
                conn.execute('INSERT INTO Blocks(ID, view, value) VALUES(?, ?, ?)', 
                             (block.id, block.view, block.value))
                conn.commit()
            except sqlite3.IntegrityError as e:
                print(f"Block with ID {block.id} already exists: {e}")

    def get_block(self, block_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Blocks WHERE ID=?', (block_id,))
            block = cursor.fetchone()
            if block:
                return {
                    'ID': block[0],
                    'view': block[1],
                    'value': block[2]
                }
            return None

    def update_block(self, block_id, view, value):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('UPDATE Blocks SET view=?, value=? WHERE ID=?', 
                         (view, value, block_id))
            conn.commit()

    def delete_block(self, block_id):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('DELETE FROM Blocks WHERE ID=?', (block_id,))
            conn.commit()

    def add_vote(self, vote, person_id):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("PRAGMA foreign_keys = ON")
            try:
                conn.execute('INSERT INTO Votes(ID, person_id) VALUES(?, ?)', 
                             (vote, person_id))
                conn.commit()
            except sqlite3.IntegrityError as e:
                print(e)
                
    def get_votes(self, person_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Votes WHERE person_id=?', (person_id,))
            votes = cursor.fetchall()
            return [vote[0] for vote in votes]
        
    def delete_vote(self, vote_id):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('DELETE FROM Votes WHERE ID=?', (vote_id,))
            conn.commit()

    def update_vote(self, vote_id, new_vote):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('PRAGMA foreign_keys = ON')
            try:
                conn.execute('UPDATE Votes SET ID=? WHERE ID=?', 
                             (new_vote, vote_id))
                conn.commit()
            except sqlite3.IntegrityError as e:
                print(f"Reference to non-existent vote ID {vote_id}: {e}")

    def add_person(self, person_id, name, birth_year, ip_addr):
        with sqlite3.connect(self.db_name) as conn:
            try:
                conn.execute('INSERT INTO Person(ID, name, birth_year, ip_addr) VALUES(?, ?, ?, ?)', 
                             (person_id, name, birth_year, ip_addr))
                conn.commit()
            except sqlite3.IntegrityError as e:
                print(f"Person with ID {person_id} already exists: {e}")

    def get_person(self, person_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Person WHERE ID=?', (person_id,))
            person = cursor.fetchone()
            if person:
                return {
                    'ID': person[0],
                    'name': person[1],
                    'birth_year': person[2],
                    'ip_addr': person[3]
                }
            return None
        
    def update_person(self, person_id, name, birth_year, ip_addr):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('UPDATE Person SET name=?, birth_year=?, ip_addr=? WHERE ID=?', 
                         (name, birth_year, ip_addr, person_id))
            conn.commit()

    def delete_person(self, person_id):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('PRAGMA foreign_keys = ON')
            conn.execute('DELETE FROM Person WHERE ID=?', (person_id,))
            conn.commit()