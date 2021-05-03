import requests

url = "https://ucf.uscourts.gov/odata.svc/Creditors(guid'1c207e82-fce2-11ea-a4de-0050569e7a8f')"

headers = {
    'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'x-requested-with': "XMLHttpRequest",
    'sec-ch-ua-mobile': "?0",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'cache-control': "no-cache",
    'postman-token': "46e9f240-3b8d-ded8-0f8b-f03b368ad909"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)