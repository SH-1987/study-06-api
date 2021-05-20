import requests
import urllib


def get_api(url, param):
    result = requests.get(url, param)
    return result.json()


def main():
    keyword = "Python Django 開発入門"
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426"
    param = {
            'applicationId':1019079537947262807,
            'keyword':keyword,
            }
    r = get_api(url, param)

    # 最高値、最安値取得
    maxprice = r['Products'][0]['Product']['maxPrice']
    minprice = r['Products'][0]['Product']['minPrice']
    print('最高値:{}, 最安値:{}'.format(maxprice, minprice))

main()
