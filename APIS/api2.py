import requests
import json
#coordenadas de braga

latitude=41.545
longitude=-8.426

#endpoint  e parametros
url="https://api.open-meteo.com/v1/forecast?latitude=41.5503&longitude=-8.42&hourly=temperature_2m,wind_speed_10m,relative_humidity_2m&forecast_days=1"


#pedido à API

response=requests.get(url)

# verificação da repsosta

if response.status_code == 200:
    data=response.json()

#mostrar os dados no terminal
    print(json.dumps(data,indent=4))
else:
    print('Erros ao aceder API:', response.status_code)
    print('respostasAPI',response.text)