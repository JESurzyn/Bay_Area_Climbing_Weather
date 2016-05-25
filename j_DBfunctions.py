import sqlite3

#this file will create the database
def CreateDB():
	conn = sqlite3.connect('users_data.db')
	cursor = conn.cursor()
	sql = '''create table weather_users (
		name text, 
		temperature real,
		humidity real)'''
	cursor.execute(sql)
	cursor.close()

def nameQuery():
	conn = sqlite3.connect('users_data.db')
	cursor = conn.cursor()
	sql2 = '''select name
	from weather_users'''
	results = cursor.execute(sql2)
	current_users = results.fetchall()
	return current_users
	cursor.close()


def saveUser(user):
	conn = sqlite3.connect('users_data.db')
	cursor = conn.cursor()
	sql3 = '''insert into weather_users (name, temperature, humidity)
	values (:nam, :temp, :hum)'''
	cursor.execute(sql3, {'nam':user.name, 'temp':user.temp, 'hum':user.humid})
	conn.commit()
	cursor.close()

def userQuery(option):
	conn = sqlite3.connect('users_data.db')
	cursor = conn.cursor()
	sql4 = '''select *
	from weather_users where name = :bla'''
	results = cursor.execute(sql4, {'bla':option})
	selected_user = results.fetchall()
	return selected_user
	cursor.close()

def deleteUser(option):
	conn = sqlite3.connect('users_data.db')
	cursor = conn.cursor()
	sql5 = '''delete from weather_users
	where name = :del'''
	cursor.execute(sql5, {'del':option})
	conn.commit()
	cursor.close()