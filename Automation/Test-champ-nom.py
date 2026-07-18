from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    navigateur = p.chromium.launch(headless=False)
    page = navigateur.new_page()
    page.goto("https://demo.guru99.com/V4/index.php")

    
    #Au lieu d'attendre "à l'aveugle" on attend que ce champ precis soit visible
    champ_identifiant = page.locator("input[name='uid']")
    expect(champ_identifiant).to_be_visible()
    
    print("le champ identifiant est bien visible, on continue!")
    champ_identifiant.fill("mngr663553")
    page.fill("input[name='password']", "bygubEV")
    page.click("input[type=submit]")

    text_newcustomer = page.locator("a[href='addcustomerpage.php']")
    expect(text_newcustomer).to_be_visible()
    print("le texte new custommer est bien visible, on continue!")
    
    navigateur.close()
