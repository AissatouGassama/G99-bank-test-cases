from playwright.sync_api import expect

class NewAccountPage:
    def __init__(self, page):
        self.page= page
        self.champ_customerid = page.locator("input[name='cusid']")
        self.champ_account_type = page.locator("select[name='selaccount']")
        self.champ_initdeposit= page.locator("input[name='inideposit']")
        self.btn_submit= page.locator("input[type='submit']")



    def creer_compte( self, customerid, account_type, initial_deposit,):
        self.page.click("text=New Account")
        self.champ_customerid.fill(customerid)
        self.champ_account_type.select_option(account_type)
        self.champ_initdeposit.fill(initial_deposit)
        self.btn_submit.click()
        print("url aprés submit", self.page.url)
        assert "AccCreateMsg.php" in self.page.url, "la création du compte à échoué"
        num_compte= self.page.url.split("aid")[1]
        return num_compte

        