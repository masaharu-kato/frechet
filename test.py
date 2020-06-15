#   
#   Copyright (c) 2020 Masaharu Kato. All rights reserved.
# 
#   test.py
#   Fréchet 距離の計算のテストを行う
#
#   **Python 3.6 以降** で実行してください．(Python3.8を推奨)
#   標準ライブラリのみで動作します．
#

import line
import frechet
import distance


#   すべてのテストを実行します．
def main():

    test_2d_line()
    test_2d_lcurve()
    test_2d_fcurve()
    test_1d_fcurve()



def test_2d_line():
    l1 = line.Line(( 0.3,  1.0), (-0.3, -1.0))
    l2 = line.Line(( 1.0,  0.0), (-1.0,  0.0))
    print('frec_dist(l1, l2):', frechet.frechet_distance(l1, l2))



def test_2d_lcurve():
    c1 = line.CurveByLines([(1.05, 0), (0.45, 1.6), (2.7, 1.6), (2.7, 1.1), (3.7, 1.6)])
    c2 = line.CurveByLines([(0, 0), (1.05, 1.1), (2.2, 1.1), (2.2, 2.2), (1.6, 0.6), (2.7, 0.6), (3.7, 1.1)])
    print('frec_dist(c1, c2):', frechet.frechet_distance(c1, c2))
    print('frec_dist(c1, c2) (prec=0.0001):', frechet.frechet_distance(c1, c2, prec=0.0001))
    print('frec_dist(c1, c2) (n_disc=(40, 60)):', frechet.frechet_distance(c1, c2, 40, 60))
    print('frec_dist(c1, c2) (n_disc=(40, 60), prec=0.0001):', frechet.frechet_distance(c1, c2, 40, 60, prec=0.0001))



def test_2d_fcurve():

    f1 = line.CurveByFormula(lambda t: ( 2*t**2 - 3*t + 5,  3*t**2 + 4*t - 6))
    f2 = line.CurveByFormula(lambda t: (-2*t**2 -   t + 7,   -t**2 + 3*t + 5))
    f3 = line.CurveByFormula(lambda t: ( 3*t**2 -   t + 2,    t**2 + 2*t + 1))
    f4 = line.CurveByFormula(lambda t: ( 2*t**2 -   t + 4,  3*t**2 + 2*t - 5))

    print('frec_dist(f1, f2):', frechet.frechet_distance(f1, f2))
    print('frec_dist(f1, f3):', frechet.frechet_distance(f1, f3))
    print('frec_dist(f1, f4):', frechet.frechet_distance(f1, f4))



def test_1d_fcurve():
    
    fs1 = line.CurveByFormula(lambda t:  2*t**2 - 3*t + 5)
    fs2 = line.CurveByFormula(lambda t: -2*t**2 -   t + 7)
    fs3 = line.CurveByFormula(lambda t:  3*t**2 -   t + 2)
    fs4 = line.CurveByFormula(lambda t:  2*t**2 -   t + 4)

    print('frec_dist(fs1, fs2):', frechet.frechet_distance(fs1, fs2))
    print('frec_dist(fs1, fs3):', frechet.frechet_distance(fs1, fs3))
    print('frec_dist(fs1, fs4):', frechet.frechet_distance(fs1, fs4))





if __name__ == "__main__":
    main()
