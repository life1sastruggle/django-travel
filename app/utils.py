import random
import uuid


def generateUUID():
    return ''.join(str((uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid1()) + str(random.random())))).split('-'))
