import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Use: --language=en")

@pytest.fixture
def browser(request):
    language = request.config.getoption("--language")
    if not language:
        raise pytest.UsageError("--language should be set")
    options_es = Options()
    options_es.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options_es)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()