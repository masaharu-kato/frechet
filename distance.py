#   
#   Copyright (c) 2020 Masaharu Kato. All rights reserved.
# 
#   distance.py
#   ユークリッド距離の計算
#

from typing import Optional, Iterable

# euclid distance
def euclid(vec1:Iterable, vec2:Optional[Iterable]=None) -> float:
    return euclid_sq(vec1, vec2) ** 0.5

# squared value of euclid distance
def euclid_sq(vec1:Iterable, vec2:Optional[Iterable]=None) -> float:
    if vec2 is None:
        if isinstance(vec1, Iterable):
            return sum(elm ** 2 for elm in vec1)
        return vec1 ** 2
    return euclid_sq(diff(vec1, vec2))

# difference of vectors
def diff(vec1, vec2) -> Iterable:
    if isinstance(vec1, Iterable) and isinstance(vec2, Iterable):
        return (elm2 - elm1 for elm1, elm2 in zip(vec1, vec2))
    return vec2 - vec1
