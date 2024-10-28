from Address import address
from Mailing import mailing

to_address = Address("404137", "Волжский", "Горького", "1г", "14")
from_addres = Address("404360", "Котельниково", "Цимлянская", "24", "1") 
mailing = Mailing(to_address, from_address, 350, 12345)


print(f'Отправление {mailing.track} из {mailing.from_address.index}) 