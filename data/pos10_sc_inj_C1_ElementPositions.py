import os, sys, argparse, math, base64, zlib, struct

if sys.version_info < (3,0):
    range = xrange

vertices = []
numVertices = [74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74]
vertices_base64 = "eJzt1W2oZVUdwGEr0qRRNJspdERtSgrrkNmrDN1DqBGlqdAbFFlNgVEYNdkrghmYKZoYWCRoERVZQRSWMnQjKlELgySLpKQXjCiKMo1MLTr7t477udG3vrk+DNzfPbPvWue/Ns9++/2vdeeG5Qk7z7/k4gt+uXHRux573uEnXjd+v/MZZ77onkN/sfG3x3507xd+/b3Rr33Zq3/3/ut+vvHgf9ato7/g9Fs/c84FP93YuWP3md+4/LbRj5x+7vf1R/zn3x9tfHF6Xv3e6e8dMf39+iXT/tpv/YDXPv6EYz93/m7P95HV5zf9/HSezZ08/5+r82xey34OX+1/czf7f+7q581jOO/nV/9/84DpfPUnrv7e5gHb5t/n9tX+Nq/j+5/Os3n+xW/8/nefffPusZ/p8y+fzlc/Znr+T6bz1b8+7efO6Xz1U6b9HzSdr37c9PMzpt/XD12dZ/Oa6Xn1o1bn2Xz89Pfrd037O2zab/3Tv7vp41d8/mf7Ol/9yOn8O/n8t6b7cCzPv3m6fzewn0dN8ziN/e+a5vc8zvuJad5HT+erHzzdjxdum3+fh0z36Wl759//f1+L5XTOjW+ffPyb3nj4b/fVj5qec8c7Hzr3xfK46e9ePXvvFsvvTPv88uy9WyxfM53r3u0PvYeL5UnT9/DE2b1dLBerc258bHbPF8vXTffywNl7sVi+dXXOjYNm79FiefyV99/3j7P+yHu3WN6wOs/m0Xz+suleLnj+1dO9vJH9/Hl1ns3Xs//Dprm+dMf8vJdM9+C50/nq+0/35u3b5t/ntumeXbJ3/v1P59k8/e49N9/04z/vru+aPv++dz507ovls6fnv2P23i2Wt077+dDsvVssz572/+vtD72Hi+Wrpnv5mNm9/fccV+fZvGB2z/993u7l7L1YLH843csDZ+/RYvmYI2/ZsePeu3nvFsvnT/fvWD5/xnT/TuT5b57u3+3s5/bp/u1l//e/fDW/PTvm5/3ANO8zp/PV73v66n5cu23+fe4/3aeD3z3//vf7n+th7x72brUe9m61/l/enXLdX++/7b03TfNce1fXu7re1fWurnd1vavrXV3v6npX17u63tX1rq53db2r611d7+p6V9c75jW8q+tdXe/qelfXu7rejTlO9zLvxnnxrq53db2r611d7+p6V9e7ut7V9a6ud2OOeDef13qddeCOC0/YfP947+x6V9e7ut7V9a6ud3W9q+tdXe/qelfXu7re1fWurnd1vavrXV3v6nrHvIZ3Yz94V9e7ut7V9a6ud3W9q+tdXe/qejfuCd7V9a6ud3W9q+tdXe/qelfXu/m81usX5376+tN2/XKLd3W9q+tdXe/qelfXu7re1fWurnd1vavrXV3v6npX17u63tX1rq53db1jXsO7ut7V9a6ud3W9q+vdmCPejfPiXV3v6npX17u63tX1rq53db2r611d78Yc8W4+r/W67NJrL3/d036zxbu63tX1rq53db2r611d7+p6V9e7ut7V9a6ud3W9q+tdXe/qelfXu7reMa/h3dgP3tX1rq53db2r611d7+p6V9e7ut6Ne4J3db2r611d7+p6V9e7ut7V9W4+r/U68dUP3vXMq/+0xbu63tX1rq53db2r611d7+p6V9e7ut7V9a6ud3W9q+tdXe/qelfXu7reMa/hXV3v6npX17u63tX1bswR78Z58a6ud3W9q+tdXe/qelfXu7re1fWurndjjng3n9d67d39lmuedd49W7yr611d7+p6V9e7ut7V9a6ud3W9q+tdXe/qelfXu7re1fWurnd1vavrHfMa3o394F1d7+p6V9e7ut7V9a6ud3W9q+vduCd4V9e7ut7V9a6ud3W9q+tdXe/m81qvYz784iNe/PQHtnhX17u63tX1rq53db2r611d7+p6V9e7ut7V9a6ud3W9q+tdXe/qelfXO+Y1vKvrXV3v6npX17u63o054t04L97V9a6ud3W9q+tdXe/qelfXu7re1fVuzBHv5vNar8/840u3f/I9j17qXV3v6npX17u63tX1rq53db2r611d7+p6V9e7ut7V9a6ud3W9q+tdXe+Y1/Bu7Afv6npX17u63tX1rq53db2r611d78Y9wbu63tX1rq53db2r611d7+p6N5/Xep161bl3bTzykPHe5V1d7+p6V9e7ut7V9a6ud3W9q+tdXe/qelfXu7re1fWurnd1vavrXV3vmNfwrq53db2r611d7+p6N+aId+O8eFfXu7re1fWurnd1vavrXV3v6npX17sxR7ybz2u9bn3voa/91Enr986ud3W9q+tdXe/qelfXu7re1fWurnd1vavrXV3v6npX17u63tX1rq53zGt4N/aDd3W9q+tdXe/qelfXu7re1fWurnfjnuBdXe/qelfXu7re1fWurnd1vZvPa71uufKrrzr44u1bvKvrXV3v6npX17u63tX1rq53db2r611d7+p6V9e7ut7V9a6ud3W9q+sd8xre1fWurnd1vavrXV3vxhzxbpwX7+p6V9e7ut7V9a6ud3W9q+tdXe/qejfmiHfzea3XqXtf9oOzf7h+7+x6V9e7ut7V9a6ud3W9q+tdXe/qelfXu7re1fWurnd1vavrXV3v6nrHvIZ3Yz94V9e7ut7V9a6ud3W9q+tdXe/qejfuCd7V9a6ud3W9q+tdXe/qelfXu/m81uslV/zhxjsOO2KLd3W9q+tdXe/qelfXu7re1fWurnd1vavrXV3v6npX17u63tX1rq53db1jXsO7ut7V9a6ud3W9q+vdmCPejfPiXV3v6npX17u63tX1rq53db2r611d78Yc8W4+r/W65ZwLdz//lev3zq53db2r611d7+p6V9e7ut7V9a6ud3W9q+tdXe/qelfXu7re1fWurnfMa3g39oN3db2r611d7+p6V9e7ut7V9a6ud+Oe4F1d7+p6V9e7ut7V9a6ud3W9m89rvfbceNhVrzjt6C3e1fWurnd1vavrXV3v6npX17u63tX1rq53db2r611d7+p6V9e7ut7V9Y55De/qelfXu7re1fWurndjjng3zot3db2r611d7+p6V9e7ut7V9a6ud3W9G3PEu/m81uuzz3nDKy84Z/3e2fWurnd1vavrXV3v6npX17u63tX1rq53db2r611d7+p6V9e7ut7V9Y55De/GfvCurnd1vavrXV3v6npX17u63tX1btwTvKvrXV3v6npX17u63tX1rq5383mt15NOPv62fY/btcW7ut7V9a6ud3W9q+tdXe/qelfXu7re1fWurnd1vavrXV3v6npX17u63jGv4V1d7+p6V9e7ut7V9W7MEe/GefGurnd1vavrXV3v6npX17u63tX1rq53Y454N5/Xeu352nmX/v6E9Xtn17u63tX1rq53db2r611d7+p6V9e7ut7V9a6ud3W9q+tdXe/qelfXO+Y1vBv7wbu63tX1rq53db2r611d7+p6V9e7cU/wrq53db2r611d7+p6V9e7ut7N57Vev/rOaduefPtTtnhX17u63tX1rq53db2r611d7+p6V9e7ut7V9a6ud3W9q+tdXe/qelfXO+Y1vKvrXV3v6npX17u63o054t04L97V9a6ud3W9q+tdXe/qelfXu7re1fVuzBHv5vNarycdf9X3z/j7+r2z611d7+p6V9e7ut7V9a6ud3W9q+tdXe/qelfXu7re1fWurnd1vavrHfMa3o394F1d7+p6V9e7ut7V9a6ud3W9q+vduCd4V9e7ut7V9a6ud3W9q+tdXe/m81qva5ZvO+niTz11i3d1vavrXV3v6npX17u63tX1rq53db2r611d7+p6V9e7ut7V9a6ud3W9Y17Du7re1fWurnd1vavr3Zgj3o3z4l1d7+p6V9e7ut7V9a6ud3W9q+tdXe/GHPFuPq/1+tVXrn/gm/vW751d7+p6V9e7ut7V9a6ud3W9q+tdXe/qelfXu7re1fWurnd1vavrXV3vmNfwbuwH7+p6V9e7ut7V9a6ud3W9q+tdXe/GPcG7ut7V9a6ud3W9q+tdXe/qejef13qd9a2LPviX1x+3xbu63tX1rq53db2r611d7+p6V9e7ut7V9a6ud3W9q+tdXe/qelfXu7reMa/hXV3v6npX17u63tX1bswR78Z58a6ud3W9q+tdXe/qelfXu7re1fWurndjjnhX/xfltF4q"
triangles = [[ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38], [ 0, 2, 1, 1, 2, 38, 2, 39, 38, 0, 3, 2, 2, 3, 39, 3, 40, 39, 0, 4, 3, 3, 4, 40, 4, 41, 40, 0, 5, 4, 4, 5, 41, 5, 42, 41, 0, 6, 5, 5, 6, 42, 6, 43, 42, 0, 7, 6, 6, 7, 43, 7, 44, 43, 0, 8, 7, 7, 8, 44, 8, 45, 44, 0, 9, 8, 8, 9, 45, 9, 46, 45, 0, 10, 9, 9, 10, 46, 10, 47, 46, 0, 11, 10, 10, 11, 47, 11, 48, 47, 0, 12, 11, 11, 12, 48, 12, 49, 48, 0, 13, 12, 12, 13, 49, 13, 50, 49, 0, 14, 13, 13, 14, 50, 14, 51, 50, 0, 15, 14, 14, 15, 51, 15, 52, 51, 0, 16, 15, 15, 16, 52, 16, 53, 52, 0, 17, 16, 16, 17, 53, 17, 54, 53, 0, 18, 17, 17, 18, 54, 18, 55, 54, 0, 19, 18, 18, 19, 55, 19, 56, 55, 0, 20, 19, 19, 20, 56, 20, 57, 56, 0, 21, 20, 20, 21, 57, 21, 58, 57, 0, 22, 21, 21, 22, 58, 22, 59, 58, 0, 23, 22, 22, 23, 59, 23, 60, 59, 0, 24, 23, 23, 24, 60, 24, 61, 60, 0, 25, 24, 24, 25, 61, 25, 62, 61, 0, 26, 25, 25, 26, 62, 26, 63, 62, 0, 27, 26, 26, 27, 63, 27, 64, 63, 0, 28, 27, 27, 28, 64, 28, 65, 64, 0, 29, 28, 28, 29, 65, 29, 66, 65, 0, 30, 29, 29, 30, 66, 30, 67, 66, 0, 31, 30, 30, 31, 67, 31, 68, 67, 0, 32, 31, 31, 32, 68, 32, 69, 68, 0, 33, 32, 32, 33, 69, 33, 70, 69, 0, 34, 33, 33, 34, 70, 34, 71, 70, 0, 35, 34, 34, 35, 71, 35, 72, 71, 0, 36, 35, 35, 36, 72, 36, 73, 72, 0, 1, 36, 36, 1, 73, 1, 38, 73, 37, 38, 39, 37, 39, 40, 37, 40, 41, 37, 41, 42, 37, 42, 43, 37, 43, 44, 37, 44, 45, 37, 45, 46, 37, 46, 47, 37, 47, 48, 37, 48, 49, 37, 49, 50, 37, 50, 51, 37, 51, 52, 37, 52, 53, 37, 53, 54, 37, 54, 55, 37, 55, 56, 37, 56, 57, 37, 57, 58, 37, 58, 59, 37, 59, 60, 37, 60, 61, 37, 61, 62, 37, 62, 63, 37, 63, 64, 37, 64, 65, 37, 65, 66, 37, 66, 67, 37, 67, 68, 37, 68, 69, 37, 69, 70, 37, 70, 71, 37, 71, 72, 37, 72, 73, 37, 73, 38]]
decoration = [[ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 15.000000], [ 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.199000], [ 0.000000, 0.000000, 0.006530, 0.000000, 0.000000, 0.486530], [ 0.000000, 0.000000, 0.630050, 0.000000, 0.000000, 0.988182], [ 0.000000, 0.000000, 1.405810, 0.000000, 0.000000, 1.885810], [ 0.000000, 0.000000, 2.683399, 0.000000, 0.000000, 4.002197], [ 0.000000, 0.000000, 4.066999, 0.000000, 0.000000, 5.385797], [ 0.000000, 0.000000, 5.450599, 0.000000, 0.000000, 6.769397], [ 0.000000, 0.000000, 6.834199, 0.000000, 0.000000, 8.152997], [ 0.000000, 0.000000, 8.217799, 0.000000, 0.000000, 9.536597], [ 0.000000, 0.000000, 9.601399, 0.000000, 0.000000, 10.920197], [ 0.000000, 0.000000, 10.984999, 0.000000, 0.000000, 12.303797], [ 0.000000, 0.000000, 12.368599, 0.000000, 0.000000, 13.687397]]

