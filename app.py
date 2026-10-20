#라우팅하는 방법
from flask import Flask, render_template, request
from scrapper import search_incruit

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/hi")
# def hi():
#    return "hi 안녕하세연 만나서 반갑읍니다."
@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    jobs = search_incruit()
#    data = "19기 어플리케이션 과정"
#    return render_template("search.html", data = data)
#이렇게 실행하면 19기 어쩌고 나온 바로 뒤에 잡서치 검색결과입니다. 일케 나옴
    return render_template("search.html", keyword = keyword, jobs = jobs) #서치.html에 키워드를 같이 보내는 것임.

if __name__ == '__main__':
    app.run(debug=True)
