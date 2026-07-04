import sayfa_ureti
import git_modulu
import indeksleyici

def fabrikayi_calistir():
    print("--- Otonom Dijital Varlık Fabrikası Başlatılıyor ---")
    
    # 1. Aşama: Yeni içerik üret
    print("Adım 1: Sayfalar üretiliyor...")
    sayfa_ureti.sayfalar_uret() 
    
    # 2. Aşama: Git senkronizasyonu
    print("Adım 2: GitHub senkronizasyonu yapılıyor...")
    git_modulu.git_yukle()
    
    # 3. Aşama: Google'a indeksleme bildirimi (Fonksiyon ismi düzeltildi)
    print("Adım 3: İndeksleme talepleri gönderiliyor...")
    indeksleyici.otonom_tarayici()
    
    print("--- Fabrika görevini başarıyla tamamladı ---")

if __name__ == "__main__":
    fabrikayi_calistir()