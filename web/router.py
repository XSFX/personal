import site

site.addsitedir("./../lib")

from user import user
from task import task

def test(**params):
    return {"success": "OK"}

def createUser(**params):
    return user.create(**params);


def listUsers(**params):
    return user.list()

def loginUser(**params):
    return user.auth(**params)

def checkUserToken(**params):
    return user.checkToken(**params)

def showTask(**params):
    return task.showTask(**params)

def listTaskCategories(**params):
    return task.listCategories(**params)

def listTasks(**params):
    return task.listTasks(**params)

def createTaskCategory(**params):
    return task.createCategory(**params)

def createTask(**params):
    return task.createTask(**params)
