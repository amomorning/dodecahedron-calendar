import ezdxf
import matplotlib.pyplot as plt
import matplotlib
import calendar
import numpy as np
from matplotlib.patches import Polygon

def dxf_init():
    doc = ezdxf.readfile("template.dxf")
    msp = doc.modelspace()

    inner_up = msp.query('POLYLINE[layer=="inner_up"]') 
    inner_down = msp.query('POLYLINE[layer=="inner_down"]')  
    dot = msp.query('POLYLINE[layer=="dot"]')  
    outer = msp.query('POLYLINE[layer=="outer"]')

    return inner_up, inner_down, dot, outer

def plot_polygon(ax, dxf_polys, color):
    patches = []
    for o in dxf_polys:
        li = []
        for i in range(len(o)):
            li.append(o[i].dxf.location[0:2])
        
        polygon = Polygon(np.array(li), facecolor=color)
        ax.add_patch(polygon)
    


def plot_polyline(ax, dxf_pls, style):
    for o in dxf_pls:
        for i in range(len(o)-1):
            u = o[i].dxf.location[0:2] 
            v = o[i+1].dxf.location[0:2]
            ax.plot([u[0], v[0]], [u[1], v[1]], style)


def plot_calender(ax, dxf_polys, dx=0, dy=0, ro=0):
    global cnt
    for o in dxf_polys:
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
        ax.text(x+dx, y+dy, t, family='consolas', fontsize=14, rotation=ro, ha='center', ma='left', va='top',linespacing=1.6, wrap=False)


if  __name__ == '__main__':
    inner_up, inner_down, dot, outer = dxf_init()
    fig = plt.figure(figsize=(24, 18))
    ax = fig.add_subplot(1, 1, 1)
    plot_polyline(ax, outer, 'k')
    plot_polyline(ax, dot, 'k--')
    cnt = 1
    plot_calender(ax, inner_up, 0, 3.6, 0)
    plot_calender(ax, inner_down, 0, 4.8, 180)

    plot_polygon(ax, inner_up, '#E1ECF4')
    plot_polygon(ax, inner_down, '#E1ECF4')

    plt.axis('off')
    plt.show()
    fig.savefig("foo.pdf", bbox_inches='tight')
