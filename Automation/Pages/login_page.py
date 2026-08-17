from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.champ_identifiant = page.locator("input[name='uid']")
        self.password = page.locator("input[name='password']")
        self.btn_submit = page.locator("input[type= 'submit']")


    def se_connecter(self, identifiant, password):
        self.page.goto("https://demo.guru99.com/V4/index.php")

        expect(self.champ_identifiant).to_be_visible()
        print("le champ identifiant est bien visible, on continu!")
    
        self.champ_identifiant.fill(identifiant)
        self.password.fill(password)
        self.btn_submit.click()
        print("Url aprés submit", self.page.url)

