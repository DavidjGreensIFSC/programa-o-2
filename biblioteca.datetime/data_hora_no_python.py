'''Pytz é uma biblioteca do Python  que permite calcular fusos horários 
e resolver problemas com horários ambiguos no final do horário de verão.

O tzdata é um 'pacote' de dados do Python que fornece dados de fuso horário
IANA. Ele é principalmente usado pelo módulo "zoneinfo" da biblioteca padrão.
Mas também pode ser usado como fonte de dados de fuso horário.;'''
 
from datetime import datetime, date, time, timedelta
import locale

data_de_hoje = date.today()
horario_especifico = time(hour=14, minute=30, second=35)

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

"""bg_BG.UTF-8"""

dataAgoraNoPaisDoLocale = datetime.now()

data_formatada = dataAgoraNoPaisDoLocale.strftime("%x")
hora_formatada = dataAgoraNoPaisDoLocale.strftime("%x")

print (data_de_hoje)
print (horario_especifico)
print ("Data formatada: ", data_formatada)
print ("Hora formatada: ", hora_formatada)