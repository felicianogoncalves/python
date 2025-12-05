# exercicio:calcular a difrença entre duas datas: e a data de nascimentos

from datetime import datetime, date, time, timedelta

data_atual=datetime.now()
data_aniv=datetime(1995,7,4)

diferençaentredatas= (data_atual-data_aniv)

print(diferençaentredatas)

from dateutil.relativedelta import relativedelta

delta=relativedelta(data_atual,data_aniv)

print(f'{delta.years} anos , {delta.months} meses,')

import time

print('Esperar 3 segundos')
time.sleep(3)
print('Fim da Pausa')