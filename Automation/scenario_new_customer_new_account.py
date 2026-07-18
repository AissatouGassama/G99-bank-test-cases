from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    navigateur = p.chromium.launch(headless=False)
    page = navigateur.new_page()
    page.goto("https://demo.guru99.com/V4/index.php")

    
    #Au lieu d'attendre "à l'aveugle" on attend que ce champ precis soit visible
    champ_identifiant = page.locator("input[name='uid']")
    expect(champ_identifiant).to_be_visible()
    
    print("le champ identifiant est bien visible, on continue!")
    champ_identifiant.fill("METS_TON_IDENTIFIANT_ICI")
    page.fill("input[name='password']", "METS_TON_MOT_DE_PASSE_ICI")
    page.click("input[type=submit]")

    # Attendons qu'aprés connexion, que le texte new customer soit visible
    text_newcustomer = page.locator("a[href='addcustomerpage.php']")
    expect(text_newcustomer).to_be_visible()
    print("le texte new custommer est bien visible, on continue!")
    
    text_newcustomer.click()
    # attendons  que le  champ name de new customer soit visible
    champ_name = page.locator("input[name='name']")
    expect(champ_name).to_be_visible()
    print('le champ nom est bien visible, on continue!')
    
    champ_name.fill("Aissatou")
    champ_name.press("Tab")
    print("le champ name est saisie")

    champ_date_of_birth = page.locator("input[name='dob']")
    expect(champ_date_of_birth).to_be_visible()
    champ_date_of_birth.fill("1995-05-15")
    champ_date_of_birth.press("Tab")
    print("le champ date of birth est visible")
    
    champ_address = page.locator("textarea[name='addr']")
    expect(champ_address).to_be_visible()
    champ_address.fill("12 Rue Montchat")
    champ_address.press("Tab")
    print("champ adresse est visible")

    champ_city= page.locator("input[name='city']")
    expect(champ_city).to_be_visible()
    champ_city.fill("Lyon")
    champ_city.press("Tab")
    print("le champ city est bien visible")

    champ_state= page.locator("input[name='state']")
    expect(champ_state).to_be_visible()
    champ_state.fill("France")
    champ_state.press("Tab")
    print("le champ State es bien visible")

    champ_pin= page.locator("input[name='pinno']")
    expect(champ_pin).to_be_visible()
    champ_pin.fill("690003")
    champ_pin.press("Tab")
    print("le champ pin est bien visible")

    champ_telephone=page.locator("input[name='telephoneno']")
    expect(champ_telephone).to_be_visible()
    champ_telephone.fill("07884444322")
    champ_telephone.press("Tab")
    print("le champ telephone est bien visible")


    champ_email= page.locator("input[name='emailid']")
    expect(champ_email).to_be_visible()
    champ_email.fill("jean9990test@exemple.com")
    champ_email.press("Tab")
    print("le champ email est bien visible")

    champ_password= page.locator("input[name='password']")
    expect(champ_password).to_be_visible()
    champ_password.fill("test@1234")
    champ_password.press("Tab")
    print("le champ pasword est bien visible")

    btn_submit =page.locator("input[type='submit']")
    btn_submit.click()
    print("tous les champs sont remplis")
    

    text_newaccount= page.locator("a[href='addAccount.php']")
    expect(text_newaccount).to_be_visible()
    text_newaccount.click()
    print("le texte new account est bien visible")

    champ_customerid= page.locator("input[name='cusid']")
    expect(champ_customerid).to_be_visible()
    champ_customerid.fill("93161")
    champ_customerid.press("Tab")
    print("le champ customer id est bien visible")

    champ_account_type = page.locator("select[name='selaccount']")
    expect(champ_account_type).to_be_visible()
    champ_account_type.select_option("Savings")
    print("le type de compte est sélectionné")

    champ_initdeposit= page.locator("input[name='inideposit']")
    expect(champ_initdeposit).to_be_visible()
    champ_initdeposit.fill("600")
    champ_initdeposit.press("Tab")
    print("le champ initial depot est bien visible")

    page.locator("input[type='submit']").click()
    print("ok")

    texte_de_la_page= page.locator("body").inner_text()
    print(texte_de_la_page)
    



    

    

    
    










   

    
    


    


