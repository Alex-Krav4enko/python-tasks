documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2', '5455 028765'],
  '2': ['10006', '5400 028765', '5455 002299'],
  '3': []
}


def get_input_data(message):
    m = input(message)
    return int(m) if type(m) == int else m


def get_name():
    doc_number = get_input_data('Введите номер документа: ')
    doc = list(filter(lambda d: d['number'] == doc_number, documents))
    if len(doc):
        try:
            document = doc.pop()['name']
        except KeyError as e:
            print(f'Exception: {e.args[0]}')
        else:
            print(document)
    else:
        print('По указанным значениям ничего не найдено')


def get_documents():
    for document in documents:
        doc = '{} {} {}'.format(document['type'], document['number'], document['name'])
        print(doc)


def get_directory():
    doc_number = get_input_data('Введите номер документа: ')
    for d in directories:
        if bool(directories[d].count(doc_number)):
            print('На полке {} найден документ: {}'.format(d, doc_number))
            return
    print('Указанного документа {} нет'.format(doc_number))


def get_directory_number():
    directory_number = get_input_data('Введите номер полки: ')
    is_valid_directory = bool(len(list(filter(lambda d: d == directory_number, directories))))
    if not is_valid_directory:
        print('Полки № {} нет'.format(directory_number))
        get_directory_number()
    else:
        return directory_number


def add_document():
    doc_type = get_input_data('Введите тип документа: ')
    doc_number = get_input_data('Введите номер документа: ')
    owner = get_input_data('Введите имя владельца: ')
    directory_number = get_directory_number()
    doc = dict(type = doc_type, number = doc_number, name = owner)
    documents.append(doc)
    directories[directory_number].append(doc_number)
    print('Новый документ добавлен: ')
    get_documents()


commands = {
    'p': get_name,
    'l': get_documents,
    's': get_directory,
    'a': add_document
}


def start():
    command = get_input_data('Введите команду: ')
    try:
        commands[command]()
    except KeyError as e:
        print('Указанной команды {} нет'.format(e.args[0]))
        start()


start()