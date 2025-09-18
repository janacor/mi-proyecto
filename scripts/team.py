from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.futgal.es/pnfg/NPcd/NFG_CmpPartido?cod_primaria=1000120&CodActa=1291366&cod_acta=1291366"

driver = webdriver.Chrome()
driver.get(url)

iframes = driver.find_elements(By.TAG_NAME, "iframe")
print(f"Detectados {len(iframes)} iframes")

for i, iframe in enumerate(iframes):
    src = iframe.get_attribute("src")
    print(f"Iframe {i}: {src}")
    
    if src:
        driver.get(src)  # abrir directamente la URL del iframe
        time.sleep(2)
        
        html = driver.page_source
        with open(f"iframe_direct_{i}.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ Guardado iframe_direct_{i}.html ({len(html)} caracteres)")

driver.quit()
