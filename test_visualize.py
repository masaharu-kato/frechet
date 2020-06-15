#   
#   Copyright (c) 2020 Masaharu Kato. All rights reserved.
# 
#   test_visualize.py
#   Fréchet 距離の計算の可視化テストを行う
#
#   **Python 3.6 以降** で実行してください．(Python3.8を推奨)
#   このテストには，可視化のために matplotlib が必要です．
#

import line
import frechet
import distance
import heatmap


#   すべてのテストを実行します．
def main():
    test_2d_lcurve()
    test_2d_lcurve_verbose()



def test_2d_lcurve():
    c1 = line.CurveByLines([(1.05, 0), (0.45, 1.6), (2.7, 1.6), (2.7, 1.1), (3.7, 1.6)])
    c2 = line.CurveByLines([(0, 0), (1.05, 1.1), (2.2, 1.1), (2.2, 2.2), (1.6, 0.6), (2.7, 0.6), (3.7, 1.1)])
    print('frec_dist(c1, c2):', frechet.frechet_distance(c1, c2))



def test_2d_lcurve_verbose():
    c1 = line.CurveByLines([(1.05, 0), (0.45, 1.6), (2.7, 1.6), (2.7, 1.1), (3.7, 1.6)])
    c2 = line.CurveByLines([(0, 0), (1.05, 1.1), (2.2, 1.1), (2.2, 2.2), (1.6, 0.6), (2.7, 0.6), (3.7, 1.1)])
    
    dist_mat = frechet.distance_matrix(c1, c2, 100, 150, distance.euclid)
    fs_mat = frechet.free_space(dist_mat, 1.06)
    re_mat = frechet.reachable_space(fs_mat)
    heatmap.save_heatmap(fs_mat, 'out_free_space.png', colors=['#F22', '#FFF'])
    heatmap.save_heatmap(re_mat, 'out_reachable_space.png', colors=['#F22', '#FFF'])



if __name__ == "__main__":
    main()
