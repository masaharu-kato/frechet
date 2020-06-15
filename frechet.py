#   
#   Copyright (c) 2020 Masaharu Kato. All rights reserved.
# 
#   frechet.py
#   Fréchet 距離の計算
#

from typing import Any, Callable, List
import line
import distance

DistFunc = Callable[[line.Point, line.Point], float]

# frechet 距離を求める
def frechet_distance(
    l1:line.Line,
    l2:line.Line,
    n_disc_l1:int = 100,
    n_disc_l2:int = 100,
    *,
    prec :float = 0.001,
    distance_func:DistFunc = distance.euclid,
) -> float:

    dist_mat = distance_matrix(l1, l2, n_disc_l1, n_disc_l2, distance_func)
    return optimize_ep(dist_mat[0][0], lambda ep: is_valid_ep(dist_mat, ep), prec)



# l1, l2 を離散化し，距離の行列(2次元配列)を求める
def distance_matrix(l1:line.Line, l2:line.Line, nd1:int, nd2:int, distance_func:DistFunc) -> List[List[float]]:

    ld1 = list(line.discretize(l1, nd1))
    ld2 = list(line.discretize(l2, nd2))
    
    return [[distance_func(p1, p2) for p2 in ld2] for p1 in ld1]


# free space を求める
def free_space(dist_mat:List[List[float]], ep:float) -> List[List[bool]]:
    return map_mat(dist_mat, lambda v: v < ep)


# reachable space を求める
def reachable_space(fs_mat:List[List[bool]]) -> List[List[bool]]:
    len1 = len(fs_mat)
    len2 = len(fs_mat[0])
    re_mat = [[False for _ in range(len2)] for _ in range(len1)] # 全Falseの配列を作成

    # 再帰的に探索を行う
    def explore(i1:int, i2:int):
        if i1 >= len1 or i2 >= len2: return # 範囲外
        if re_mat[i1][i2]: return # 探索済み
        if not fs_mat[i1][i2]: return # 領域外
        re_mat[i1][i2] = True # 探索(到達可能として記録)
        explore(i1, i2+1) # 上側
        explore(i1+1, i2) # 右側

    explore(0, 0)

    return re_mat


# ep が真のfrechet距離以上か調べる
def is_valid_ep(dist_mat:List[List[float]], ep:float) -> bool:
    return reachable_space(free_space(dist_mat, ep))[-1][-1]


# ep値を最適化する
def optimize_ep(min_ep:float, is_valid:Callable[[float], bool], prec:float) -> float:
    
    ep = min_ep
    d_ep_init = ep / 2
    d_ep = d_ep_init
    last_res = False

    while True:
        res = is_valid(ep)
        if res:
            if ep == min_ep or d_ep <= prec: return ep
            d_ep = d_ep / 2 if last_res else d_ep_init
            ep -= d_ep
        else:
            d_ep = d_ep_init if last_res else d_ep * 2
            ep += d_ep

        last_res = res



# 2次元配列の各要素に関数を適用する
def map_mat(mat:List[List[Any]], func:Callable[[Any], Any]) -> List[List[Any]]:
    return [list(map(func, l)) for l in mat]

