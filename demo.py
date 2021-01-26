import psycopg2

conn = psycopg2.connect('dbname = mydb user=postgres')

cursor = connection.cursor()

cursor.execute('''
	CREATE TABLE table2(
	id INTEGER PRIMARY KEY,
	completed BOOLEAN NOT NULL DEFAULT False
	);
	''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')

connection.commit()

connection.close()
cursor.close()