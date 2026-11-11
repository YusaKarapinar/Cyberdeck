# Donanım

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
