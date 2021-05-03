import requests
from bs4 import BeautifulSoup
import csv
import json

page = 1


while page <1318:


    url = "https://ucf.uscourts.gov/search"

    querystring = {"SelectedCourts":"","CreditorSearch":"","DebtorSearch":"","CaseNumber":"","Amount":"40","EnteredOn":"08/12/2020","page":str(page),"__swhg":["1620060421194,1620060688027,1620060718791","1620060825184"]}

    headers = {
        'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
        'accept': "text/html, */*; q=0.01",
        'x-requested-with': "XMLHttpRequest",
        'sec-ch-ua-mobile': "?0",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'cache-control': "no-cache",
        'postman-token': "8fe59f2f-3f77-fa99-1184-951b859c57d8"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    html1 = BeautifulSoup(response.content, 'html.parser')

    trs = html1.find_all('tr')

    for tr in trs:

        court = ''
        case = ''
        street1 = ''
        street2 = ''
        street3 = ''
        city = ''
        state = ''
        zipcode = ''
        country = ''
        creditor_name = ''
        debtor_name = ''
        amount = ''
        id = ''
        scrapedUrl = 'https://ucf.uscourts.gov/search?SelectedCourts=&CreditorSearch=&DebtorSearch=&CaseNumber=&Amount=40&EnteredOn=08%2F15%2F2020&page=' + str(page)

        tds = tr.find_all('td')

        try:
            court = tds[1]
            court = court.text.strip()

        except:
            print ("Error")

        try:
            case = tds[2]
            case = case.text.strip()

        except:
            print ("Error")

        try:
            creditor_name = tds[3]
            creditor_name = creditor_name.text.strip()
            print (creditor_name)

        except:
            print ("Error")

        try:
            debtor_name = tds[4]
            debtor_name = debtor_name.text.strip()

        except:
            print ("Error")

        try:
            amount = tds[5]
            amount = amount.text.strip()

        except:
            print ("Error")


        try:
            id = tds[0]
            try:
                button = id.find('button')
                id = button.get('id')



                second_url = "https://ucf.uscourts.gov/odata.svc/Creditors(guid'" + str(id) +"')"
                print (second_url)

                headers1 = {
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

                response1 = requests.request("GET", second_url, headers=headers1)

                data = json.loads(response1.text)

                if 'Street1' in data:
                    street1 = data['Street1']

                if 'Street2' in data:
                    street2 = data['Street2']

                if 'Street3' in data:
                    street3 = data['Street3']

                if 'City' in data:
                    city = data['City']


                if 'State' in data:
                    state = data['State']

                if 'ZipCode' in data:
                    zipcode = data['ZipCode']

                if 'Country' in data:
                    country = data['Country']


            except:
                print ("Error")

        except:
            print ("Error")


        if id != '':

            temp = []
            temp.append(court)
            temp.append(case)
            temp.append(street1)
            temp.append(street2)
            temp.append(street3)
            temp.append(city)
            temp.append(state)
            temp.append(zipcode)
            temp.append(country)
            temp.append(creditor_name)
            temp.append(debtor_name)
            temp.append(amount)
            temp.append(id)
            temp.append(scrapedUrl)

            print (temp)

            arr = []
            arr.append(temp)

            with open('data1.csv', 'a+') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(arr)



    page = page+1

