# Trendyol Stok Takip Botu

Bu proje, Trendyol'daki belirli bir ürünün stok durumunu takip eder ve seçilen beden tekrar stoklara girdiğinde kullanıcıya e-posta bildirimi gönderir.

## ✨ Proje Amacı
- Trendyol'daki ürün sayfasını otomatik olarak kontrol etmek
- Belirli bedenlerin stok durumunu gözlemlemek
- Belirlenen beden stokta olduğunda anında e-posta göndermek

## ⚙️ Kullanılan Teknolojiler
- Python
- BeautifulSoup (HTML parse)
- Requests (HTTP istekleri)
- smtplib (e-posta gönderimi)
- python-dotenv (.env dosyasından bilgi alma)

## ⚡ Kurulum
1. Bu repoyu klonlayın:
```bash
git clone https://github.com/kullaniciadi/trendyol-stok-botu.git
```
2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```
3. Ana dizinde `.env` dosyası oluşturun ve aşağıdaki bilgileri girin:
```env
SENDER_EMAIL=seningmailin@gmail.com
SENDER_PASSWORD=uygulama_sifren
RECEIVER_EMAIL=alici@gmail.com
```
> Not: Gmail hesabınızda 2 adımlı doğrulama aktif olmalıdır ve uygulama Şifresi kullanılmalıdır.

## 🚀 Kullanım
```bash
python main.py
```
Kod çalıştığında:
- Trendyol sayfasından ürün bilgileri çekilir
- Belirlenen beden stokta ise e-posta gönderilir
- Bu kontrol belirli aralıklarla otomatik olarak tekrarlanır (varsayılan: 10 dakika)

## 📊 Örnek Terminal Çıktısı
```
Sayfa başarıyla çekildi.
Ürün Adı: Keten Karışımlı Pantolon
- XS (stokta)
✅ E-posta gönderildi!
```

## 📅 Geliştirme Planı
- Farklı bedenleri birden fazla kontrol etme
- Kullanıcı arayüzü ekleme (tkinter/web)
- Farklı mağazalardaki ürünleri takip etme
- Bildirimleri mobil uygulama/telegram ile de yollama

---

Hazırlayan: Nil Akşun

> Bu proje kişisel kullanım için geliştirilmiştir. Trendyol tarafından resmi olarak desteklenmemektedir.

