#!/usr/bin/env python3
# Kayyum Onaylı En Yavaş Hesap Makinesi
# Mahkeme kararıyla yazılmıştır. Acele etmek yasak.

import time
import random

def mahkeme_durusmasi():
    print("Mahkeme duruşması başlatılıyor...")
    time.sleep(2)
    print("Savcı: 2 + 2 gerçekten gerekli mi?")
    time.sleep(1)
    print("Kayyum: Gerekli. Ama yavaşça.")
    time.sleep(1)

def felsefi_soru():
    sorular = [
        "Peki bu sayılar gerçek mi, yoksa sadece bir illüzyon mu?",
        "İki artı iki, evrenin temel sabitlerinden biri mi?",
        "Hesaplamak bir hak mı, yoksa bir ayrıcalık mı?",
        "Bürokrasi olmadan matematik olur mu?"
    ]
    print(random.choice(sorular))
    time.sleep(1.5)

def hesapla():
    print("=== Kayyum Onaylı Hesap Makinesi ===")
    print("Lütfen işlem için mahkeme onayını bekleyin...\n")
    
    mahkeme_durusmasi()
    felsefi_soru()
    
    print("\nHesaplama başlıyor... (bu biraz zaman alabilir)")
    time.sleep(3)
    
    # Gizli not: bazen en basit işlemler bile beklemeyi gerektirir.
    sonuc = 2 + 2
    
    print(f"\nMahkeme kararı: {sonuc}")
    print("Bu sonuç kayyum onaylıdır. İtiraz süresi 30 yıldır.")
    print("\nİşlem tamamlandı. Teşekkürler, sabırlı vatandaş.")

if __name__ == "__main__":
    hesapla()
