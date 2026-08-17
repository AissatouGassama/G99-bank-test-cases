from Pages.login_page import LoginPage

def test_login_reussi(page):
    login_page = LoginPage(page)
    login_page.se_connecter("mngr664973", "jenuzap")
    assert "Manager" in page.locator("body").inner_text()