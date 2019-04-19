from flask import Flask, render_template

application = Flask(__name__)

def index():
    return render_template('index.html')

def news():
    return render_template('news.html')

def jiofeng():
    return render_template('jiofeng.html')

def zoo():
    return render_template('zoo.html')

def daxi():
    return render_template('daxi.html')

def hsinju():
    return render_template('hsinju.html')

def taoyuan():
    return render_template('taoyuan.html')

def doublepei():
    return render_template('doublepei.html')

def longshantemple():
    return render_template('longshantemple.html')

application.add_url_rule('/', view_func=index)
application.add_url_rule('/news', view_func=news)
application.add_url_rule('/jiofeng', view_func=jiofeng)
application.add_url_rule('/zoo', view_func=zoo)
application.add_url_rule('/daxi', view_func=daxi)
application.add_url_rule('/hsinju', view_func=hsinju)
application.add_url_rule('/taoyuan', view_func=taoyuan)
application.add_url_rule('/doublepei', view_func=doublepei)
application.add_url_rule('/longshantemple', view_func=longshantemple)

if __name__ == '__main__':
    application.run()
