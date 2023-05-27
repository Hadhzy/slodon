import slodon.api.test.server


async def task1():
    pass


async def task2():
    pass

from slodon.api.test.server import test_method


test_method()
slodon.api.test.server.TEST_VALUE = 1
test_method()


string1 = "test/test2"

string2 = string1.split("/")[0]
print(string2)
