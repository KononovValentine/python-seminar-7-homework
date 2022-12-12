import view
import operation

def startProgram():
    mode = operation.checkMode(view.startButton())
    if mode == 1:
        view.importData()
        operation.enterInfo()
    elif mode == 2:
        view.exprotData()
        value = int(view.exportOneOrMany())
        if value == 0:
            operation.checkList()
        elif value == 1:
            lastName = view.enterLastName()
            operation.checkLastName(lastName)
        else:
            view.printError(1)
    else:
        view.printError(1)


