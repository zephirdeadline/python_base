#!/usr/bin/python3
import cgi

print("Content-type: text/html; charset=utf-8\n")

html = """<!Doctype html>
<head>
<meta charset="utf-8">
<title>Ma page web</title>
</head>
<body>
    <h1>Page web python CGI</h1>
    
    <form method="POST" action="result.py">
        <p><input type="text" name="username">
        <input type="submit" value="send"></p>  
    </form>
</body>
</html>
"""

print(html)