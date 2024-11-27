'''Pytz é uma biblioteca do Python  que permite calcular fusos horários 
e resolver problemas com horários ambiguos no final do horário de verão.

O tzdata é um 'pacote' de dados do Python que fornece dados de fuso horário
IANA. Ele é principalmente usado pelo módulo "zoneinfo" da biblioteca padrão.
Mas também pode ser usado como fonte de dados de fuso horário.;'''
 
from datetime import datetime, date, time, timedelta

data_de_hoje = date.today()

horario_especifico = time(hour=14, minute=30, second=35)

print (data_de_hoje)
print (horario_especifico)