color = [0, 6, 5, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6]

index_base64 = 'eJylVlFv2zYQfs+vYGUMUACLcjIUKBLbgOMGWIBkCdJgQDfsgSZPFguJ9CjKrjf0v/dIKrYk28G2CrAl6u6+++6Od9T43cfH+cvnp1uS27KYno3DjeA1zoGJ8OiXJViGWnaVwF+1XE+iuVYWlE1etiuICA+rSWThq00dzDXhOTMV2Elts+RDRNLp2R7OSlvA9IYttoVW9EtFKlauCkAcAeM0SPfa75KEtHSTpCWruJErSyrDJ5Hjd5WmXCi6COpfKsp1meZMCVpKJTMJIrmglwgTTcdpMP6vaJwp5Zn8fwgtS/1DAItdOo5j2G07g+5yRRmShRZb8k9H4C69BpMVenNFcikEqOsDjY0UNr8iF6PRT4fCHOQyt6ekJTNLqa7I6FC0YkJItTyQfTvrLAcGlAAzZ2rNqiP0f4Cc1TXPE8at1EgR6wp9Jq9PmOZ9VsdpaJCxS2jzigd6UkyiNl9XoCBq9PrVWjNDGtsJEZrXJbYSXYK9LcA93mzvRNyFPL/uWIPCBANaK9iQm9nN5/vHX+mtfxkH5CGxpgY063o1wCx84uCNs1r5NJD4vJdjp1s1Wm0X3jIO3tvY7krTma8tYaRwBTjIvAP1kh7ok5bK3jtBHD2WSkbDjvg34Fabn+PRkCRY0iEZnQ8DufPD6qap90CFzLK66tOf68Ij0Q+I0vwdAQkQ1Qp4XSDnExgXzjz8vUFkaXSthDc6AYQILqaT2VRkZjh51hYrR+asBMOOppZ7Uc8JmgbLYBhH4R452uj2gdmcPt0NyXtc9BJOfwej4xO5Ds4os5bx3B0NRhe7nZexojpWnMZokwMUTwa4rNzmm5DLUS94F065LaHKUToYfJy9zAaD615+yEsOJJOmsjhVDEJb8G1FFkCw9AI7nbgaymxLNrnkOfGA+FaWK20sJb+AAbKBZk1YUXgVqDqeOnv/XjNsSnrnLR5QOY4wl+4X+DbZGrZ6C8vx4FH7TdaE8QkssRiKxamJjzrzq6aayNbuwgw8MTLn6VR2Gxi/DYLfP0Z/9vJ7kGvcIEay4qLf7hbPUWbEQyOP/XFfG7iITrfgPrQdLN1IA5mrETpwc+nQqs2Wvhqi9g7jX5pQKGVVyTW81XL00u3/8NeL4Fu/EQ1gwCpEu1fF86ozWF+HZWvAxm2kMDKpqdWzH+v3Wq/i0/PXw9FwAsQthh12uHeeoZJ/w+7NRiqhNxTP2Ns1uJla4UcaIuBZ4vSi4Rsj/5Wh1+z7dPf9V8c4DYfg2H/4Tb8DrvXVsg=='

