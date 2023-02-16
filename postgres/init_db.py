import os, psycopg2

# Get the database URL from the environment variable
db_url = os.environ['DATABASE_URL']

# Connect to the database
conn = psycopg2.connect(db_url)

# Create a cursor object
cur = conn.cursor()

# Create a new table
cur.execute('CREATE TABLE articles (id serial PRIMARY KEY, title varchar(256))')

# Insert some data into the table
cur.execute('INSERT INTO articles (title) VALUES (%s)', ('First Article',))
cur.execute('INSERT INTO articles (title) VALUES (%s)', ('Second Article',))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
