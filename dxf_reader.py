import ezdxf

doc = ezdxf.readfile("template.dxf")
msp = doc.modelspace()

inner_up = msp.query('POLYLINE[layer=="inner_up"]') 
inner_down = msp.query('POLYLINE[layer=="inner_down"]')  
dot = msp.query('POLYLINE[layer=="dot"]')  
outer = msp.query('POLYLINE[layer=="outer"]')


for v in outer[0]:
    print(v.dxf.location)