def decodeVertices():
    vertices_binary = zlib.decompress(base64.b64decode(vertices_base64))
    k = 0
    for i in range(len(numVertices)):
        current = []
        for j in range(numVertices[i] * 3):
            current.append(float(struct.unpack('=d', vertices_binary[k:k+8])[0]))
            k += 8
        vertices.append(current)

def dot(a, b):
    return sum(a[i]*b[i] for i in range(len(a)))

def normalize(a):
    length = math.sqrt(dot(a, a))
    for i in range(3):
        a[i]/=length
    return a

def distance(a, b):
    c = [0] * 2
    for i in range(len(a)):
        c[i] = a[i] - b[i]
    return math.sqrt(dot(c, c))

def cross(a, b):
    c = [0, 0, 0]
    c[0] = a[1]*b[2] - a[2]*b[1]
    c[1] = a[2]*b[0] - a[0]*b[2]
    c[2] = a[0]*b[1] - a[1]*b[0]
    return c

class Quaternion:
    def __init__(self, values):
        self.R = values

    def __str__(self):
        return str(self.R)

    def __mul__(self, other):
        imagThis = self.imag()
        imagOther = other.imag()
        cro = cross(imagThis, imagOther)

        ret = ([self.R[0] * other.R[0] - dot(imagThis, imagOther)] +
               [self.R[0] * imagOther[0] + other.R[0] * imagThis[0] + cro[0],
                self.R[0] * imagOther[1] + other.R[0] * imagThis[1] + cro[1],
                self.R[0] * imagOther[2] + other.R[0] * imagThis[2] + cro[2]])

        return Quaternion(ret)

    def imag(self):
        return self.R[1:]

    def conjugate(self):
        ret = [0] * 4
        ret[0] = self.R[0]
        ret[1] = -self.R[1]
        ret[2] = -self.R[2]
        ret[3] = -self.R[3]

        return Quaternion(ret)

    def inverse(self):
        return self.conjugate()

    def rotate(self, vec3D):
        quat = Quaternion([0.0] + vec3D)
        conj = self.conjugate()

        ret = self * (quat * conj)
        return ret.R[1:]

