import requests
import json



def test_initial_call():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = json.dumps({'message_type': 'New Order Single',
     'stock_symbol': 'AAPL',
     'quantity': 1,
     'price': 123,
     'side': 'Buy',
     'order_type': 'Market'})

    resp = requests.post('http://127.0.0.1:5000/fixmessage/api', params=data)
    print(resp.json())

test_initial_call()