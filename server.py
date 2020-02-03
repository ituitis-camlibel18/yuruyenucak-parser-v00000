import os


from bottle import Bottle, request, template, route
from pathlib import Path
from socket import gethostname, gethostbyname 


ip_all = {}

def index_page():
    global ip_all
    device_ip = request.headers.get("X-Forwarded-For","127.0.0.1")
    if device_ip in ip_all:
            ip_all[device_ip] +=1
    else:
            ip_all[device_ip] = 1
    one =Path("index1frame.html").read_text()

    two = ''
    for ip, count in ip_all.items():
       two += f'<tr> <th> {ip} </th><th> {count}</th></tr>'
    html = one.format(two)
    return html

def create_app():
    app = Bottle()
    app.route("/", "GET", index_page)
    app.route("/index1.html", "GET", index_page)
    
    return app

    


application = create_app()
application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

    

