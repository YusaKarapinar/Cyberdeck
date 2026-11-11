# Cyberdeck

Deneyap Kart (ESP32) tabanlı, el tipi kişisel "cep terminali".

## Konsept
- Avuç boyu, 3D baskı gövde
- 2.4–3.5" SPI TFT ekran, terminal görünümü
- Tactile buton matrisli mini klavye
- LiPo pil + şarj devresi
- Yanda genişleme "kartuş" yuvası (önce LoRa, sonra sensör/IR)

Uygulamalar: Wi-Fi/BLE tarayıcı, seri terminal, SD'ye not defteri, sistem ekranı.

## Yol haritası
1. Kart + ekran + 3 buton ile menü
2. Klavye
3. Kasa
4. Pil
5. Kartuş yuvası

## Klasörler
- `tools/`: MicroPython test scriptleri (`mpremote connect /dev/ttyUSB0 run tools/saglik_testi.py`)
- `docs/`: donanım notları
- `yedek/`: orijinal flash yedeği (git'e girmez)
