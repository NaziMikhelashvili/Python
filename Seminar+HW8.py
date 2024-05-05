# Задача 49 - создать телефонный справочник с возможность импорта и экспорта данных в формате txt 
# Фамилия имя отчетсво номер телефона - данные которые должны находиться в файле 


def create_contact():
    s_name = str(input('введите фамилию:'))
    f_name = str(input('введите имя:'))
    m_name = str(input('введите отчество:'))
    phone = str(input('введите номер телефона:'))
    return f'{s_name} {f_name} {m_name}: {phone}'

def add_new_contact():
    contact_str = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact_str)


def open_phonebook():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n')
        for n, contacts_str in enumerate(contacts_list, 1):
            print(n, contacts_str)

def find_contact():
    print(f'Варианты поиска: \n1 По фамилии \n2 по имени \n3 по отчеству \n4 по телефону' )
    var = input('выберите вариант поиска:')
    while var not in ('1', '2', '3', '4'):
        print('некорректный ввод')
        var = input('выберите вариант поиска:')
    i_var = int(var) - 1

    search = input('введите данные для поиска: ').title() #делает заглавными буквы
    with open('phonebook.txt', 'r', encoding= 'utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n') #rstrip убирает пробелы с правой стороны
        #split убирает знаки переноса 
    for str_contact in contacts_list:
        list_contact = str_contact.replace(':', '').split()
        if search in list_contact[i_var]:
            print(str_contact)


def copy_phonebook():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
        contacts_list = contacts_str.rstrip().split('\n')
        row = int(input('введите номер строки для копирования: '))
        for n, contacts_str in enumerate(contacts_list, 1):
            list_contact = contacts_str.replace(':', '').split()
            with open('phonebook2.txt', 'a', encoding='utf-8') as file:
                if n == row:
                    file.write(contacts_str)
                    file.write('\n')
    print('копирование завершено')

def main():
    menu =4
    while menu !=0:
        print(f'Варианты действий: \n1 добавить контакт \n2 найти контакт \n3 открыть всю книгу \n4 скопировать контакт \n0 выход')
        menu =int(input('Выберите, что хотите сделать: '))
        if menu == 1:
            add_new_contact()
        elif menu == 2:
            find_contact()
        elif menu == 3:
            open_phonebook()
        elif menu == 4:
            copy_phonebook()
        elif menu == 0:
            pass
        else:
            print ('некорректный ввод')
            menu = int(input('Выберите, что хотите сделать: '))
        input('Нажмите Enter чтобы продолжить')
        print()

main()




