import requests #리퀘스트라는 내부 기능을 불러옴.
keyword = "인사총무"
pages = 5
page = pages * 60
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&psize=60&startno={page}" 
    #인크루트 공고페이지 긁어오는데 kw=키워드인데 내 키워드를 위에서 변수 설정 해줬으니 중괄호하고 키워드 넣어주고, 페이지도 넣어줌.
jobs = []
# 변수들을 설정하기.
def search_incruit():

    for page in range(pages): #1페이지만 할 것이 아니기 때문에 저 페이지를 페이지스에 세팅된 값(5니까 0,1,2,3,4)까지 반복해주는거임.
        r = requests.get(url)#원래 url을 다 넣어야 되는데 그러면 복잡하고, 각 페이지별로 다 따로 넣어야 하니까 생노가다라서 변수 넣어주면 한번에 해결 가능함.
        '''
        https://search.incruit.com/list/search.asp 여기까지가 URL임.
        col 이라는 파라미터와 kw라는 파라미터가 &으로 묶여있음.
        '''
        #print(r.status_code) #코드 뒤에 괄호가 없으면 속성, 괄호가 있으면 함수
        #print(r.text)
        #특정한 데이터를 빠르고 편하게 가지고 올 수 있는 뷰티풀 수프 설치
        from bs4 import BeautifulSoup
        # 프롬 뒤에는 모듈(파일), 임포트 뒤에는 함수를 적음.
        soup = BeautifulSoup(r.text, "html.parser") # .text는 긁어온 값에서 텍스트만 보여주는 속성임.
        #print(soup.prettify())
        lis = soup.find_all("li", class_ = "c_col")
        #print(lis) #공고문 저거 다 찾아서 표시해라라는 뜻
        #print(len(lis)) 몇개인지 봄.
        #jobs = [] #얘는 for page 안에 있으면 초기화가 되기 때문에 for문 위로 빼야 됨.
        for li in lis:
            try: #시도해보라는 거
                company = li.find("a", class_ = "cpname").text # a태그는 우리가 마우스 클릭하기 전에 손모양으로 바뀌면서 클릭할 수 있게 되는게 a임.
                title  = li.find("div", class_ = "cell_mid").find("a").text
                location = li.find("div", class_ = "cl_md").find_all("span")[0].text
                #파인드올해서 스팬 긁어오면 여러 정보가 나오는데 첫번째 정보만 필요하니까[0] 하면 스팬 필요한거 스팬 이렇게 나오는데 .텍스트하면 필요한거만 뜸.
                link = li.find("div", class_ = "cell_mid").find("a").get("href")
                #하나를 찾는 메소드 find , 다 찾는거 find_all / .text는 내가 필요한것만 보여줌.
                #print(company) #회사명
                #print(title) # 공고제목
                #print(location) # 업체 위치
                #print(link) # 공고링크
                job_data = {
                    "company" : company,
                    "title" : title,
                    "location" : location,
                    "link" : link
                }
                jobs.append(job_data)

            except: #시도 해보고 아니면
                pass #넘겨라.

        #print(jobs)
        #print(len(jobs))
        print(f"{page + 1} 크롤링 중...")
    return jobs