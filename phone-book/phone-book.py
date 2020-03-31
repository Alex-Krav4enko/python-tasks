class Contact:
    def __init__(self, name, surname, phone_number, favorite=True, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite = favorite
        self.details = kwargs

    def __str__(self):
        separator = '\n\t\t\t\t'
        return f'''
            Имя: {self.name}
            Фамилия: {self.surname}
            Телефон: {self.phone_number}
            В избранных: {self._get_favorite_status()}
            Дополнительная информация:
                {separator.join(self.get_details(self.details))}
        '''

    @staticmethod
    def get_details(raw_details):
        details = []
        for value in raw_details:
            details.append(f'{value}: {raw_details[value]}')
        return details

    def _get_favorite_status(self):
        return 'да' if self.favorite else 'нет'


class PhoneBook:
    contact_list = []

    def __init__(self, name):
        self.name = name

    def get_contact_list(self):
        self._print_list(self.contact_list)

    def add_contact(self, contact):
        self.contact_list.append(contact)

    def delete_contact(self, phone_number):
        for contact in self.contact_list:
            if contact.phone_number == phone_number:
                self.contact_list.remove(contact)
                break

    def get_favorites(self):
        favorites = list(filter(lambda contact: contact.favorite, self.contact_list))
        self._print_list(favorites)

    def get_by_name(self, name):
        contacts = []
        for contact in self.contact_list:
            full_name = f'{contact.name} {contact.surname}'
            try:
                full_name.index(name)
                contacts.append(contact)
            except ValueError:
                continue
        self._print_list(contacts)

    @staticmethod
    def _print_list(_list):
        if len(_list):
            for contact in _list:
                print(contact)
        else:
            print('Empty results')


phone_book = PhoneBook('example')
jhon = Contact('Jhon', 'Smith', '+71234567809', favorite=False, telegram='@jhony', email='jhony@smith.com')
bill = Contact('Bill', 'Smith', '+79000000000', favorite=True, telegram='@bill', email='bill@smith.com')
kate = Contact('Kate', 'Smith', '+79111111111', favorite=True, telegram='@kate', email='kate@smith.com')

phone_book.add_contact(jhon)
phone_book.add_contact(bill)
phone_book.add_contact(kate)

phone_book.delete_contact('+79000000000')
phone_book.get_contact_list()
