import requests
from bs4 import BeautifulSoup
import json
import re
import smtplib
from email.mime.text import MIMEText
import time
from dotenv import load_dotenv
import os

# Ortam değişkenlerini yükle (e-posta bilgileri gibi gizli bilgiler .env dosyasından çekilecek)
load_dotenv()


# 1. Ürün sayfasını Trendyol'dan çek
def fetch_product_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Sayfa başarıyla çekildi.")
        return BeautifulSoup(response.text, "html.parser")
    else:
        print(f"Hata oluştu. Durum kodu: {response.status_code}")
        return None


# 2. E-posta gönderme fonksiyonu
def send_email(receiver_email, subject, message, sender_email, sender_password):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("✅ E-posta gönderildi!")
    except Exception as e:
        print("❌ E-posta gönderilemedi:", e)


# 3. Ürün bilgilerini al, beden stok durumunu kontrol et ve gerekirse e-posta gönder

def get_product_info(soup):
    scripts = soup.find_all("script")
    json_data = None

    for script in scripts:
        if script.string and "window.__PRODUCT_DETAIL_APP_INITIAL_STATE__" in script.string:
            match = re.search(r"window\.__PRODUCT_DETAIL_APP_INITIAL_STATE__ = ({.*});", script.string.strip())
            if match:
                json_text = match.group(1)
                try:
                    json_data = json.loads(json_text)
                except json.JSONDecodeError as e:
                    print("JSON çözümlemesi başarısız:", e)
                    return
            break

    if not json_data:
        print("Ürün JSON verisi bulunamadı.")
        return

    product_title = json_data.get("product", {}).get("name", "Ürün adı bulunamadı")
    print(f"\nÜrün Adı: {product_title}")

    variants = json_data.get("product", {}).get("variants", [])
    if not variants:
        print("Varyant bilgisi bulunamadı.")
        return

    desired_size = "XS"  # Takip edilmek istenen beden
    desired_in_stock = False

    print("\nBeden Seçenekleri:")
    for variant in variants:
        size = variant.get("attributeValue", "Beden bilinmiyor")
        sellable = variant.get("sellable", False)
        status = "stokta" if sellable else "STOKTA YOK"
        print(f"- {size} ({status})")

        if size.upper() == desired_size and sellable:
            desired_in_stock = True

    # Eğer istenen beden stokta ise e-posta gönder
    if desired_in_stock:
        send_email(
            receiver_email=os.getenv("RECEIVER_EMAIL"),
            subject=f"{desired_size} Bedeni Stokta!",
            message=f"{desired_size} bedeni stokta! Link: {product_url}",
            sender_email=os.getenv("SENDER_EMAIL"),
            sender_password=os.getenv("SENDER_PASSWORD")
        )


# 4. Takip edilecek ürün linki
product_url = "https://www.trendyol.com/stradivarius/keten-karisimli-bol-kesim-pantolon-p-670154023"

# 5. Bot'u sürekli çalıştır: belirli aralıklarla kontrol et
while True:
    soup = fetch_product_page(product_url)
    if soup:
        get_product_info(soup)

    print("\n🔁 10 dakika bekleniyor...\n")
    time.sleep(600)  # 600 saniye = 10 dakika
