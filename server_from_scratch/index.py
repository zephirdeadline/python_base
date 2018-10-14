#!/usr/bin/python3
import cgi
import http.cookies
import datetime
import os
import sys
import codecs

"""set utf8 for print function if needed"""
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


""" Create a cookie """
expiration = datetime.datetime.now() + datetime.timedelta(days=365)
expiration = expiration.strftime("%a, %d-%b-%Y %H-%M-%S")

my_cookie = http.cookies.SimpleCookie()
my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["expires"] = expiration
my_cookie["pref_lang"]["httponly"] = True
print(my_cookie.output())
print("Content-type: text/html; charset=utf-8\n")

html = """<!Doctype html>
<head>
<meta charset="utf-8">
<title>Ma page web</title>
</head>
<body>
    <h1>Page web python CGI</h1>"""
print(html)
try:
    user_cookies = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print(f'language ééééé: {user_cookies["pref_lang"].value}')
except:
    pass

html = """
    
    <form method="POST" action="result.py">
        <p><input type="text" name="username">
        <input type="submit" value="send"></p>  
    </form>
</body>
</html>
"""

print(html)