import requests

api_url = "http://localhost:8080/graphql"

#(placar, combinaçoes experadas)
test_scores = [
    ("0x0", 1),  
    ("3x0", 1),  
    ("6x6", 4),  
    ("9x3", 2),  
    ("12x12", 9),
    ("27x25", 77),  
]

def send_query(score):
    query = """
        mutation {
            verify(score: "%s") {
                combinations
            }
        }
    """ % score
    response = requests.post(api_url, json={"query": query})
    return response.json()

for score, expected_combinations in test_scores:
    response = send_query(score)
    combinations = response["data"]["verify"]["combinations"]
    assert combinations == expected_combinations, f"Esperava {expected_combinations} combinações para o placar {score}, o resultado foi {combinations}"
    print(f"Sucesso para o placar {score}: {combinations} combinações")