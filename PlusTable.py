import sqlite3
class PlusTable():
    def __init__(self):
        self.con = sqlite3.connect("plusbase.db")
        self.cur = self.con.cursor()
    def insert(self,summand1,summand2,result):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS PLUS_TABLE(summand1 INT, summand2 INT, result INT)""")
        self.cur.execute(f"""INSERT INTO PLUS_TABLE(summand1,summand2,result) values({summand1},{summand2},{result});""")
    def read(self):
        self.cur.execute("""SELECT * FROM PLUS_TABLE""")
        self.office = self.cur.fetchall()
        self.con.commit()
        return self.office[-1]
if __name__ == "__main__":
    obj = PlusTable()
    run = ""
    while True:
        run = input("run or exit")
        if run == "run":
            summand1 = int(input())
            summand2 = int(input())
            result = summand1 + summand2
            obj.insert(summand1,summand2,result)
    
        else:
            print(obj.read())
            break
    