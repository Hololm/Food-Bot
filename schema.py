import requests
import threading
import random


def main():
    s = requests.Session()
    s.headers = {}

    def log():
        json_data = {}

        res = s.post('', json=json_data)
        auth_token = res.json()
        s.headers.update({'Authorization': 'Bearer {}'.format(auth_token)})

    def visit():
        jsonData = {}

        s.headers.update({'Authorization': 'Bearer {}'.format('')})
        res_response = s.post('', json=jsonData)

        print(res_response.text)

    thread_list = []
    for i in range(50):
        thread_list.append(threading.Thread(target=visit))
    for x in thread_list:
        x.start()


if __name__ == "__main__":
    main()
