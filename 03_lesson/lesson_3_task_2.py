from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "A6", "+7 928 333-22-88"),
    Smartphone("Nokia", "C3", "+7 961 320-80-23"),
    Smartphone("Siemens", "B4", "+7 961 286-04-80"),
    Smartphone("Samsung", "C8", "+7 928 446-72-60"),
    Smartphone("Honor", "A8", "+7 938 125-35-70"),
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. " f"{phone.subscriber_number}")
