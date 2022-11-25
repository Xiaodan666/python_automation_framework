import pytest


@pytest.fixture(scope='class')
def login():
    print("这是在conftest里面的一个方法")
