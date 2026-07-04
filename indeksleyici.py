import xml.etree.ElementTree as ET
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import logging

SERVICE_ACCOUNT_FILE = 'hizmet-hesabi-anahtari.json' 

def google_api_bildir(url):
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, 
                    scopes=['https://www.googleapis.com/auth/indexing'])
    service = build('indexing', 'v3', credentials=creds)
    content = {'url': url, 'type': 'URL_UPDATED'}
    return service.urlNotifications().publish(body=content).execute()

def otonom_tarayici():
    tree = ET.parse('sitemap.xml')
    root = tree.getroot()
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    # Tüm URL'leri topla
    urls = [url.find('ns:loc', ns).text for url in root.findall('ns:url', ns)]
    
    print(f"Sistem taraması başlatıldı. {len(urls)} URL tespit edildi.")
    
    for url in urls:
        try:
            google_api_bildir(url)
            print(f"BİLDİRİLDİ: {url}")
        except Exception as e:
            print(f"HATA ({url}): {e}")

if __name__ == "__main__":
    otonom_tarayici()