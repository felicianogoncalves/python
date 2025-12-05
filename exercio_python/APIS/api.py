import requests
import json
#coordenadas de braga

latitude=41.545
longitude=-8.426

#endpoint  e parametros
url="https://api.open-meteo.com/v1/forecast"

params={
    'latitude' : latitude,
    'longitude' : longitude,
    'daily' : 'temperature_2m_max,temperature_2m_min',
    'timezone' : 'auto'
}

#pedido à API

response=requests.get(url,params=params)

# verificação da repsosta

if response.status_code == 200:
    data=response.json()

#mostrar os dados no terminal
    print(json.dumps(data,indent=4))
else:
    print('Erros ao aceder API:', response.status_code)
    print('respostasAPI',response.text)