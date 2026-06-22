import json
with open('kaggle-housePrice/flask_deployment/data.json', 'r') as f:
    data = json.load(f)
    print(f"Jumlah nilai: {len(data['data'][0])}")