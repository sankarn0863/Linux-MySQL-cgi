#!/usr/bin/python

import cgi, cgitb
import MySQLdb

form = cgi.FieldStorage()

username = form.getvalue('UserName')
count = form.getvalue('country')
number = form.getvalue('num')
email = form.getvalue('mail')
mypass = form.getvalue('MyPass')


db= MySQLdb.connect("localhost","naredlav1","gqsc1d","naredlav1_db") 

myCursor = db.cursor()

sql = "INSERT INTO venu VALUES ('%s','%s','%s','%s','%s');" %(username,count,number,email,mypass)

try:
        myCursor.execute(sql)
        db.commit()
except:
        db.rollback()
db.close()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title> REGISTRATION FORM</title>"
print "</head>"
print "<body>"
print "<h2> REGISTRATION SUCCESSFUL = %s GARU!</h2>" %(username)
print "</body>"
print "</html>"

