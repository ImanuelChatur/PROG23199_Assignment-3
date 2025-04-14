# Assignment: 3
# Course: PROG23199
# Submission date: 2025-04-13
# Name: Imanuel Chatur
# Sheridan ID: 991637637
# Instructors name: Syed Tanbeer
import sqlite3


class ZooManager:
    """
    Description:
        Database manager for the Zoo

    Methods:
        initialize_db():
            Executes table creation script

        insert_animal(name, hungry_count, food_consumed):
            inserts animal into the database

        get_animals():
            returns animals from database

        close_db():
            terminates connection
    """

    zoo_db = "ZooInfo_Imanuel.db"

    def __init__(self):
        try:
            self.conn = sqlite3.connect(ZooManager.zoo_db)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)

        self.initialize_db()

    def initialize_db(self):
        """
        Initialize db:
            Drops tables then creates the zoo table
        """
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
        """

        :param name:
        :param hungry_count:
        :param food_consumed:
        :return:
        """
        query = ("INSERT INTO ZooInfo_IMANUEL"
                 "(animal_name, hungry_count, total_food_consumed) VALUES (?, ?, ?)")
        self.cursor.execute(query, (name, hungry_count, food_consumed))

    def get_animals(self):
        """
        get_animals:
            returns animals from SQL query
        """
        sql = "SELECT * FROM ZooInfo_Imanuel"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close_db(self):
        self.cursor.close()
        self.conn.close()
