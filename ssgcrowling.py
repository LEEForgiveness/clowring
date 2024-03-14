import requests
from bs4 import BeautifulSoup

def crawl_realtime_search():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = 'https://www.ssg.com/item/itemView.ssg?itemId=0000008333648&siteNo=6001&salestrNo=2037'
    response = requests.get(url, headers= headers)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # 원하는 정보를 포함한 HTML 태그를 찾습니다.
        # 예를 들어, 네이버의 실시간 검색어는 <span class="ah_k"> 태그에 있습니다.
        # search_keywords = soup.find('span', class_='mndtl_prdtit_name')
        # prices = soup.find_all('span', class_='text-orange')
        print(soup.find('span', class_='cdtl_info_tit_txt').get_text())
        print(soup.find('em', class_='ssg_price').get_text())
        # 추출한 정보를 출력합니다.
        # print('키보드:')
        # for idx, (keyword,price) in enumerate(zip(search_keywords, prices), start=1):
        #     print(f'{idx}. {keyword.text} {price.text}')
    else:
        print(f'Error: {response.status_code}')

if __name__ == '__main__':
    crawl_realtime_search()
