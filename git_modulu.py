import os
import subprocess

def git_yukle():
    try:
        os.chdir(r'C:\Users\Necdet\Desktop\Otonom_robotu\klon_site_robotu')
        
        # Sadece dosyaları ekle, .json anahtarını özellikle hariç tut
        subprocess.run(['git', 'add', '--all', ':!hizmet-hesabi-anahtari.json'], check=True)
        
        status = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if not status.stdout.strip():
            print("BİLGİ: Gönderilecek yeni değişiklik yok.")
            return

        subprocess.run(['git', 'commit', '-m', 'Otonom sistem: Otomatik içerik güncellendi'], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("BAŞARILI: Veriler GitHub'a gönderildi.")
    except Exception as e:
        with open("hata_log.txt", "a") as f:
            f.write(f"HATA: {e}\n")
        print(f"HATA: {e}")