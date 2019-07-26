import sqlite3



path = r"C:\Users\Student\Downloads"
conn = sqlite3.connect(path)

rows = conn.execute("""
SELECT t.name , t.milliseconds/60000 ,t.artists  FROM tracks as t
JOIN albums as a on t.albumid = a.albumid
join artists as a on a.artistid = s.artistid
""")