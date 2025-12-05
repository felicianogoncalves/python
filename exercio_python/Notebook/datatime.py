from datetime import datetime,date,time,timedelta

#saber a data e hora atuais

agora=datetime.now()
print(agora)

# saber a data ou a hora

hoje=date.today()
print(hoje)

#saber o mes

hora_atual=agora.time()
print(hora_atual)
print(hoje.month)
print(hoje.year)
print(hoje.day)

data_especifica=date(2004,7,12)
hora_especifica=time(14,30,5)

print(data_especifica)
print(hora_especifica)

#formatação de datas
#dd/mm/aaaa

print(agora.strftime('%d-%m-%y'))

#converter string para um tipo date time

data_str='19/08/2025 03:05'
data_convertida=datetime.strptime(data_str,'%d/%m/%Y %H:%M')

print(data_convertida)

#operações com datas

amanha=hoje + timedelta(days=1)
ontem=hoje - timedelta(days=1)

#tambem podemos adicionar ou subtrair horas, minutos ou semanas
mais_2horas=agora + timedelta(hours=2)

#calendarios
import calendar

#saber se o ano é bissexto

print(calendar.isleap(2025))

#mostrar calendario
print(calendar.month(2025,9))

#dia da semana
# 0 - segunda feira , 6 é domingo
dia_semana=calendar.weekday(2025,9,19)
print(dia_semana)