######### declarar variables tipos strings #############
varA= "cadena"
print (varA)
print (type(varA))
print (len(varA))
print (varA[2])
print (varA[-2])
from datetime import datetime
from dateutil.relativedelta import relativedelta

fecha_nacimiento = datetime.strptime("02/11/1987", "%d/%m/%Y")
edad = relativedelta(datetime.now(), fecha_nacimiento)
print(f"{edad.years} años, {edad.months} meses y {edad.days} días")

######## 'type' se utiliza para ver el tipo de variable en este caso ######


