import pytest


@pytest.fixture(autouse=True)
def my_fixture():
    with open("text1.txt", "w") as f:
        f.write("some")
    with open("text2.txt", "w") as f:
        f.write("text")
    with open("text3.txt", "r") as f:
        pass
