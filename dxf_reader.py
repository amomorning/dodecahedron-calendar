import ezdxf
import matplotlib.pyplot as plt


doc = ezdxf.readfile("template.dxf")
msp = doc.modelspace()

inner_up = msp.query('POLYLINE[layer=="inner_up"]') 
inner_down = msp.query('POLYLINE[layer=="inner_down"]')  
dot = msp.query('POLYLINE[layer=="dot"]')  
outer = msp.query('POLYLINE[layer=="outer"]')

for o in outer:
    for i in range(len(o)-1):
        u = o[i].dxf.location[0:2] 
        v = o[i+1].dxf.location[0:2]
        plt.plot([u[0], v[0]], [u[1], v[1]], color='k')
print('dot', len(dot))
for o in dot:
    u = o[0].dxf.location[0:2]
    v = o[1].dxf.location[0:2]
    print(u, v)
    plt.plot([u[0], v[0]], [u[1], v[1]], 'k--')

plt.show()
