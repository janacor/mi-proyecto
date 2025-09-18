import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ruta del JSON
RUTA_JSON = "equipos.json"

# Cargar equipos
with open(RUTA_JSON, "r", encoding="utf-8") as f:
    equipos = json.load(f)

# Configurar Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Ejecuta sin abrir ventana del navegador
driver = webdriver.Chrome(options=options)

# URL del partido (modifica según el partido que quieras)
url = "https://www.futgal.es/pnfg/NPcd/NFG_CmpPartido?cod_primaria=1000120&CodActa=1291366&cod_acta=1291366"
driver.get(url)

# Esperar que se carguen los elementos clave
wait = WebDriverWait(driver, 10)

# --- EXTRAER EQUIPOS ---
# Ajusta estos XPATH según la estructura real de la página
equipo_local = wait.until(
    EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'Local')]/following-sibling::td"))
).text.strip()

equipo_visitante = wait.until(
    EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'Visitante')]/following-sibling::td"))
).text.strip()

goles_local = 0
goles_visitante = 0

print(f"{equipo_local} vs {equipo_visitante}\n")

# --- EXTRAER GOLES ---
# Ajusta el XPATH a la tabla real de goles
filas_goles = driver.find_elements(By.XPATH, "//table[contains(@summary,'goles')]/tbody/tr")

for fila in filas_goles:
    celdas = fila.find_elements(By.TAG_NAME, "td")
    if len(celdas) < 3:
        continue
    minuto = celdas[0].text.strip()
    equipo = celdas[1].text.strip()
    jugador = celdas[2].text.strip()

    # Actualizar goles jugador
    if equipo in equipos and jugador in equipos[equipo]["jugadores"]:
        equipos[equipo]["jugadores"][jugador] += 1

    # Actualizar marcador
    if equipo == equipo_local:
        goles_local += 1
    elif equipo == equipo_visitante:
        goles_visitante += 1

    print(f"{minuto}' - {jugador} ({equipo}) → {equipo_local} {goles_local} - {goles_visitante} {equipo_visitante}")

# Guardar JSON actualizado
with open(RUTA_JSON, "w", encoding="utf-8") as f:
    json.dump(equipos, f, indent=4, ensure_ascii=False)

print(f"\nResultado final: {equipo_local} {goles_local} - {goles_visitante} {equipo_visitante}")

driver.quit()
