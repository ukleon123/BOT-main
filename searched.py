import json
import requests
from urllib import parse

class Searched:
    def __init__(self):
        self.linkFrame = 'https://search.naver.com/search.naver?query='
        self.URL = "https://api.signal.bz/news/realtime"
        self.header = {
            'referer' : "https://www.signal.bz/",
            'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        }
    def getData(self):
        links = list()
        keywords = list()
        raw = requests.get(self.URL, self.header)
        data = json.loads(raw.text)
        for keyword in data['top10']:
            keywords.append(keyword['keyword'])
            link = parse.quote(keyword['keyword'])
            links.append(self.linkFrame + link)
        return keywords, links
class StockUp:
    def __init__(self):
        self.URL ="https://m.stock.naver.com/api/stocks/up/KOSPI?page=1&pageSize=20" 
        self.header = { 
            "referer" : "https://m.stock.naver.com/index.html",
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36" 
        }

        self.linkframe = "https://finance.naver.com/item/main.nhn?code="
    def getData(self):
        num = 0
        response = requests.get(self.URL, headers = self.header)
        stockdata = json.loads(response.text)
        
        links = list()
        result = list()
        
        for data in stockdata['stocks']:
            if(num < 10):
                frame = list()
                frame.append(data['closePrice'])
                frame.append(data['fluctuationsRatio'])
                frame.append(data['stockName'])
                result.append(frame)
                
                links.append(self.linkframe + data['itemCode'])
                num += 1
        return result, links

        
