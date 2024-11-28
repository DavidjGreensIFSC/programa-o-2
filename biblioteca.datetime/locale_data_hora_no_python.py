from datetime import datetime, date, time, timedelta
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

"""bg_BG.UTF-8"""

dataAgoraNoPaisDoLocale = datetime.now()

data_formatada = dataAgoraNoPaisDoLocale.strftime("%x")
hora_formatada = dataAgoraNoPaisDoLocale.strftime("%x")

print ("Data formatada: ", data_formatada)
print ("Hora formatada: ", hora_formatada)