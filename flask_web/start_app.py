from flask import Flask, render_template

app = Flask(__name__) #app 객체 생성

@app.route('/') # 127.0.0.1:5000/
def index():
    return render_template('index.html')   # html 페이지 보내기

@app.route('/season')
def get_season():
    season = '봄'
    seasonlist = ['봄', '여름', '가을', '겨울']
    return render_template(
        'season.html',
        season = season,
        seasons = seasonlist
    )
# request(요청) - GET 방식
@app.route('/loopindex', methods = ['GET'])
def loopindex():
    items = ['a', 'b', 'c', 'd']
    return render_template('loopindex.html', items=items)

app.run()