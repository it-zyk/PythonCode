import time


def login():
    return "welcome to our webseite--------------time %s " % str(time.ctime())


def register():
    return "welcome to register"


def profile():
    return "-------------profile-------------------"


def application():
    if file_name == "/login.py":
        login()
    elif file_name == "/register.py":
        register()
    
    else:
        return "not found your page"


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    
    file_name = environ["PATH_INFO"]
    if file_name == "/index.py":
        return login()
    elif file_name == "/profile.py":
        return profile()
    else:
        return "Not found your page"

    return 'Hello World! 我爱你中国'
