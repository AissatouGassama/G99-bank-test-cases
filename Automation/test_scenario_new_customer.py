from Pages.login_page import LoginPage
from Pages.new_customer_page import NewCustomerPage
from Pages.new_account_page import NewAccountPage
import random

def test_creer_un_client(page_connectee):
    new_customer_page=NewCustomerPage(page_connectee)
    email_aleatoire= f"awa{random.randint(10000, 99999)}@exemple.com"
    id_client = new_customer_page.creer_client("Awa", "f", "1999-05-12", 
    "Menival", "Lyon", "France", "690000", "87666788", email_aleatoire, "test123")
    
    new_account_page=NewAccountPage(page_connectee)
    new_account_page.creer_compte(id_client, "Current", "1000")

