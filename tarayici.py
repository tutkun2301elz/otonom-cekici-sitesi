import xml.etree.ElementTree as ET
import requests
import time

# İndeksleyici modülündeki fonksiyonunu buraya dahil etmen gerekecek
# Şimdilik mantığı kuruyoruz:
def sitemap_oku(xml_dosya):
    tree = ET.parse(xml_dosya)
    root = tree.getroot()
    
    # Namespace tanımlama (Sitemap standartlarında gereklidir)
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [url.find('ns:loc', ns).text for url in root.findall('ns:url', ns)]
    return urls

def toplu_indeksle(url_listesi):
    for url in url_listesi:
        print(f"İşleniyor: {url}")
        # Burada indeksleyici.py içindeki API çağrını tetikleyeceksin
        # Örnek: publish_to_indexing_api(url)
        time.sleep(1) # API limitlerine takılmamak için bekleme süresi

if __name__ == "__main__":
    url_listesi = sitemap_oku('sitemap.xml')
    print(f"Toplam {len(url_listesi)} URL bulundu.")
    toplu_indeksle(url_listesi)