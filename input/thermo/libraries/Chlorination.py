#!/usr/bin/env python
# encoding: utf-8

name = "Chlorination"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "1230xa",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3 C  u0 p0 c0 {2,S} {4,S} {5,D}
4 Cl u0 p3 c0 {3,S}
5 C  u0 p0 c0 {3,D} {6,S} {7,S}
6 Cl u0 p3 c0 {5,S}
7 Cl u0 p3 c0 {5,S}
8 H  u0 p0 c0 {2,S}
9 H  u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.046,31.867,34.851,37.2015,40.58,42.80,45.83],'cal/(mol*K)'),
        H298 = (-26.053,'kcal/mol'),
        S298 = (93.522,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)


entry(
    index = 2,
    label = "HCL",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([ 6.945,6.9431,6.973,7.033,7.222,7.451,7.972],'cal/(mol*K)'),
        H298 = (-22.06,'kcal/mol'),
        S298 = (44.670,'cal/(mol*K)'),
    ),
    shortDesc = u"""NIST""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "C3H3Cl3",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 Cl u0 p3 c0 {2,S}
8 Cl u0 p3 c0 {3,S}
9 Cl u0 p3 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.67,20,22.74,25.63,27.60,29.77,30.58],'cal/(mol*K)'),
        H298 = (-15.2,'kcal/mol'),
        S298 = (85.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""NIST""",
    longDesc = 
u"""

""",
)

#entry(
#    index = 4,
#    label = "1,1,1,2,3-pentachloropropane",
#    molecule = 
#"""
#1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
#2 C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
#3 C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
#4 H u0 p0 c0 {1,S}
#5 Cl u0 p3 c0 {1,S}
#6 Cl u0 p3 c0 {3,S}
#7 Cl u0 p3 c0 {2,S}
#8 H u0 p0 c0 {2,S}
#9 H u0 p0 c0 {2,S}
#10 Cl u0 p3 c0 {3,S}
#11 Cl u0 p3 c0 {3,S}
#""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([34.04,38.44,41.68,44.31,47.85,50.47,53.21],'cal/(mol*K)'),
#        H298 = (-53.3,'kcal/mol'),
#        S298 = (105.15,'cal/(mol*K)'),
#    ),
#    shortDesc = u"""CBS-QB3 calcs""",
 #   longDesc = 
#u"""
#
#""",
#)

entry(
    index = 5,
    label = "ClCC(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4 Cl u0 p3 c0 {1,S}
5 Cl u0 p3 c0 {1,S}
6 Cl u0 p3 c0 {3,S}
7 Cl u0 p3 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
10 Cl u0 p3 c0 {3,S}
11 Cl u0 p3 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.24,41.54,45.18,48.11,50.75,53.78,56.01],'cal/(mol*K)'),
        H298 = (-59.5,'kcal/mol'),
        S298 = (108.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "Cl",
    molecule = 
"""
1 Cl u1 p3 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968],'cal/(mol*K)'),
        H298 = (29.347,'kcal/mol'),
        S298 = (37.959,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)



entry(
    index = 7,
    label = "Cl2",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.957,8.266,8.491,8.642,8.796,8.846,8.873],'cal/(mol*K)'),
        H298 = (-0.685,'kcal/mol'),
        S298 = (53.383,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "CH2Cl",
    molecule = 
"""
1 C  u1 p0 c0 {2,S} {3,S} {4,S}
2 Cl u0 p3 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.987,11.160 ,12.171,13.025,14.364,15.361,16.996 ],'cal/(mol*K)'),
        H298 = (28.606,'kcal/mol'),
        S298 = (57.651,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "CHCl2",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u1 p0 c0 {1,S} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.907,13.296,14.418,15.293,16.484,17.210,18.224],'cal/(mol*K)'),
        H298 = (20.597,'kcal/mol'),
        S298 = (65.728,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "rad1",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {7,S} {8,S}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 C  u1 p0 c0 {2,S} {5,S} {6,S}
5 Cl u0 p3 c0 {4,S}
6 Cl u0 p3 c0 {4,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.735 ,28.138 ,30.686,32.652,35.457,37.330,39.985],'cal/(mol*K)'),
        H298 = (19.949,'kcal/mol'),
        S298 = (87.920,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "rad2",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  Cl u0 p3 c0 {1,S}
5  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  Cl u0 p3 c0 {5,S}
7  Cl u0 p3 c0 {5,S}
8  C  u1 p0 c0 {5,S} {9,S} {10,S}
9  Cl u0 p3 c0 {8,S}
10 H  u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.167 ,42.155 ,44.960,47.005,49.701,51.321,53.316],'cal/(mol*K)'),
        H298 = (-10.101,'kcal/mol'),
        S298 = (111.697,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)


