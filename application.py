from flask import Flask, render_template

application = Flask(__name__)

def index():
    return render_template('index.html')

def news():
    return render_template('news.html')

def jiofeng():
    return render_template('九份.html')

def zoo():
    return render_template('動物園.html')

def daxi():
    return render_template('大溪老街.html')

def hsinju():
    return render_template('新竹.html')

def taoyuan():
    return render_template('桃園.html')

def doublepei():
    return render_template('雙北.html')

def longshantemple():
    return render_template('龍山寺.html')

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
#    application.debug = True
    application.run()