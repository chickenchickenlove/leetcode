from typing import List

# dp
# 기본값 -1. -1이면 띌 수 없음. (돌이 없는 곳)
# 돌이 있는 곳에 왔을 때의 최소값? 최대값?
# k= 항상 1보다 커야함.
# dp를 다 만들 순 없고, 저 값을 그대로 사용해야 함.


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dpm = [9876543210 for _ in range(n)]
        dpM = [0 for _ in range(n)]

        if stones[1] != 1:
            return False
        dpm[0] = 0
        dpm[1] = stones[1]
        dpM[1] = stones[1]

        # 2도 나와야함.
        for i in range(2, n):
            for j in range(i):
                pre_stone = stones[j]
                now_stone = stones[i]

                min_range = dpm[j]
                max_range = dpM[j]

                if pre_stone + (min_range-1) <= now_stone <= pre_stone + (max_range+1):
                    if (now_stone - pre_stone) in (min_range-1, min_range, min_range+1, max_range-1, max_range, max_range+1):
                        dpm[i] = min(dpm[i], now_stone - pre_stone)
                        dpM[i] = max(dpM[i], now_stone - pre_stone)
        # print(f'{dpm=}')
        # print(f'{dpM=}')
        return dpm[-1] != 9876543210
# min, max가 보장된다고 해서 항상 그 안의 값이 가능하지는 않음.
# 그런데 대부분 되네? min, max만 하면 될 것 같음...

# Solution().canCross([0,1,3,5,6,8,12,17])
# Solution().canCross([0,1,2,3,4,8,9,11])
# Solution().canCross([0,1,3,6,7])
# Solution().canCross([0,2])
Solution().canCross([0,1,3,6,10,13,15,16,19,21,25])


