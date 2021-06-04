#!/usr/bin/python

import cgi, cgitb
import MySQLdb


myForm = cgi.FieldStorage()

nick = myForm.getvalue('UserName')
secret = myForm.getvalue('MyPass')

db= MySQLdb.connect("localhost","naredlav1","gqsc1d","naredlav1_db") 

myCursor = db.cursor()

sql = "SELECT passcode from venu WHERE userid = '%s' "%(nick)

try:
  myCursor.execute(sql)
  output = myCursor.fetchone()
  for row in output:
     sWord  = row
except:
  print "Error: unable to fetch data"
db.close()

if secret == sWord:

  print "Content-type:text/html\r\n\r\n"
  print "<html>"
  print "<head>"
  print "<title>Confirm</title>"
  print "</head>"
  print "<body>"
  print "<h2>Good to see you again %s !<h2>"%(nick)
  print "<h4>Do you like to continue with the Bookings?<h4>"
  print "</body>"
  print "</html>"

else:
  print "Content-type:text/html\r\n\r\n"
  print "<h1>INVALID INPUT</h1>"
  print "<h3>Classfied empty//Wrong Username or Password</h3>"
  print "<h5>REGISTER AND TRY AGAIN</h5>"
  print "<h6>THANK YOU...OOPS SORRY :-(</h6>"
  print "<html>"
