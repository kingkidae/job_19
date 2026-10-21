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
    jobs = search_incruit(keyword)#스크래퍼에서 긁어온 정보를 반환한 변수
#    data = "19기 어플리케이션 과정"
#    return render_template("search.html", data = data)
#이렇게 실행하면 19기 어쩌고 나온 바로 뒤에 잡서치 검색결과입니다. 일케 나옴
    return render_template("search.html", keyword = keyword, jobs = enumerate(jobs)) #서치.html에 키워드를 같이 보내는 것임.

if __name__ == '__main__':
    app.run(debug=True) #디버그 트루를 하면 코딩을 하고 수정하고 저장하면 자동으로 업데이트해줌.
#여기서 서버가 돌아가는 것임.
#http://127.0.0.1:5000 여기로 들어갈 수 있고, localhst:5000으로도 페이지에 들어갈 수 있음.