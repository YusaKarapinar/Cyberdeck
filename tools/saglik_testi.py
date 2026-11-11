import gc, os, machine, esp, esp32, time, network
print("FREQ", machine.freq())
gc.collect(); print("HEAP_FREE", gc.mem_free())
try:
    print("HEAPS", esp32.idf_heap_info(esp32.HEAP_DATA))
except Exception as e: print("HEAPS ERR", e)
print("FLASH", esp.flash_size())
st=os.statvfs('/'); print("FS_FREE_KB", st[0]*st[3]//1024)
try: print("TEMP_RAW_F", esp32.raw_temperature())
except Exception as e: print("TEMP ERR", e)
w=network.WLAN(network.STA_IF); w.active(True)
nets=w.scan(); print("WIFI_COUNT", len(nets))
for n in sorted(nets,key=lambda x:-x[3])[:5]: print("  WIFI", n[0].decode('utf-8','replace') or "(gizli)", n[3], "dBm ch", n[2])
w.active(False)
try:
    import bluetooth
    found=set()
    def irq(ev,data):
        if ev==5: found.add(bytes(data[1]))
    b=bluetooth.BLE(); b.active(True); b.irq(irq); b.gap_scan(4000,30000,30000); time.sleep(4.5)
    print("BLE_DEVICES", len(found)); b.active(False)
except Exception as e: print("BLE ERR", e)
from machine import Pin, SoftI2C, ADC
for sda,scl in ((4,15),(21,22),(23,22),(4,5)):
    try:
        i=SoftI2C(sda=Pin(sda),scl=Pin(scl),freq=100000); print("I2C", sda, scl, [hex(a) for a in i.scan()])
    except Exception as e: print("I2C ERR", sda, scl, e)
print("BOOT_BTN(GPIO0)", Pin(0,Pin.IN,Pin.PULL_UP).value())
for p in (36,39,34,35): print("ADC", p, ADC(Pin(p)).read_u16())
print("DONE")
