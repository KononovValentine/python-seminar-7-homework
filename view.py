import data

def startButton():
    print('Добро пожаловать в телефонный справочник')
    return input('Введите "in" для ввода данных или "out" для получения данных: ')

def importData():
    print('Выбран режим ввода данных')

def exprotData():
    print('Выбран режим вывода данных')

def exportOneOrMany():
    return input('Введите 0 для получения всего списка или 1 для получения одной записи: ')

def printData(data):
    print(data)

def printError(error):
    if error == 1:
        print('Введен некорректный запрос!')
    elif error == 2:
        print('Человек с такой фамилией уже находится в списке!')
    else:
        print('Введены не все данные!')

def enterData():
    data.lastName = input('Введите фамилию: ')
    data.firstName = input('Введите имя: ')
    data.phoneNumber = input('Введите номер: ')
    data.description = input('Введите описание: ')

def enterLastName():
    return input('Введите фамилию: ')