#   
#   Copyright (c) 2020 Masaharu Kato. All rights reserved.
# 
#   heatmap.py
#   ヒートマップを用いた行列の可視化
#

from typing import Any, List, Optional

import matplotlib
import matplotlib.pyplot as plt

def save_heatmap(data:List[List[Any]], path:str, *, cmap:Optional[str]=None, colors:Optional[List[str]]=None):

    if colors: cmap = matplotlib.colors.ListedColormap(colors)

    fig, ax = plt.subplots()
    ax.set_xlim(0, len(data[0]))
    ax.set_ylim(0, len(data))
    im = ax.imshow(data, cmap=cmap)
    plt.savefig(path)

