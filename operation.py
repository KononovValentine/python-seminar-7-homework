import data
import view

def checkMode(mode):
    if mode == 'in':
        return 1
    elif mode == 'out':
        return 2
    else:
        return 0

def clearData():
    data.lastName = ''
    data.firstName = ''
    data.phoneNumber = ''
    data.description = ''

def writeData():
    date = f'; Фамилия: {data.lastName} , Имя: {data.firstName} , Номер телефона: {data.phoneNumber} , ' \
           f'Описание: {data.description}'
    return date

def writeFile():
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(writeData())
        file.close()
        clearData()

def checkList():
    with open('data.txt', 'r', encoding='utf-8') as file:
        array = list(map(str, file.readline().split('; ')))
        for i in array:
            if ';' in i:
                i = i.replace(';', '')
            print(i)
    file.close()

def checkLastName(lastName):
    with open('data.txt', 'r', encoding='utf-8') as file:
        array = list(map(str, file.readline().split('; ')))
        error = False
        for i in array:
            if f'Фамилия: {lastName} ' in i:
                print(i)
                error = True
        if error == False:
            print('Данного человека нет в списке')
    file.close()

def detectOverlap():
    with open('data.txt', 'r', encoding='utf-8') as file:
        array = list(map(str, file.readline().split('; ')))
        error = False
        for i in array:
            if f'Фамилия: {data.lastName} ' in i:
                error = True
        if error == True:
            file.close()
            return 1
        else:
            file.close()
            return 0

def detectEmptyRequest():
    if data.lastName == '' or data.firstName == '' or data.description == '' or data.phoneNumber == '':
        return 1
    else:
        return 0

def enterInfo():
    view.enterData()
    checkOverlap = detectOverlap()
    checkEmptyRequest = detectEmptyRequest()
    if checkOverlap == 0 and checkEmptyRequest == 0:
        writeFile()
    elif checkOverlap == 1:
        view.printError(2)
    elif checkEmptyRequest == 1:
        view.printError(3)