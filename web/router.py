import site

site.addsitedir("./../lib")

from user import user


def test(**params):
    return {"success": "OK"}


def createUser(**params):
    return user.create(**params);


def listUsers(**params):
    return user.list()
