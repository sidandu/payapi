import requests

url = "http://127.0.0.1:5000/payment/api"
headers ={'Accept': 'application/json', 'Content-Type': 'application/json'}
auth = ('dandu','pass123')
card_data = {"card_number": "5105105105105100", "card_holder": "jaffa", "card_expiry": "02-2021", "card_cvv": 13, "amount": 10.0}

resp = requests.get(url=url, headers=headers, auth = auth, json = card_data)

print(resp.status_code, resp.json())
    