# Donanım

## Kart modeli
Büyük ihtimalle **Deneyap Kart 1A (ilk sürüm)**. Kesinleştirmek için kartın üstündeki yazıya bakılmalı.
Gerekçe: WROVER modülü ve PSRAM var. Normal Deneyap Kart'ın kart üstü IMU'su (LSM6DSM, I2C 0x6A) ve PDM mikrofonu taramada çıkmadı. 1A v2 ESP32-S3 kullanıyor, bu kart ise klasik ESP32.

| Özellik | Değer | Kaynak |
|---|---|---|
| Modül | ESP32-WROVER-E | resmi doküman |
| İşlemci | Tensilica LX6, çift çekirdek, 240 MHz | doküman + test |
| SRAM / ROM | 520 KB / 448 KB | doküman |
| PSRAM | 8 MB (dokümana göre). Klasik ESP32 doğrudan 4 MB eşler; testte 4 MB görüldü | doküman + test |
| Flash | 4 MB SPI | doküman + test |
| Kablosuz | Wi-Fi 802.11 b/g/n, Bluetooth Classic + BLE | çip + test |
| USB-seri | CP2102N | test |
| Kart üstü sensör | IMU ve mikrofon yok sayılıyor (I2C taramasında bulunamadı) | test |
| Arduino desteği | Var | doküman |

Kaynaklar: https://deneyapkart.org/en/docs/deneyap-kart-1a · https://circuitpython.org/board/deneyap_kart/

## Ana kart (sağlık testi: 2026-11-11, MicroPython v1.25.0)
| Özellik | Sonuç |
|---|---|
| Çip | ESP32-D0WD-V3 rev 3.0, çift çekirdek, 240 MHz |
| Flash | 4 MB ✓ |
| PSRAM | 4 MB ✓ (WROVER modülü) |
| Wi-Fi | ✓ 9 ağ, en güçlü −41 dBm |
| Bluetooth LE | ✓ 4 sn'de 40 cihaz |
| USB-seri | CP2102N ✓ (921600 baud'da okuma koptu, 460800 sorunsuz) |
| BOOT butonu (GPIO0) | Bırakılı = 1 ✓ (basma testi yapılmadı) |
| I2C | Hiçbir pin çiftinde cihaz bulunamadı: kart üstünde I2C sensör yok ya da besleme gerekiyor |

Kartın üzerinde önceden kalmış bir Arduino sketch vardı (giriş-only pinlere çıkış veriyordu). Flash yedeği `yedek/`te. Geri yükleme:
`esptool --port /dev/ttyUSB0 -b 460800 write-flash 0 yedek/yedek-orijinal-flash.bin`

## Linux erişimi
Kullanıcı `dialout` grubunda değil. Geçici: `sudo setfacl -m u:$USER:rw /dev/ttyUSB0`. Kalıcı: `sudo usermod -aG dialout $USER`, sonra oturumu kapatıp aç.

## Yedek kart
Arduino klonu da var (model doğrulanmadı).