def getQuaternion(u, ref):
    u = normalize(u)
    ref = normalize(ref)
    axis = cross(u, ref)
    normAxis = math.sqrt(dot(axis, axis))

    if normAxis < 1e-12:
        if math.fabs(dot(u, ref) - 1.0) < 1e-12:
            return Quaternion([1.0, 0.0, 0.0, 0.0])

        return Quaternion([0.0, 1.0, 0.0, 0.0])

    axis = normalize(axis)
    cosAngle = math.sqrt(0.5 * (1 + dot(u, ref)))
    sinAngle = math.sqrt(1 - cosAngle * cosAngle)

    return Quaternion([cosAngle, sinAngle * axis[0], sinAngle * axis[1], sinAngle * axis[2]])

def exportVTK():
    vertices_str = ""
    triangles_str = ""
    color_str = ""
    cellTypes_str = ""
    startIdx = 0
    vertexCounter = 0
    cellCounter = 0
    lookup_table = []
    lookup_table.append([0.5, 0.5, 0.5, 0.5])
    lookup_table.append([1.0, 0.847, 0.0, 1.0])
    lookup_table.append([1.0, 0.0, 0.0, 1.0])
    lookup_table.append([0.537, 0.745, 0.525, 1.0])
    lookup_table.append([0.5, 0.5, 0.0, 1.0])
    lookup_table.append([1.0, 0.541, 0.0, 1.0])
    lookup_table.append([0.0, 0.0, 1.0, 1.0])

    decodeVertices()

    for i in range(len(vertices)):
        for j in range(0, len(vertices[i]), 3):
            vertices_str += ("%f %f %f\n" %(vertices[i][j], vertices[i][j+1], vertices[i][j+2]))
            vertexCounter += 1

        for j in range(0, len(triangles[i]), 3):
            triangles_str += ("3 %d %d %d\n" % (triangles[i][j] + startIdx, triangles[i][j+1] + startIdx, triangles[i][j+2] + startIdx))
            cellTypes_str += "5\n"
            tmp_color = lookup_table[color[i]]
            color_str += ("%f %f %f %f\n" % (tmp_color[0], tmp_color[1], tmp_color[2], tmp_color[3]))
            cellCounter += 1
        startIdx = vertexCounter

    fh = open('pos10_sc_inj_C1_ElementPositions.vtk','w')
    fh.write("# vtk DataFile Version 2.0\n")
    fh.write("test\nASCII\n\n")
    fh.write("DATASET UNSTRUCTURED_GRID\n")
    fh.write("POINTS " + str(vertexCounter) + " float\n")
    fh.write(vertices_str)
    fh.write("CELLS " + str(cellCounter) + " " + str(cellCounter * 4) + "\n")
    fh.write(triangles_str)
    fh.write("CELL_TYPES " + str(cellCounter) + "\n")
    fh.write(cellTypes_str)
    fh.write("CELL_DATA " + str(cellCounter) + "\n")
    fh.write("COLOR_SCALARS type 4\n")
    fh.write(color_str + "\n")
    fh.close()

