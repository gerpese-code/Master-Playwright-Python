import json
from pages.login_page import LoginPage

# Función para leer los datos del JSON
def load_user_data():
    with open('data/auth_data.json') as f:
        return json.load(f)

def test_login_con_json(set_up):
    page = set_up # Usamos la configuración de tu conftest.py
    data = load_user_data()
    
    login_page = LoginPage(page)
    login_page.navigate()
    
    # Usamos los datos del archivo JSON
    login_page.login(data["user"], data["pass"])
    
    # Verificamos el éxito
    assert page.url == "https://www.saucedemo.com/inventory.html"