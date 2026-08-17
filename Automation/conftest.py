import pytest
from Pages.login_page import LoginPage

import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def page_connectee(page):
    login_page=LoginPage(page)
    login_page.se_connecter(os.getenv("GURU99_USER"), os.getenv("GURU99_PASSWORD"))

    return page
