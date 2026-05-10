# 🫀 Yapay Zeka Destekli Hasta Takip Sistemi

Bu proje, gerçek zamanlı hasta verilerini takip etmek amacıyla geliştirilmiş yapay zeka destekli bir sağlık izleme sistemidir. Sistem; EKG verilerini, nabız değerlerini ve vücut sıcaklığını anlık olarak okuyup analiz ederek kullanıcı dostu bir arayüz üzerinden göstermektedir.

Proje kapsamında Arduino üzerinden alınan sensör verileri Python ile işlenmiş, Excel dosyalarına kaydedilmiş ve PyQt5 kullanılarak geliştirilen hastane temalı bir arayüzde görselleştirilmiştir. Ayrıca sistem içerisinde taşikardi (hızlı kalp ritmi) simülasyonu da bulunmaktadır.

---

## 🚀 Özellikler

- Gerçek zamanlı EKG görüntüleme
- Anlık nabız takibi
- Vücut sıcaklığı ölçümü
- Taşikardi simülasyonu
- Excel tabanlı veri kaydı
- PyQt5 ile modern kullanıcı arayüzü
- Arduino ile seri port haberleşmesi
- Otomatik veri güncelleme sistemi
- Hastane tipi hasta takip ekranı

---

## 🧰 Kullanılan Teknolojiler

- Python
- PyQt5
- NumPy
- Pandas
- Matplotlib
- OpenPyXL
- SciPy
- PySerial
- Arduino

---

## 📂 Proje Yapısı

```bash
├── mergeGui.py
├── sicaklikNabiz.py
├── tasikardiDeneme.py
├── megadeneme.xlsx
├── sıcaklık_nabız.xlsx
├── arayuz.bat
├── sıcaklık_nabız.bat
├── tasikardi.bat
