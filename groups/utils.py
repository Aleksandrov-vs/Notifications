import secrets


def createID():
    return secrets.token_hex(5)