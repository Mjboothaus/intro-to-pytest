import pytest

# fixtures/cli_opt/conftest.py
def pytest_addoption(parser):
    parser.addoption("--myopt", type=str)

@pytest.fixture
def myopt(request):
    return request.config.option.myopt
