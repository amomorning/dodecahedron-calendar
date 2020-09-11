import ezdxf
import matplotlib.pyplot as plt
import calendar

doc = ezdxf.readfile("template.dxf")
msp = doc.modelspace()

inner_up = msp.query('POLYLINE[layer=="inner_up"]') 
inner_down = msp.query('POLYLINE[layer=="inner_down"]')  
dot = msp.query('POLYLINE[layer=="dot"]')  
outer = msp.query('POLYLINE[layer=="outer"]')

f = plt.figure(figsize=(24, 18))
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

cnt = 1
print('up', len(inner_up))
for o in inner_up:
    x = 0
    y = 0
    for i in range(len(o)):
        x += o[i].dxf.location[0]
        y += o[i].dxf.location[1]
    x /= len(o)
    y /= len(o)
    # plt.scatter(x, y, color='r')
    t = str(calendar.month(2020, cnt))
    cnt += 1
    plt.text(x, y+3.6, t, family='consolas', fontsize=14, ha='center', ma='left', va='top',linespacing=1.6, wrap=False)

    # for i in range(len(o)):
    #     u = o[i].dxf.location[0:2] 
    #     v = o[(i+1)%len(o)].dxf.location[0:2]
    #     plt.plot([u[0], v[0]], [u[1], v[1]], color='k')


for o in inner_down:
    x = 0
    y = 0
    for i in range(len(o)):
        x += o[i].dxf.location[0]
        y += o[i].dxf.location[1]
    x /= len(o)
    y /= len(o)
    # plt.scatter(x, y, color='r')
    t = str(calendar.month(2020, cnt))
    cnt += 1
    plt.text(x, y+4.8, t, family='consolas', fontsize=14, rotation=180, ha='center', ma='left', va='top',linespacing=1.6, wrap=False)

    # for i in range(len(o)):
    #     u = o[i].dxf.location[0:2] 
    #     v = o[(i+1)%len(o)].dxf.location[0:2]
    #     plt.plot([u[0], v[0]], [u[1], v[1]], color='k')


plt.axis('off')
plt.show()
# f.savefig("foo.pdf", bbox_inches='tight')
