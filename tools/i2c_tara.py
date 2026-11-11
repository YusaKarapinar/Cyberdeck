from machine import Pin, SoftI2C
P=[0,2,4,5,12,13,14,15,18,19,21,22,23,25,26,27,32,33]
for a in P:
  for b in P:
    if a==b: continue
    try:
      r=SoftI2C(sda=Pin(a),scl=Pin(b),freq=100000,timeout=2000).scan()
      if r and len(r)<20: print("FOUND sda",a,"scl",b,[hex(x) for x in r])
    except Exception as e: pass
print("DONE")
