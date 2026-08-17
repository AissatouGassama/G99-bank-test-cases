import pytest
from Pages.login_page import LoginPage

@pytest.fixture
def page_connectee(page):
    login_page=LoginPage(page)
    login_page.se_connecter("mngr664973", "jenuzap")

    return page
