import requests
r = requests.get('https://search.incruit.com/list/search.asp?col=job&kw=%C0%CE%BB%E7%C3%D1%B9%AB&psize=60')
print(r.status_code) #코드 뒤에 괄호가 없으면 속성, 괄호가 있으면 함수
