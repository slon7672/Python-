from address import Address
from mailing import Mailing

to_address_mail = Address("743465", "Белгород", "Пушкина", 22, 56)
from_address_mail = Address("359728", "Владивосток", "Колотушкина", 12, 2)
treck = "3579"
cost = 456

track_mail = Mailing(to_address_mail, from_address_mail, treck, cost)

print(
    f"Отправление {treck} из {from_address_mail} в {to_address_mail}. "
    f"Стоимость {cost} рублей."
)
