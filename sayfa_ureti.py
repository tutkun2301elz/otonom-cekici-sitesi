import os

# Ayarlar: Hedef anahtar kelimeler
ANAHTAR_KELIMELER = ["Esenyurt Araç Kurtarma", "Esenyurt Çekici Fiyatları", "Beylikdüzü Esenyurt Oto Çekici"]

# Şablon: index.html yapın
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>{kelime} | 7/24 Profesyonel Yol Yardım</title>
    <meta name="description" content="{kelime} için hemen bizi arayın. Esenyurt genelinde hızlı çekici hizmeti.">
</head>
<body>
    <h1>{kelime}</h1>
    <p>Aracınız yolda mı kaldı? {kelime} konusunda uzman ekibimizle hizmetinizdeyiz.</p>
</body>
</html>
"""

def sayfalar_uret():
    if not os.path.exists('sayfalar'):
        os.makedirs('sayfalar')
    
    for kelime in ANAHTAR_KELIMELER:
        dosya_adi = kelime.replace(" ", "_").lower() + ".html"
        with open(f"sayfalar/{dosya_adi}", "w", encoding="utf-8") as f:
            f.write(HTML_TEMPLATE.format(kelime=kelime))
        print(f"Oluşturuldu: {dosya_adi}")

if __name__ == "__main__":
    sayfalar_uret()