def getNormal(tri_vertices):
    vec1 = [tri_vertices[1][0] - tri_vertices[0][0],
            tri_vertices[1][1] - tri_vertices[0][1],
            tri_vertices[1][2] - tri_vertices[0][2]]
    vec2 = [tri_vertices[2][0] - tri_vertices[0][0],
            tri_vertices[2][1] - tri_vertices[0][1],
            tri_vertices[2][2] - tri_vertices[0][2]]
    return normalize(cross(vec1,vec2))

def exportWeb(bgcolor):
    lookup_table = []
    lookup_table.append([0.5, 0.5, 0.5])
    lookup_table.append([1.0, 0.847, 0.0])
    lookup_table.append([1.0, 0.0, 0.0])
    lookup_table.append([0.537, 0.745, 0.525])
    lookup_table.append([0.5, 0.5, 0.0])
    lookup_table.append([1.0, 0.541, 0.0])
    lookup_table.append([0.0, 0.0, 1.0])

    decodeVertices()

    mesh = "'data:"
    mesh += "{"
    mesh += "\"autoClear\":true,"
    mesh += "\"clearColor\":[0.0000,0.0000,0.0000],"
    mesh += "\"ambientColor\":[0.0000,0.0000,0.0000],"
    mesh += "\"gravity\":[0.0000,-9.8100,0.0000],"
    mesh += "\"cameras\":["
    mesh += "{"
    mesh += "\"name\":\"Camera\","
    mesh += "\"id\":\"Camera\","
    mesh += "\"position\":[21.7936,2.2312,-85.7292],"
    mesh += "\"rotation\":[0.0432,-0.1766,-0.0668],"
    mesh += "\"fov\":0.8578,"
    mesh += "\"minZ\":10.0000,"
    mesh += "\"maxZ\":10000.0000,"
    mesh += "\"speed\":1.0000,"
    mesh += "\"inertia\":0.9000,"
    mesh += "\"checkCollisions\":false,"
    mesh += "\"applyGravity\":false,"
    mesh += "\"ellipsoid\":[0.2000,0.9000,0.2000]"
    mesh += "}],"
    mesh += "\"activeCamera\":\"Camera\","
    mesh += "\"lights\":["
    mesh += "{"
    mesh += "\"name\":\"Lamp\","
    mesh += "\"id\":\"Lamp\","
    mesh += "\"type\":0.0000,"
    mesh += "\"position\":[4.0762,34.9321,-63.5788],"
    mesh += "\"intensity\":1.0000,"
    mesh += "\"diffuse\":[1.0000,1.0000,1.0000],"
    mesh += "\"specular\":[1.0000,1.0000,1.0000]"
    mesh += "}],"
    mesh += "\"materials\":[],"
    mesh += "\"meshes\":["

    for i in range(len(triangles)):
        vertex_list = []
        indices_list = []
        normals_list = []
        color_list = []
        for j in range(0, len(triangles[i]), 3):
            tri_vertices = []
            idcs = triangles[i][j:j + 3]
            tri_vertices.append(vertices[i][3 * idcs[0]:3 * (idcs[0] + 1)])
            tri_vertices.append(vertices[i][3 * idcs[1]:3 * (idcs[1] + 1)])
            tri_vertices.append(vertices[i][3 * idcs[2]:3 * (idcs[2] + 1)])
            indices_list.append(','.join(str(n) for n in range(len(vertex_list),len(vertex_list) + 3)))
            # left hand order!
            vertex_list.append(','.join("%.5f" % (round(n,5) + 0.0) for n in tri_vertices[0]))
            vertex_list.append(','.join("%.5f" % (round(n,5) + 0.0) for n in tri_vertices[2]))
            vertex_list.append(','.join("%.5f" % (round(n,5) + 0.0) for n in tri_vertices[1]))
            normal = getNormal(tri_vertices)
            normals_list.append(','.join("%.5f" % (round(n,5) + 0.0) for n in normal * 3))
            color_list.append(','.join([str(n) for n in lookup_table[color[i]]] * 3))
        mesh += "{"
        mesh += "\"name\":\"element_" + str(i) + "\","
        mesh += "\"id\":\"element_" + str(i) + "\","
        mesh += "\"position\":[0.0,0.0,0.0],"
        mesh += "\"rotation\":[0.0,0.0,0.0],"
        mesh += "\"scaling\":[1.0,1.0,1.0],"
        mesh += "\"isVisible\":true,"
        mesh += "\"isEnabled\":true,"
        mesh += "\"useFlatShading\":false,"
        mesh += "\"checkCollisions\":false,"
        mesh += "\"billboardMode\":0,"
        mesh += "\"receiveShadows\":false,"
        mesh += "\"positions\":[" + ','.join(vertex_list) + "],"
        mesh += "\"normals\":[" + ','.join(normals_list) + "],"
        mesh += "\"indices\":[" + ','.join(indices_list) + "],"
        mesh += "\"colors\":[" + ','.join(color_list) + "],"
        mesh += "\"subMeshes\":["
        mesh += "{"
        mesh += "\"materialIndex\":0,"
        mesh += " \"verticesStart\":0,"
        mesh += " \"verticesCount\":" + str(len(triangles[i])) + ","
        mesh += " \"indexStart\":0,"
        mesh += " \"indexCount\":" + str(len(triangles[i])) + ""
        mesh += "}]"
        mesh += "}"
        mesh += ","

        del normals_list[:]
        del vertex_list[:]
        del color_list[:]
        del indices_list[:]

    mesh = mesh[:-1] + "]"
    mesh += "}'"
    index_compressed = base64.b64decode(index_base64)
    index = str(zlib.decompress(index_compressed))
    if (len(bgcolor) == 3):
        mesh += ";\n            "
        mesh += "scene.clearColor = new BABYLON.Color3(%f, %f, %f)" % (bgcolor[0], bgcolor[1], bgcolor[2])

    index = index.replace('##DATA##', mesh)
    fh = open('pos10_sc_inj_C1_ElementPositions.html','w')
    fh.write(index)
    fh.close()

