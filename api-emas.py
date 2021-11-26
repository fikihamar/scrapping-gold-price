import requests, re
from bs4 import BeautifulSoup

class APIemas:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
    
    def getMonth(month):
        result = "00"
        if (month == "Januari"):
            result = "01"
        elif (month == "Februari"):
            result = "02"
        elif (month == "Maret"):
            result = "03"
        elif (month == "April"):
            result = "04"
        elif (month == "Mei"):
            result = '05'
        elif (month == "Juni"):
            result = "06"
        elif (month == "Juli"):
            result = '07'
        elif (month == "Agustus"):
            result = "08"
        elif (month == "September"):
            result = '09'
        elif (month == "Oktober"):
            result = "10"
        elif (month == "November"):
            result = "11"
        elif (month == "Desember"):
            result = '12'
        
        return result

    def hargaEmas(self, request):
        url = 'https://www.anekalogam.co.id/id'

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.37'
        }  
        response = requests.get(url, headers=headers) 
        soup = BeautifulSoup(response.content, 'html.parser')

        data = []
        price_buy = []
        price_sell = []
        result = []
        last_update = ""

        h3 = soup.select('span.n-heading')
        for x in h3:
            data.append(float(x.text.replace("Rp","").strip().replace(".", "")))

        for index, value in enumerate(data, start=1):
            if (index % 2 == 0):
                price_buy.append(value)
            elif (index % 2 == 1):
                price_sell.append(value)

        
        date = re.sub("\s{4,}"," ", soup.select('strong.n-heading')[0].text.replace("\n", "")).strip().split(" ")
        last_update = int(date[2] + APIemas.getMonth(date[1]) + date[0]) 

        emas = [1, 2, 3, 5, 10, 25, 50, 100]
        for index, value in enumerate(emas):
            result.append(
                {
                    "name" : f"Emas LM {value} gram",
                    "price_buy" : price_buy[index],
                    "price_sell" : price_sell[index],
                    "last_update" : last_update 
                }
            )
                
        response = {
                'status' : 200,
                'data' : result
            }

        return response  