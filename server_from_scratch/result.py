#!/usr/bin/python3
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

"""
No difference between POST and GET
"""
if form.getvalue("username"):
    username = form.getvalue("username")

print("Content-type: text/html; charset=utf-8\n")

html = """<!Doctype html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
"""

print(html)

print(f"Bonjour {username} !")

html = """
</body>
</html>
"""

print(html)