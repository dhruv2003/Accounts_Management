import sqlite3

class database:
  def __init__(self,db):
    self.connection=sqlite3.connect(db)
    self.current=self.connection.cursor()
    self.current.execute(
      "CREATE TABLE IF NOT EXISTS expense_record (item_name text, item_price float, purchase_date date)")
    self.connection.commit()
    
    
  def fetch_record(self,query):
    self.current.execute(query)
    rows=self.current.fetchall()
    return rows
  
  def insertRecord(self, item_name, item_price, purchase_date):
        self.cur.execute("INSERT INTO expense_record VALUES (?, ?, ?)",
                        (item_name, item_price, purchase_date))
        self.conn.commit()
        
        
  def removeRecord(self, rwid):
        self.cur.execute("DELETE FROM expense_record WHERE rowid=?", (rwid,))
        self.conn.commit()
        
  def updateRecord(self, item_name, item_price, purchase_date, rid):
        self.cur.execute("UPDATE expense_record SET item_name = ?, item_price = ?, purchase_date = ? WHERE rowid = ?",
                        (item_name, item_price, purchase_date, rid))
        self.conn.commit()
        
        
  def __dl__(self):
    self.connection.close()