import sqlite3

class ZooManager:
    zoo_db = "ZooInfo_Imanuel.db"

    def __init__(self):
        try:
            self.conn = sqlite3.connect(ZooManager.zoo_db)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)

        self.initialize_db()

    def initialize_db(self):
        self.cursor.executescript("""
        DROP TABLE IF EXISTS ZooInfo_Imanuel;
        CREATE TABLE "ZooInfo_Imanuel"(
            "animal_id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "animal_name" VARCHAR(20),
            "hungry_count" INT,
            "total_food_consumed" INT
        );
        """)

        self.conn.commit()

    def insert_animal(self, name, hungry_count, food_consumed):
        query = "INSERT INTO ZooInfo_IMANUEL(animal_name, hungry_count, total_food_consumed) VALUES (?, ?, ?)"
        self.cursor.execute(query, (name, hungry_count, food_consumed))

    def get_animals(self):
        sql = "SELECT * FROM ZooInfo_Imanuel"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close_db(self):
        self.cursor.close()
        self.conn.close()