import calendar
import ezdxf
import io
import json
import numpy as np
import time

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.backends.backend_pdf import PdfPages

def dxf_init():
    doc = ezdxf.readfile("template.dxf")
    msp = doc.modelspace()

    inner_up = msp.query('POLYLINE[layer=="inner_up"]') 
    inner_down = msp.query('POLYLINE[layer=="inner_down"]')  
    dot = msp.query('POLYLINE[layer=="dot"]')  
    outer = msp.query('POLYLINE[layer=="outer"]')
    

    return inner_up, inner_down, dot, outer


def get_center(dxf_poly):
    u = np.zeros(2)
    for o in dxf_poly:
        u += o.dxf.location[0:2]
    u /= len(dxf_poly)

    return u


def plot_polygons(ax, dxf_polys, t, color):
    patches = []
    for o in dxf_polys:
        center = get_center(o)
        li = []
        for i in range(len(o)):
            u = o[i].dxf.location[0:2]
            v = center + t*(u-center)
            li.append(v)
        
        polygon = Polygon(np.array(li), facecolor=color)
        ax.add_patch(polygon)
    


def plot_polyline(ax, dxf_pls, c, ls):
    for o in dxf_pls:
        for i in range(len(o)-1):
            u = o[i].dxf.location[0:2] 
            v = o[i+1].dxf.location[0:2]
            ax.plot([u[0], v[0]], [u[1], v[1]], c=c, ls=ls, linewidth=1)


def plot_calendar(ax, dxf_polys, dx=0, dy=0, ro=0):
    global cnt, year
    for o in dxf_polys:
        u = get_center(o)
        # plt.scatter(u[0], u[1], color='r')
        t = str(calendar.month(year, cnt))
        cnt += 1
        ax.text(u[0]+dx, u[1]+dy, t, family='consolas', fontsize=13, rotation=ro, ha='center', ma='left', va='top',linespacing=1.6, wrap=False)


def gen_calendar(
    style = 'double',
    maincolor = '#E1ECF4FF',
    backcolor='#FFFFFFFF',
    percolor = '#E45C18FF'):
    inner_up, inner_down, dot, outer = dxf_init()
    fig = plt.figure(figsize=(24, 18))
    ax = fig.add_subplot(1, 1, 1)
    plot_polyline(ax, outer, 'gray', '-')
    plot_polyline(ax, dot, 'gray', ':')

    plot_calendar(ax, inner_up, 0, 3.6, 0)
    plot_calendar(ax, inner_down, 0, 4.4, 180)

    if (style == 'filled'):
        plot_polygons(ax, inner_up, 1, maincolor)
        plot_polygons(ax, inner_down, 1, maincolor)
    if (style == 'flipped'):
        plot_polygons(ax, inner_up, 1, maincolor)
        plot_polygons(ax, inner_up, 0.8, backcolor)
        plot_polygons(ax, inner_down, 0.8, maincolor)
    if (style == 'double'):
        plot_polygons(ax, inner_up, 1, maincolor)
        plot_polygons(ax, inner_up, 0.8, backcolor)
        plot_polygons(ax, inner_down, 1, maincolor)
        plot_polygons(ax, inner_down, 0.8, backcolor) 


    plt.axis('off')
    pdfio = io.BytesIO()
    with PdfPages(pdfio) as pdf:
        fig.savefig(pdf, format="pdf", bbox_inches='tight')
        pass
    return pdfio.getvalue()
    



if  __name__ == '__main__':
    year = 2020
    cnt = 1
    gen_calendar()
    plt.show()