tc = [0,1,3,4,5,7,8,9,11,12,13,15,16,17,19,20,21,23,24,25,27,28,29,31,32,33,35,36,37,39,40,41,43,44,45,47,48,49,51,52,53,55,56,57,59,60,61,63,64,65,67,68,69,71,72,73,75,76,77,79,80,81,83,84,85,87,88,89,91,92,93,95,96,97,99,100,101,103,104,105,107,108,109,111,112,113,115,116,117,119,120,121,123,124,125,127,128,129,131,132,133,135,136,137,139,140,141,143,144,145,147,148,149,151,152,153,155,156,157,159,160,161,163,164,165,167,168,169,171,172,173,175,176,177,179,180,181,183,184,185,187,188,189,191,192,193,195,196,197,199,200,201,203,204,205,207,208,209,211,212,213,215,216,217,219,220,221,223,224,225,227,228,229,231,232,233,235,236,237,239,240,241,243,244,245,247,248,249,251,252,253,255,256,257,259,260,261,263,264,265,267,268,269,271,272,273,275,276,277,279,280,281,283,284,285,287,288,289,291,292,293,295,296,297,299,300,301,303,304,305,307,308,309,311,312,313,315,316,317,319,320,321,323,324,325,327,328,329,331,332,333,335,336,337,339,340,341,343,344,345,347,348,349,351,352,353,355,356,357,359,360,361,363,364,365,367,368,369,371,372,373,375,376,377,379,380,381,383,384,385,387,388,389,391,392,393,395,396,397,399,400,401,403,404,405,407,408,409,411,412,413,415,416,417,419,420,421,423,424,425,427,428,429,431,432,433,435,436,437,439,440,441,443,444,445,447,448,449,451,452,453,455,456,457,459,460,461,463,464,465,467,468,469,471,472,473,475,476,477,479,480,481,483,484,485,487,488,489,491,492,493,495,496,497,499,500,501,503,504,505,507,508,509,511,512,513,515,516,517,519,520,521,523,524,525,527,528,529,531,532,533,535,536,537,539,540,541,543,544,545,547,548,549,551,552,553,555,556,557,559,560,561,563,564,565,567,568,569,571,572,573,575,576,577,579,580,581,583,584,585,587,588,589,591,592,593,595,596,597,599,600,601,603,604,605,607,608,609,611,612,613,615,616,617,619,620,621,623,624,625,627,628,629,631,632,633,635,636,637,639,640,641,643,644,645,647,648,649,651,652,653,655,656,657,659,660,661,663,664,665,667,668,669,671,672,673,675,676,677,679,680,681,683,684,685,687,688,689,691,692,693,695,696,697,699,700,701,703,704,705,707,708,709,711,712,713,715,716,717,719,720,721,723,724,725,727,728,729,731,732,733,735,736,737,739,740,741,743,744,745,747,748,749,751,752,753,755,756,757,759,760,761,763,764,765,767,768,769,771,772,773,775,776,777,779,780,781,783,784,785,787,788,789,791,792,793,795,796,797,799,800,801,803,804,805,807,808,809,811,812,813,815,816,817,819,820,821,823,824,825,827,828,829,831,832,833,835,836,837,839,840,841,843,844,845,847,848,849,851,852,853,855,856,857,859,860,861,863,864,865,867,868,869,871,872,873,875,876,877,879,880,881,883,884,885,887,888,889,891,892,893,895,896,897,899,900,901,903,904,905,907,908,909,911,912,913,915,916,917,919,920,921,923,924,925,927,928,929,931,932,933,935,936,937,939,940,941,943,944,945,947,948,949,951,952,953,955,956,957,959,960,961,963,964,965,967,968,969,971,972,973,975,976,977,979,980,981,983,984,985,987,988,989,991,992,993,995,996,997,999,1000,1001,1003,1004,1005,1007,1008,1009,1011,1012,1013,1015,1016,1017,1019,1020,1021,1023,1024,1025,1027,1028,1029,1031,1032,1033,1035,1036,1037,1039,1040,1041,1043,1044,1045,1047,1048,1049,1051,1052,1053,1055,1056,1057,1059,1060,1061,1063,1064,1065,1067,1068,1069,1071,1072,1073,1075,1076,1077,1079,1080,1081,1083,1084,1085,1087,1088,1089,1091,1092,1093,1095,1096,1097,1099,1100,1101,1103,1104,1105,1107,1108,1109,1111,1112,1113,1115,1116,1117,1119,1120,1121,1123,1124,1125,1127,1128,1129,1131,1132,1133,1135,1136,1137,1139,1140,1141,1143,1144,1145,1147,1148,1149,1151,1152,1153,1155,1156,1157,1159,1160,1161,1163,1164,1165,1167,1168,1169,1171,1172,1173,1175,1176,1177,1179,1180,1181,1183,1184,1185,1187,1188,1189,1191,1192,1193,1195,1196,1197,1199,1200,1201,1203,1204,1205,1207,1208,1209,1211,1212,1213,1215,1216,1217,1219,1220,1221,1223,1224,1225,1227,1228,1229,1231,1232,1233,1235,1236,1237,1239,1240,1241,1243,1244,1245,1247,1248,1249,1251,1252,1253,1255,1256,1257,1259,1260,1261,1263,1264,1265,1267,1268,1269,1271,1272,1273,1275,1276,1277,1279,1280,1281,1283,1284,1285,1287,1288,1289,1291,1292,1293,1295,1296,1297,1299,1300,1301,1303,1304,1305,1307,1308,1309,1311,1312,1313,1315,1316,1317,1319,1320,1321,1323,1324,1325,1327,1328,1329,1331,1332]
# Solution().canCross(tc)





        # dp :


# SET로 넣으면 될 듯.
# BFS로도 가능함.
# 0 1 3 5 6 8 12 17
# 0 1 2 2 1 2
#         3 2
#           3 4   5

# 가장 큰 경우만 가능 경우도 있지만?
# 0 1 2 3 6 9 11 12 13
# 0 1 1 2 3 3 2  3  2
#       1
# 최대, 최소를 다 살펴야 할 듯?
# dp[11] = dp[9], dp[7]을 살펴보자.
# 3가지 경우 3 * 2000 ? 이건 아닌 듯. 필터링이 필요할 것 같은데.
# N**2이면 될 것 같은데...
# 그 안에 여러가지 숫자들이 존재할테니까...
# 최소값만 보는 것은 온당하지 않음.
# 필터링 될 것 같긴 함.



# 1 2 2 3 4 5
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 2 = 5
# 5 + 3 = 8
# 8 + 4 = 12
# 12 + 5 = 17