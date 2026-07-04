def html_olustur(baslik, hizmetler, telefon):
    html_kod = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>{baslik}</title>
        <style>
            body {{ font-family: Arial; line-height: 1.6; padding: 20px; }}
            .hizmet {{ border-bottom: 1px solid #ccc; padding: 10px 0; }}
            .tel {{ color: red; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>{baslik}</h1>
        <p>İstanbul'un her noktasında, 7/24 profesyonel ve güvenilir oto kurtarma hizmetimizle yanınızdayız.</p>
    """
    
    for hizmet in hizmetler:
        html_kod += f"""
        <div class="hizmet">
            <h2>{hizmet}</h2>
            <p>İhtiyaç anında {hizmet} için en hızlı çözüm! Bizi hemen arayın: <span class="tel">{telefon}</span></p>
        </div>
        """
        
    html_kod += "</body></html>"
    
    # Dosyaya yaz
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_kod)
    print("index.html dosyası başarıyla oluşturuldu!")

# Veriler
h1 = "İstanbul Çekici"
h2_liste = ['EN Yakın Çekici', 'İSTANBUL OTO KURTARICI NELER YAPAR?', 'İSTANBUL’DA YOL YARDIM HİZMETLERİMİZ', 'İstanbul Oto Kurtarıcı']
telefon = "05495562301"

html_olustur(h1, h2_liste, telefon)