def computeMinAngle(idx, curAngle, positions, connections, check):
    matrix = [[-math.cos(curAngle), -math.sin(curAngle)], [math.sin(curAngle), -math.cos(curAngle)]]

    minAngle = 2 * math.pi
    nextIdx = -1

    for j in connections[idx]:
        direction = [positions[j][0] - positions[idx][0],
                     positions[j][1] - positions[idx][1]]
        direction = [dot(matrix[0],direction), dot(matrix[1],direction)]

        if math.fabs(dot([1.0, 0.0], direction) / distance(positions[j], positions[idx]) - 1.0) < 1e-6: continue

        angle = math.fmod(math.atan2(direction[1],direction[0]) + 2 * math.pi, 2 * math.pi)

        if angle < minAngle:
            nextIdx = j
            minAngle = angle
        if angle == minAngle and check:
            dire =  [positions[j][0] - positions[idx][0],
                     positions[j][1] - positions[idx][1]]
            minA0 = math.atan2(dire[1], dire[0])
            minA1 = computeMinAngle(nextIdx, minA0, positions, connections, False)
            minA2 = computeMinAngle(j, minA0, positions, connections, False)
            if minA2[1] < minA2[1]:
                nextIdx = j

    if nextIdx == -1:
        nextIdx = connections[idx][0]

    return (nextIdx, minAngle)

def squashVertices(positionDict, connections):
    removedItems = []
    indices = [int(k) for k in positionDict.keys()]
    idxChanges = indices
    for i in indices:
        if i in removedItems:
            continue
        for j in indices:
            if j in removedItems or j == i:
                continue

            if distance(positionDict[i], positionDict[j]) < 1e-6:
                connections[j] = list(set(connections[j]))
                if i in connections[j]:
                    connections[j].remove(i)
                if j in connections[i]:
                    connections[i].remove(j)

                connections[i].extend(connections[j])
                connections[i] = list(set(connections[i]))
                connections[i].sort()

                for k in connections.keys():
                    if k == i: continue
                    if j in connections[k]:
                        idx = connections[k].index(j)
                        connections[k][idx] = i

                idxChanges[j] = i
                removedItems.append(j)

    for i in removedItems:
        del positionDict[i]
        del connections[i]

    for i in connections.keys():
        connections[i] = list(set(connections[i]))
        connections[i].sort()

    return idxChanges

