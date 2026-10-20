import requests
keyword = "인사총무"
pages = 5
page = pages * 60
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&psize=60&startno={page}"
jobs = []

def search_incruit():

    for page in range(pages):
        r = requests.get(url)
        '''
        https://search.incruit.com/list/search.asp 여기까지가 URL임.
        col 이라는 파라미터와 kw라는 파라미터가 &으로 묶여있음.
        '''
        #print(r.status_code) #코드 뒤에 괄호가 없으면 속성, 괄호가 있으면 함수
        #print(r.text)
        #특정한 데이터를 빠르고 편하게 가지고 올 수 있는 뷰티풀 수프 설치
        from bs4 import BeautifulSoup
        # 프롬 뒤에는 모듈(파일), 임포트 뒤에는 함수를 적음.
        soup = BeautifulSoup(r.text, "html.parser")
        #print(soup.prettify())
        lis = soup.find_all("li", class_ = "c_col")
        #print(lis) #공고문 저거 다 찾아서 표시해라라는 뜻
        #print(len(lis)) 몇개인지 봄.
        #jobs = [] #얘는 for page 안에 있으면 초기화가 되기 때문에 for문 위로 빼야 됨.
        for li in lis:
            try:
                company = li.find("a", class_ = "cpname").text # a태그는 우리가 마우스 클릭하기 전에 손모양으로 바뀌면서 클릭할 수 있게 되는게 a임.
                title  = li.find("div", class_ = "cell_mid").find("a").text
                location = li.find("div", class_ = "cl_md").find_all("span")[0].text
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

            except:
                pass

        #print(jobs)
        #print(len(jobs))
        print(f"{page + 1} 크롤링 중...")
    return jobs