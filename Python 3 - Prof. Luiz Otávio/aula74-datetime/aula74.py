from datetime import datetime, timedelta

data1 = datetime(2019, 12, 17, 5, 52, 52)
data2 = datetime.strptime('01/02/0500 03:00:00', '%d/%m/%Y %H:%M:%S')
print(data1.strftime('%d/%m/%Y %H:%M:%S'))

data1 = datetime.strptime('17/12/2019', '%d/%m/%Y')
print(data1.strftime('%d/%m/%Y %H:%M:%S'))
print(data1.timestamp())
print(datetime.fromtimestamp(data1.timestamp()))

print(data1 + timedelta(days=7, seconds=700, hours=27))
print(data2)
print(data1 > data2)
print((data1 - data2))
