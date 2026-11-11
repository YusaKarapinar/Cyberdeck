# Konsept (Yuşa onayı, 2026-11-11)

**Atölye aleti + kablosuz keşif modu.** Cep ya da çanta boyu, masa boyu değil.

## Modlar
1. Atölye: seri monitör (başka kartı dinle), I2C/pin tarayıcı, voltaj ölçer (ADC), sinyal üreteci (PWM).
2. Keşif: Wi-Fi ağları ve BLE cihazları, sinyal gücüyle canlı liste. Yalnız pasif dinleme.
3. Sonra: not defteri (vault'a gönderim), LoRa kartuşu.

## Ekran yol haritası
- **v0 (eldeki):** 20x4 karakter LCD (HD44780 uyumlu, sarı-yeşil, paralel 16 pin, I2C sırt kartı yok). Retro terminal görünümü. Yedek: 16x2 mavi LCD.
  - 4-bit modda 6 GPIO (RS, E, D4–D7). RW toprağa: LCD hiç veri göndermez, 5 V ESP32'ye dönmez.
  - VDD 5 V, kontrast için 10k pot (V0). 3.3 V lojik seviyesi HD44780'de genelde yeterli; okunmazsa seviye dönüştürücü ya da 3.3 V LCD.
- **v1 (alınacak):** SPI renkli TFT, 2.8"–3.2" 320x240 (ILI9341 ya da ST7789). Sinyal grafikleri ve daha zengin menü için.

## Alınacaklar listesi (sonra)
- SPI TFT 2.8"–3.2" ILI9341/ST7789
- PCF8574 I2C LCD sırt kartı (LCD'yi 2 kabloya indirir), istenirse
- LiPo pil + şarj/boost modülü (TP4056 + 5 V boost ya da hazır kombine)
- microSD modülü
- Tactile buton seti (klavye matrisi)
