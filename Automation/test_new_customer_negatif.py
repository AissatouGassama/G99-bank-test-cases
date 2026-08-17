from Pages.login_page import LoginPage
from Pages.new_customer_page import NewCustomerPage


#test scenario name customer avec les differents cas de test
def test_cas_nom_customer_vide(page_connectee):
    page_connectee.click("text=New customer")
    new_customer_page=NewCustomerPage(page_connectee)
    new_customer_page.champ_name.fill("")
    new_customer_page.champ_name.press("Tab")
    assert "Customer name must not be blank" in page_connectee.locator("body").inner_text()
    print("Test réussi: le nom ne doit pas etre vide")


def test_cas_nom_customer_avec_chiffre(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text=New Customer")
    new_customer_page.champ_name.fill("Awa123")
    new_customer_page.champ_name.press("Tab")
    texte_de_la_page= page_connectee.locator("body").inner_text()
    assert "Numbers are not allowed" in texte_de_la_page
    print("Test réussi : le nom ne prend pas de chiffre !")

def test_cas_nom_customer_avec_caractère_spécial(page_connectee):
    page_connectee.click("text=New Customer")
    new_customer_page= NewCustomerPage(page_connectee)
    new_customer_page.champ_name.fill("@Awa!@")
    new_customer_page.champ_name.press("Tab")
    assert"Special characters are not allowed" in page_connectee.locator("body").inner_text()
    print("Test réussi: le nom ne pend pas de caractere spécial")

def test_cas_nom_qui_commence_avec_espace(page_connectee):
    page_connectee.click("text=New customer")
    new_customer_page= NewCustomerPage(page_connectee)
    new_customer_page.champ_name.fill(" ")
    new_customer_page.champ_name.press("Tab")
    assert "First character can not have space"in page_connectee.locator("body").inner_text()
    print("Test réussi: le nom ne doit pas commencer par un espace")
    
    #test scenario address customer avec les differents cas de test
def test_cas_adresse_vide(page_connectee):
    page_connectee.click("text=New customer")
    new_customer_page= NewCustomerPage(page_connectee)
    new_customer_page.champ_address.fill("")
    new_customer_page.champ_address.press("Tab")
    assert "Address Field must not be blank" in page_connectee.locator("body").inner_text()
    print("Test réussi: l'adresse ne doit pas etre vide")

def test_adresse_avec_caractère_spéciale(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_address.fill("Menival!@?")
    new_customer_page.champ_address.press("Tab")
    assert "Special characters are not allowed" in page_connectee.locator("body").inner_text()
    print("Test réussi: l'adreese ne doit pas contenir de caractere spécial")

def test_cas_adress_commence_par_espace(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_address.fill(" ")
    new_customer_page.champ_address.press("Tab")
    assert "First character can not have space" in page_connectee.locator("body").inner_text()
    print("Test réussi: l'adreese ne doit pas commencer par un espace")

    #test scenario city customer avec les differents cas de test
def test_cas_city_vide(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text=New customer")
    new_customer_page.champ_city.fill("")
    new_customer_page.champ_city.press("Tab")
    assert "City Field must not be blank" in page_connectee.locator("body").inner_text()
    print("Test réussi: le champ city ne doit pas etre vide")

def test_cas_city_avec_chiffre(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text=New Customer")
    new_customer_page.champ_city.fill("Lyon123")
    new_customer_page.champ_city.press("Tab")
    assert "Numbers are not allowed" in page_connectee.locator("body").inner_text()
    print("Test réussi : le champ city ne prend pas de chiffre !")

def test_cas_city_avec_caractere_spécial(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_city.fill("@lyon!?")
    new_customer_page.champ_city.press("Tab")
    assert "Special characters are not allowed" in page_connectee.locator("body").inner_text()
    print("Test réussi: le champ city ne doit pas contenir de caractere spécial")

def test_cas_city_commence_avec_un_espace(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_city.fill(" ")
    new_customer_page.champ_city.press("Tab")
    assert "First character can not have space" in page_connectee.locator("body").inner_text()
    print("Test réussi: le champ city ne doit pas commencer par un espace")
    
    #test scenario State customer avec les differents cas de test
def test_cas_state_avec_chiffre(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text=New Customer")
    new_customer_page.champ_state.fill("Rhone123")
    new_customer_page.champ_state.press("Tab")
    assert "Numbers are not allowed" in page_connectee.locator("body").inner_text()
    print("Test réussi : le champ state ne prend pas de chiffre !")

def test_cas_state_vide(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text=New customer")
    new_customer_page.champ_state.fill("")
    new_customer_page.champ_state.press("Tab")
    assert "State must not be blank" in page_connectee.locator("body").inner_text()
    print("Test réussi: le champ state ne doit pas etre vide")

def test_cas_state_commence_par_un_espace(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_state.fill(" ")
    new_customer_page.champ_state.press("Tab")
    assert "First character can not have space" in  page_connectee.locator("body").inner_text()
    print("Test réussi: le champ State ne doit pas commencer par un espace")

    #test scenario pin customer avec les differents cas de test
def test_cas_code_postal_avec_lettres(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_pin.fill("6900PI")
    new_customer_page.champ_pin.press("Tab")
    assert "Characters are not allowed" in page_connectee.locator("body").inner_text()
    print("Test réussi: le code postal ne peut etre que numérique")

def test_cas_code_postal_vide(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_pin.fill("")
    new_customer_page.champ_pin.press("Tab")
    assert "PIN Code must not be blank" in page_connectee.locator("body").inner_text()
    print("Test réussi: Le champ code postl de peut pas etre vide")

def test_cas_code_postal_avec_caractère_spécial(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_pin.fill("690?@!")
    new_customer_page.champ_pin.press("Tab")
    assert "Special characters are not allowed" in page_connectee.locator("body").inner_text()
    print("Test réussi: Le code postal ne peut pas contenir de caractères spéciaux")


def test_cas_code_postal_avec_moins_de_six_caractere(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_pin.fill("69000")
    new_customer_page.champ_pin.press("Tab")
    assert "PIN Code must have 6 Digits" in page_connectee.locator("body").inner_text()
    print("Test réussi: le code postal ne peut pas contenir moins  de 6 chiifres")

def test_cas_code_postal_avec_espace(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_pin.fill("69 000")
    new_customer_page.champ_pin.press("Tab")
    assert "Characters are not allowed" in page_connectee.locator("body").inner_text()
    print("Test réussi: le code postal ne peut pas avoir d'espace")


    #test scenario number customer avec les differents cas de test
def test_cas_number_vide(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_number.fill("")
    new_customer_page.champ_number.press("Tab")
    assert "Mobile no must not be blank" in page_connectee.locator("body").inner_text()
    print("Test réussi: le champ Numéro de téléphone ne peut pas etre etre vide")

def test_cas_number_avec_caractère_spécial(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_number.fill("988899@§/")
    new_customer_page.champ_number.press("Tab")
    assert "Special characters are not allowed" in page_connectee.locator("body").inner_text()
    print("Test réussi: le numéro de téléphone ne peut pas contenir de caractères spéciaux")

def test_cas_number_avec_lettres(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_number.fill("98889NUM")
    new_customer_page.champ_number.press("Tab")
    assert "Characters are not allowed" in page_connectee.locator("body").inner_text()
    print("Test réussi: Le numéro de téléphone ne peut etre que numérique")

def test_cas_number_qui_commence_avec_un_espace(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_number.fill(" 7799999")
    new_customer_page.champ_number.press("Tab")
    assert "First character can not have space" in page_connectee.locator("body").inner_text()
    print("Test réussi: le numéro de téléphone ne peut pas commencer avec un espace")


    #test scenario Email customer avec les differents cas de test
def test_email_new_customer_vide(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_email.fill("")
    new_customer_page.champ_email.press("Tab")
    assert "Email-ID must not be blank" in page_connectee.locator("body").inner_text()
    print("Test réussi: le champ adresse email ne peut pas etre vide")

def test_cas_email_new_customer_non_valide(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_email.fill("awa1exemple.com")
    new_customer_page.champ_email.press("Tab")
    assert "Email-ID is not valid" in page_connectee.locator("body").inner_text()
    print("Test réussi: ladresse email  non  valide")

def test_cas_email_commence_avec_un_espace(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_email.fill(" ")
    new_customer_page.champ_email.press("Tab")
    assert "First character can not have space" in page_connectee.locator("body").inner_text()
    print("Test réussi: L'adresse email ne peut pas commencer avec un espace")

    #test scenario password customer avec les differents cas de test
def test_cas_password_new_customer_vide(page_connectee):
    new_customer_page= NewCustomerPage(page_connectee)
    page_connectee.click("text= New customer")
    new_customer_page.champ_password.fill("")
    new_customer_page.champ_password.press("Tab")
    assert "Password must not be blank" in page_connectee.locator("body").inner_text()
    print("Test réussi:le mot de passe ne doit pas etre vide ")






















    













 
    




    




