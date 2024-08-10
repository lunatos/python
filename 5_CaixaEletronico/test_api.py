import requests
import json

# Test 1: Valor invalido
response = requests.post(
    'http://localhost:8000/api/saque',
    headers={'Content-Type': 'application/json'},
    data=json.dumps({'valor':0})
)
print('Test 1: valor = 0')
print(response.text)
print()

# Test 2: Valor sem possibilidades de ser sacado
response = requests.post(
    'http://localhost:8000/api/saque',
    headers={'Content-Type': 'application/json'},
    data=json.dumps({'valor':101})
)
print('Test 2: valor = 101')
print(response.text)
print()

# Test 3: Teste com resultado positivo
response = requests.post(
    'http://localhost:8000/api/saque',
    headers={'Content-Type': 'application/json'},
    data=json.dumps({'valor':274})
)
print('Test 3: valor = 274')
print(response.text)
print()