import serial
import pandas as pd
import os
import time

# Seri port ve baud rate ayarları
serial_port = 'COM8'  # Arduino'nun bağlı olduğu portu buraya yazın (örn. COM3, COM4, /dev/ttyUSB0)
baud_rate = 9600

# Masaüstü yolu

excel_file = os.path.join('sıcaklık_nabız.xlsx')

# Seri portu aç
ser = serial.Serial(serial_port, baud_rate)

# Eğer Excel dosyası mevcut değilse, yeni bir dosya oluştur
if not os.path.exists(excel_file):
    df = pd.DataFrame(columns=['Nabız', 'Sıcaklık'])  # Sütun başlıkları
    df.to_excel(excel_file, index=False, engine='openpyxl')

try:
    while True:
        # Seri porttan gelen veriyi oku
        line = ser.readline().decode('utf-8').strip()  # Veriyi string olarak al
        print(f"Gelen veri: {line}")  # Gelen veriyi ekrana yazdır

        # Veriyi nabız ve sıcaklık olarak ayır (eğik çizgi kullanarak)
        try:
            pulse, temperature = map(float, line.split('/'))  # Nabız ve sıcaklığı ayır
        except ValueError:
            print("Hatalı veri formatı, atlanıyor.")
            continue

        # Yeni veriyi DataFrame'e ekle
        new_data = pd.DataFrame({'Nabız': [pulse], 'Sıcaklık': [temperature]})

        # Dosyayı kilitlenmeden sürekli güncelle
        try:
            # Veriyi doğrudan Excel dosyasına kaydet
            with pd.ExcelWriter(excel_file, mode='a', if_sheet_exists='overlay', engine='openpyxl') as writer:
                df = pd.read_excel(excel_file, engine='openpyxl')
                df = pd.concat([df, new_data], ignore_index=True)
                df.to_excel(writer, index=False, sheet_name='Sheet1')
            print("Veri başarıyla kaydedildi.")
        except PermissionError:
            print("Excel dosyası başka bir program tarafından kullanılıyor. 5 saniye sonra tekrar denenecek...")
            time.sleep(5)  # Excel dosyası başka bir program tarafından kilitlenirse 5 saniye bekleyin ve tekrar deneyin
            continue

except KeyboardInterrupt:
    print("Veri alımı durduruldu.")
finally:
    ser.close()