entry(
    index = 12,
    label = "rad3",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  C  u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  Cl u0 p3 c0 {4,S}
6  Cl u0 p3 c0 {4,S}
7  C  u1 p0 c0 {4,S} {8,S} {10,S}
8  Cl u0 p3 c0 {7,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.416 ,37.606 ,40.792,43.253,46.702,48.914,51.842],'cal/(mol*K)'),
        H298 = (-6.900,'kcal/mol'),
        S298 = (104.456,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)


entry(
    index = 13,
    label = "rad4",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  Cl u0 p3 c0 {1,S}
5  C  u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
6  Cl u0 p3 c0 {5,S}
7  C  u1 p0 c0 {5,S} {8,S} {10,S}
8  Cl u0 p3 c0 {7,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.355 ,37.552 ,40.741,43.204,46.660,48.879,51.823],'cal/(mol*K)'),
        H298 = (-5.818,'kcal/mol'),
        S298 = (103.998,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)




entry(
    index = 14,
    label = "rad5",
    molecule = 
"""
1  C  u1 p0 c0 {2,S} {3,S} {4,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  C  u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  Cl u0 p3 c0 {4,S}
6  Cl u0 p3 c0 {4,S}
7  C  u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  Cl u0 p3 c0 {7,S}
9  H  u0 p0 c0 {7,S}
10 H  u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.659 ,36.796 ,40.030,42.574,46.192,48.535,51.647],'cal/(mol*K)'),
        H298 = (-12.848,'kcal/mol'),
        S298 = (104.027,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)


entry(
    index = 15,
    label = "rad6",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  Cl u0 p3 c0 {1,S}
3  C  u1 p0 c0 {1,S} {4,S} {5,S}
4  Cl u0 p3 c0 {3,S}
5  C  u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6  Cl u0 p3 c0 {5,S}
7  Cl u0 p3 c0 {5,S}
8  Cl u0 p3 c0 {5,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.837 ,36.982 ,40.212 ,42.744,46.332 ,48.646,51.703],'cal/(mol*K)'),
        H298 = (-8.758,'kcal/mol'),
        S298 = (105.970,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "1230xf",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {8,S} {9,S}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 Cl u0 p3 c0 {4,S}
6 Cl u0 p3 c0 {4,S}
7 Cl u0 p3 c0 {4,S}
8 H  u0 p0 c0 {1,S}
9 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.148 ,33.230 ,36.160 ,38.345,41.360,43.317,46.044],'cal/(mol*K)'),
        H298 = (-20.637,'kcal/mol'),
        S298 = (90.801,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "240ab",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  Cl u0 p3 c0 {2,S}
4  Cl u0 p3 c0 {2,S}
5  C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  Cl u0 p3 c0 {5,S}
7  Cl u0 p3 c0 {5,S}
8  Cl u0 p3 c0 {5,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {1,S}
11 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.381 ,38.923 ,42.375 ,45.109,49.149,51.939,55.980],'cal/(mol*K)'),
        H298 = (-58.083,'kcal/mol'),
        S298 = (98.307,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "240db",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  Cl u0 p3 c0 {1,S}
3  C  u0 p0 c0 {1,S} {4,S} {5,S} {11,S}
4  Cl u0 p3 c0 {3,S}
5  C  u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6  Cl u0 p3 c0 {5,S}
7  Cl u0 p3 c0 {5,S}
8  Cl u0 p3 c0 {5,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {1,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.630  ,38.464 ,42.240  ,45.229,49.554,52.436,56.425],'cal/(mol*K)'),
        H298 = (-54.049,'kcal/mol'),
        S298 = (99.599,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)


entry(
    index = 19,
    label = "250fb",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  Cl u0 p3 c0 {1,S}
3  C  u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C  u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  Cl u0 p3 c0 {4,S}
6  Cl u0 p3 c0 {4,S}
7  Cl u0 p3 c0 {4,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.008,34.775,38.707,41.947,46.832,50.216,55.080],'cal/(mol*K)'),
        H298 = (-49.253,'kcal/mol'),
        S298 = (94.098,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)



entry(
    index = 20,
    label = "1240za",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,D}
2 Cl u0 p3 c0 {1,S}
3 Cl u0 p3 c0 {1,S}
4 C  u0 p0 c0 {1,D} {5,S} {7,S}
5 C  u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6 Cl u0 p3 c0 {5,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {5,S}
9 H  u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.731,26.651,29.819,32.388,36.213,38.844,42.624 ],'cal/(mol*K)'),
        H298 = (-13.244,'kcal/mol'),
        S298 = (82.453,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)


entry(
    index = 21,
    label = "1240zf",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {7,S} {8,S}
2 C  u0 p0 c0 {1,D} {3,S} {9,S}
3 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 Cl u0 p3 c0 {3,S}
5 Cl u0 p3 c0 {3,S}
6 Cl u0 p3 c0 {3,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {1,S}
9 H  u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.729,27.813,30.918,33.325,36.797,39.189,42.773],'cal/(mol*K)'),
        H298 = (-7.364,'kcal/mol'),
        S298 = (81.149,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc = 
u"""

""",
)