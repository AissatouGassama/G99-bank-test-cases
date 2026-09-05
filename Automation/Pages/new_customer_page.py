from playwright.sync_api import expect

class NewCustomerPage:
    def __init__(self, page):
        self.page= page
        self.champ_name = page.locator("input[name='name']")
        self.champ_gender_male = page.locator("input[name='rad1'][value='m']")
        self.champ_gender_female = page.locator("input[name='rad1'][value='f']")
        self.champ_datebirth =page.locator("input[name='dob']")
        self.champ_address = page.locator("textarea[name='addr']")
        self.champ_city = page.locator("input[name='city']")
        self.champ_state = page.locator("input[name='state']")
        self.champ_pin = page.locator("input[name='pinno']")
        self.champ_number = page.locator("input[name='telephoneno']")
        self.champ_email = page.locator("input[name='emailid']")
        self.champ_password = page.locator("input[name='password']")
        self.btn_submit = page.locator("input[type='submit']")


    def creer_client(self, name, gender, datebirth, address, city, state, pin,
     number, email, password ):
        self.page.click("text=New Customer")
        print("le texte new custommer est bien visible, on continue!")
        
        self.champ_name.fill(name)

        if gender == "m":
            self.champ_gender_male.check()
        else:
            self.champ_gender_female.check()
      
        self.champ_datebirth.fill(datebirth)
        self.champ_address.fill(address)
        self.champ_city.fill(city)
        self.champ_state.fill(state)
        self.champ_pin.fill(pin)
        self.champ_number.fill(number)
        self.champ_email.fill(email)
        self.champ_password.fill(password)
        self.btn_submit.click()
        self.page.wait_for_load_state("networkidle")
        print("url apés submit:", self.page.url)
        assert "CustomerRegMsg.php" in self.page.url, "la creation du client à échoué"
        id_client=self.page.url.split("cid=")[1]
        return id_client

    
      
  
        
