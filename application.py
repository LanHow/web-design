from flask import Flask, render_template

application = Flask(__name__)

def index():
    return render_template('index.html')

application.add_url_rule('/', 'index', (lambda: index()))

if __name__ == '__main__':
#    application.debug = True
    application.run()
