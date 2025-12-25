import pytest
import os
from datetime import datetime

@pytest.fixture(scope="function")
def set_up(page):
    # Configuración de pantalla profesional
    page.set_viewport_size({"width": 1280, "height": 720})
    
    yield page # Aquí es donde corre tu test
    
    # Lógica de Reporte: Toma captura si el test termina
    if not os.path.exists("results"):
        os.makedirs("results")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    page.screenshot(path=f"results/evidencia_{timestamp}.png")