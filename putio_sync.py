#!/usr/bin/env python

import sqlite3
import putio
import datetime
import yaml

# Load config
config_file = open('config.yml', 'r')
config = yaml.load(config_file.read())
config_file.close()


print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Starting..."
conn = sqlite3.connect(config['db']['path'])
c = conn.cursor()
c.execute("SELECT id FROM downloads")
existing =  [i[0] for i in c.fetchall()]

c.execute("SELECT id FROM ignored")
ignored =  [i[0] for i in c.fetchall()]

helper = putio.AuthHelper(config['putio']['client_id'], config['putio']['client_secret'], config['putio']['callback_url'], type='token')
client = putio.Client(config['putio']['oauth_token'])
files = client.File.list()

for file in files:
	if not file.id in existing and not file.id in ignored:
		print "Downloading " + file.name + "..."
		file.download(config['download']['path'])
		c.execute("INSERT INTO downloads VALUES (?,?)", (file.id, file.name))
		conn.commit()
		print "Done."

conn.close()
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " done."
