#!/usr/bin/python

import cgi, cgitb
import MySQLdb

form = cgi.FieldStorage()

username = form.getvalue('UserName')
count = form.getvalue('country')
number = form.getvalue('num')
email = form.getvalue('mail')
mypass = form.getvalue('MyPass')
salary = form.getvalue('sal')

db= MySQLdb.connect("localhost","naredlav1","gqsc1d","naredlav1_db")

myCursor = db.cursor()

sql = "INSERT INTO naredla VALUES ('%s','%s','%s','%s','%s','%s');" %(username,count,number,email,mypass,salary)

try:
        myCursor.execute(sql)
        db.commit()
except:
        db.rollback()
db.close()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title> ECONOMY REGISTRATION SUCCESSFUL </title>"
print "</head>"
print "<body>"
print "<h2> ECONOMY REGISTRATION SUCCESSFULL</h2>" 
print "</body>"
print "</html>"