from tools import *

@app.route('/')
def page_test():
    return '0'



if __name__ == '__main__':
    app.run(host,port)
