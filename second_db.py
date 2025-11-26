from kivy.lang import Builder
from kivymd.app import MDApp
#import sqlite3
import psycopg2



class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Blue"

		# Create Database Or Connect To One
		#conn = sqlite3.connect('first_db.db')
		
		# Define DB Stuff
		conn = psycopg2.connect(
			host = "ccu6unqr99fgui.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com", 
			user = "u5n26bf6f6ifpr",
			password = "pc9052ef292d5046cdf83fb6731101b7f66209a03709ded41f53a4028108d6a4d",
			dbname = "d3o7isrekq6ci5",
			port="5432"
			)

		# Create A Cursor
		c = conn.cursor()

		# Create an actual database

		# Check to see if database was created
		#c.execute("SHOW DATABASES")
		#for db in c:
		#	print(db)



		# Create A Table
		c.execute("""CREATE TABLE if not exists customers
			(name TEXT);
		 """)

		# Check to see if table created
		#c.execute("SELECT * FROM customers")
		#print(c.description)



		# Commit our changes
		conn.commit()

		# Close our connection
		conn.close()

		return Builder.load_file('second_db.kv')



	def submit(self):
		# Create Database Or Connect To One
		#conn = sqlite3.connect('first_db.db')
		conn = psycopg2.connect(
			host = "ccu6unqr99fgui.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com", 
			user = "u5n26bf6f6ifpr",
			password = "pc9052ef292d5046cdf83fb6731101b7f66209a03709ded41f53a4028108d6a4d",
			dbname = "d3o7isrekq6ci5",
			port="5432"
			)

		# Create A Cursor
		c = conn.cursor()

		

		# Add A Record
		sql_command = "INSERT INTO customers (name) VALUES (%s)"
		values = (self.root.ids.word_input.text,)
		
		# Execute SQL Command
		c.execute(sql_command, values)	
		

		# Add a little message
		self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

		# Clear the input box
		
		self.root.ids.word_input.text = ''


		# Commit our changes
		conn.commit()

		# Close our connection
		conn.close()

		

	def show_records(self):
		# Create Database Or Connect To One
		#conn = sqlite3.connect('first_db.db')
		conn = psycopg2.connect(
			host = "ccu6unqr99fgui.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com", 
			user = "u5n26bf6f6ifpr",
			password = "pc9052ef292d5046cdf83fb6731101b7f66209a03709ded41f53a4028108d6a4d",
			dbname = "d3o7isrekq6ci5",
			port="5432"
			)

		# Create A Cursor
		c = conn.cursor()

		
		# Grab records from database
		c.execute("SELECT * FROM customers")
		records = c.fetchall()

		word = ''
		# Loop thru records
		for record in records:
			word = f'{word}\n{record[0]}'
			self.root.ids.word_label.text = f'{word}'

		# Commit our changes
		conn.commit()

		# Close our connection
		conn.close()



MainApp().run()
