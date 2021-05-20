import requests
import pandas as pd
import urllib


def get_api(url, param):
    result = requests.get(url, param)
    return result.json()

def main():
    keyword = "Python Django 開発入門"
    # ranking API
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    param = {
            'applicationId':1019079537947262807,
            'age':30,
            ':sex':0
            }
    col = ['rank', 'item', 'price', 'itemUrl']
    df = pd.DataFrame(index=[], columns = col)
    r = get_api(url, param)
    for i in range(10):
        r1 = r['Items'][i]['Item']
        df = df.append(pd.Series([r1['rank'], r1['itemName'], r1['itemPrice'], r1['itemUrl']], index=col), ignore_index=True)
#    rank = r['Items'][0]['rank']
    print(df)
    df.to_csv('ranking.csv')

main()
