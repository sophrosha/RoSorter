import pytest


class DummyBase:
    def __init__(self):
        self.messages = []

    def printf(self, code, *args):
        self.messages.append((code, args))


@pytest.fixture
def dummy_base():
    return DummyBase
