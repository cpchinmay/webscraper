import requests
import json
import pandas as pd

# ['Deal Date', 'Security Code', 'Security Name', 'Client Name', 'Deal Type *', 'Quantity', 'Price **']

r=requests.get("https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx",headers={'User-Agent': 'Custom'})


read_html_pandas_data = pd.read_html(r.text)[1]
print(len(read_html_pandas_data))
print(list(read_html_pandas_data.columns))
# Define the API endpoint URL
url = "http://localhost:8000/users/"
for ind in read_html_pandas_data.index:
    print(read_html_pandas_data['Deal Date'][ind], read_html_pandas_data['Security Code'][ind])


        # Define the request payload
    payload = {
        "deal_date": read_html_pandas_data['Deal Date'][ind],
        "security_code": read_html_pandas_data['Security Code'][ind],
        "security_name": read_html_pandas_data['Security Name'][ind],
        "client_name": read_html_pandas_data['Client Name'][ind],
        "deal_type": read_html_pandas_data['Deal Type *'][ind],
        "quantity": int(read_html_pandas_data['Quantity'][ind]),
        "price": int(read_html_pandas_data['Price **'][ind])
    }

    # Convert the payload to JSON
    payload_json = json.dumps(payload)

    # Set the request headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the POST request
    response = requests.post(url, data=payload_json, headers=headers)

    # Check the response
    if response.status_code == 200:
        # Successful request
        print("User created successfully")
        print(response.json())
    else:
        # Failed request
        print("Error creating user")
        print(response.text)