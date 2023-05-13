from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture
def open_resize_browser():
    browser.open('https://google.com')
    driver = browser.driver
    driver.maximize_window()
    driver.set_window_size(800, 800)

def test_google_search(open_resize_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_abra(open_resize_browser):
    browser.element('[name="q"]').should(be.blank).type('jknfinasdfniasnfijansifjnaisnfijasdnfiansdjfnasdfniasdnfiaisnfiasnfinaifniassnfinasifnainf').press_enter()
    browser.element('[class="card-section"]').should(have.text('ничего не найдено'))
    print('Результатов не найдено')