def computeLineEquations(positions, connections):
    cons = set()
    for i in connections.keys():
        for j in connections[i]:
            cons.add((min(i, j), max(i, j)))

    lineEquations = {}
    for item in cons:
        a = (positions[item[1]][1] - positions[item[0]][1])
        b = -(positions[item[1]][0] - positions[item[0]][0])

        xm = 0.5 * (positions[item[0]][0] + positions[item[1]][0])
        ym = 0.5 * (positions[item[0]][1] + positions[item[1]][1])
        c = -(a * xm +  b * ym)

        lineEquations[item] = (a, b, c)

    return lineEquations

def checkPossibleSegmentIntersection(segment, positions, lineEquations, minAngle, lastIntersection):
    item1 = (min(segment), max(segment))

    (a1, b1, c1) = (0,0,0)
    A = [0]*2
    B = A

    if segment[0] == None:
        A = lastIntersection
        B = positions[segment[1]]

        a1 = B[1] - A[1]
        b1 = -(B[0] - A[0])
        xm = 0.5 * (A[0] + B[0])
        ym = 0.5 * (A[1] + B[1])
        c1 = -(a1 * xm + b1 * ym)

    else:
        A = positions[segment[0]]
        B = positions[segment[1]]

        (a1, b1, c1) = lineEquations[item1]

        if segment[1] < segment[0]:
            (a1, b1, c1) = (-a1, -b1, -c1)

    curAngle = math.atan2(a1, -b1)
    matrix = [[-math.cos(curAngle), -math.sin(curAngle)], [math.sin(curAngle), -math.cos(curAngle)]]

    origMinAngle = minAngle

    segment1 = [B[0] - A[0], B[1] - A[1], 0.0]

    intersectingSegments = []
    distanceAB = distance(A, B)
    for item2 in lineEquations.keys():
        item = item2
        C = positions[item[0]]
        D = positions[item[1]]

        if segment[0] == None:
            if (segment[1] == item[0] or
                segment[1] == item[1]): continue
        else:
            if (item1[0] == item[0] or
                item1[1] == item[0] or
                item1[0] == item[1] or
                item1[1] == item[1]): continue

        nodes = set([item1[0],item1[1],item[0],item[1]])
        if len(nodes) < 4: continue       # share same vertex

        (a2, b2, c2) = lineEquations[item]

        segment2 = [C[0] - A[0], C[1] - A[1], 0.0]
        segment3 = [D[0] - A[0], D[1] - A[1], 0.0]

        # check that C and D aren't on the same side of AB
        if cross(segment1, segment2)[2] * cross(segment1, segment3)[2] > 0.0: continue

        if cross(segment1, segment2)[2] < 0.0 or cross(segment1, segment3)[2] > 0.0:
            (C, D, a2, b2, c2) = (D, C, -a2, -b2, -c2)
            item = (item[1], item[0])

        denominator = a1 * b2 - b1 * a2
        if math.fabs(denominator) < 1e-9: continue

        px = (b1 * c2 - b2 * c1) / denominator
        py = (a2 * c1 - a1 * c2) / denominator

        distanceCD = distance(C, D)

        distanceAP = distance(A, [px, py])
        distanceBP = distance(B, [px, py])
        distanceCP = distance(C, [px, py])
        distanceDP = distance(D, [px, py])

        # check intersection is between AB and CD
        check1 = (distanceAP - 1e-6 < distanceAB and distanceBP - 1e-6 < distanceAB)
        check2 = (distanceCP - 1e-6 < distanceCD and distanceDP - 1e-6 < distanceCD)
        if not check1 or not check2: continue

        if math.fabs(dot(segment1, [D[0] - C[0], D[1] - C[1], 0.0]) / (distanceAB * distanceCD) + 1.0) < 1e-9: continue

        if ((distanceAP < 1e-6) or
            (distanceBP < 1e-6 and distanceCP < 1e-6) or
            (distanceDP < 1e-6)):
            continue

        direction = [D[0] - C[0], D[1] - C[1]]
        direction = [dot(matrix[0], direction), dot(matrix[1], direction)]
        angle = math.fmod(math.atan2(direction[1], direction[0]) + 2 * math.pi, 2 * math.pi)

        newSegment = ([px, py], item[1], distanceAP, angle)

        if distanceCP < 1e-6 and angle > origMinAngle: continue
        if distanceBP > 1e-6 and angle > math.pi: continue

        if len(intersectingSegments) == 0:
            intersectingSegments.append(newSegment)
            minAngle = angle
        else:
            if intersectingSegments[0][2] - 1e-9 > distanceAP:
                intersectingSegments[0] = newSegment
                minAngle = angle
            elif intersectingSegments[0][2] + 1e-9 > distanceAP and angle < minAngle:
                intersectingSegments[0] = newSegment
                minAngle = angle

    return intersectingSegments

