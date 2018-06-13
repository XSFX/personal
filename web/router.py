import site

site.addsitedir("./../lib")

from user import user


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
