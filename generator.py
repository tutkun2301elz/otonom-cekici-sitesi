import os

# Ayarlar
FILE_NAME = "index.html"
NEW_TITLE = "Esenyurt Oto Çekici | 7/24 Profesyonel Yol Yardım"
NEW_DESCRIPTION = "Esenyurt bölgesinde 7/24 en hızlı ve güvenilir oto çekici hizmeti."

def update_site_content():
    # HTML dosyasını otonom olarak güncelle
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        content = f.read()

    # Başlık güncelleme (Regex veya basit replace kullanılabilir)
    updated_content = content.replace("<title>Esenyurt Oto Çekici | 7/24 Profesyonel Yol Yardım</title>", 
                                     f"<title>{NEW_TITLE}</title>")
    
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"{FILE_NAME} başarıyla güncellendi.")

# Git süreçlerini otonom tetikleme
def push_to_github():
    os.system("git add index.html")
    os.system('git commit -m "Otonom: İçerik ve SEO güncellendi"')
    os.system("git push -u origin main")
    print("Değişiklikler GitHub'a gönderildi.")

if __name__ == "__main__":
    update_site_content()
    push_to_github()