def projectToPlane(normal):
    fh = open('pos10_sc_inj_C1_ElementPositions.gpl','w')
    normal = normalize(normal)
    ori = getQuaternion(normal, [0, 0, 1])

    left2Right = [0, 0, 1]
    if math.fabs(math.fabs(dot(normal, left2Right)) - 1) < 1e-9:
        left2Right = [1, 0, 0]
    rotL2R = ori.rotate(left2Right)
    deviation = math.atan2(rotL2R[1], rotL2R[0])
    rotBack = Quaternion([math.cos(0.5 * deviation), 0, 0, -math.sin(0.5 * deviation)])
    ori = rotBack * ori

    decodeVertices()

    for i in range(len(vertices)):
        positions = {}
        connections = {}
        for j in range(0, len(vertices[i]), 3):
            nextPos3D = ori.rotate(vertices[i][j:j+3])
            nextPos2D = nextPos3D[0:2]
            positions[j/3] = nextPos2D

        if len(positions) == 0:
            continue

        idx = 0
        maxX = positions[0][0]
        for j in positions.keys():
            if positions[j][0] > maxX:
                maxX = positions[j][0]
                idx = j
            if positions[j][0] == maxX and positions[j][1] > positions[idx][1]:
                idx = j

        for j in range(0, len(triangles[i]), 3):
            for k in range(0, 3):
                vertIdx = triangles[i][j + k]
                if not vertIdx in connections:
                    connections[vertIdx] = []
                for l in range(1, 3):
                    connections[vertIdx].append(triangles[i][j + ((k + l) % 3)])

        numConnections = 0
        for j in connections.keys():
            connections[j] = list(set(connections[j]))
            numConnections += len(connections[j])

        numConnections /= 2
        idChanges = squashVertices(positions, connections)

        lineEquations = computeLineEquations(positions, connections)

        idx = idChanges[int(idx)]
        fh.write("%.6f    %.6f\n" % (positions[idx][0], positions[idx][1]))

        curAngle = math.pi
        origin = idx
        count = 0
        passed = []
        while (count == 0 or distance(positions[origin], positions[idx]) > 1e-9) and not count > numConnections:
            nextGen = computeMinAngle(idx, curAngle, positions, connections, False)
            nextIdx = nextGen[0]
            direction = [positions[nextIdx][0] - positions[idx][0],
                         positions[nextIdx][1] - positions[idx][1]]
            curAngle = math.atan2(direction[1], direction[0])

            intersections = checkPossibleSegmentIntersection((idx, nextIdx), positions, lineEquations, nextGen[1], [])
            if len(intersections) > 0:
                while len(intersections) > 0 and not count > numConnections:
                    fh.write("%.6f    %.6f\n" %(intersections[0][0][0], intersections[0][0][1]))
                    count += 1
    
                    idx = intersections[0][1]
                    direction = [positions[idx][0] - intersections[0][0][0],
                                 positions[idx][1] - intersections[0][0][1]]
                    curAngle = math.atan2(direction[1], direction[0])
                    nextGen = computeMinAngle(idx, curAngle, positions, connections, False)
    
                    intersections = checkPossibleSegmentIntersection((None, idx), positions, lineEquations, nextGen[1], intersections[0][0])
            else:
                idx = nextIdx
    
            fh.write("%.6f    %.6f\n" % (positions[idx][0], positions[idx][1]))
    
            if idx in passed:
                direction1 = [positions[idx][0] - positions[passed[-1]][0],
                              positions[idx][1] - positions[passed[-1]][1]]
                direction2 = [positions[origin][0] - positions[passed[-1]][0],
                              positions[origin][1] - positions[passed[-1]][1]]
                dist1 = distance(positions[idx], positions[passed[-1]])
                dist2 = distance(positions[origin], positions[passed[-1]])
                if dist1 * dist2 > 0.0 and math.fabs(math.fabs(dot(direction1, direction2) / (dist1 * dist2)) - 1.0) > 1e-9:
                    sys.stderr.write("error: projection cycling on element id: %d, vertex id: %d\n" %(i, idx))
                break

            passed.append(idx)
            count += 1
        fh.write("\n")

        if count > numConnections:
            sys.stderr.write("error: projection cycling on element id: %d\n" % i)

        for j in range(0, len(decoration[i]), 6):
            for k in range(j, j + 6, 3):
                nextPos3D = ori.rotate(decoration[i][k:k+3])
                fh.write("%.6f    %.6f\n" % (nextPos3D[0], nextPos3D[1]))
            fh.write("\n")

    fh.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--export-vtk', action='store_true')
    parser.add_argument('--export-web', action='store_true')
    parser.add_argument('--background', nargs=3, type=float)
    parser.add_argument('--project-to-plane', action='store_true')
    parser.add_argument('--normal', nargs=3, type=float)
    args = parser.parse_args()

    if (args.export_vtk):
        exportVTK()
        sys.exit()

    if (args.export_web):
        bgcolor = []
        if (args.background):
            validBackground = True
            for comp in bgcolor:
                if comp < 0.0 or comp > 1.0:
                    validBackground = False
                    break
            if (validBackground):
                bgcolor = args.background
        exportWeb(bgcolor)
        sys.exit()

    if (args.project_to_plane):
        normal = [0.0, 1.0, 0.0]
        if (args.normal):
            normal = args.normal
        projectToPlane(normal)
        sys.exit()

    parser.print_help()
