import timeit
def search_an_element(arr,el):
	t = 0
	for i in range(0,len(arr)//2):
		if arr[i] > t:
			t = arr[i]
		if arr[i*-1] > t:
			t = arr[i*-1]
	return t
a = [13868,54682,91258,34058,52406,7068,96281,40968,81386,77706,27186,84210,86126,58424,24450,11882,66629,84765,71504,72163,91780,64738,32963,30337,7746,47207,15038,91228,43899,9237,6075,24286,42064,43358,1204,79106,84363,64738,36156,88681,50494,1148,19170,50645,76690,90212,74129,54428,21483,32996,96121,34124,72302,21673,28762,8926,69526,97180,68639,93375,310,10922,92616,58542,1340,24136,71441,20633,70755,67849,1086,71764,87517,55730,2728,73560,34088,89854,22157,95831,55437,83771,6479,95634,54196,59798,54641,29712,68959,86941,41066,53062,19184,46553,84167,59921,26806,45575,9056,76648,74123,89438,91246,83549,75488,85286,16627,59277,27210,35563,9702,63272,92909,53721,9595,13093,23655,35029,84403,31064,32430,23986,66974,13849,99856,61966,43164,88337,13299,8443,65339,8863,12878,21913,64359,23343,23423,2596,57883,17231,7399,29794,96026,31231,43098,43233,65675,86870,86464,87611,49703,45298,96038,58587,5720,24836,41752,83235,40134,34123,6348,69116,73796,45999,97903,52797,6461,40838,47330,42344,80,73509,64491,46080,39746,39996,61731,37963,63876,99639,82801,90745,34631,38981,84630,25447,31112,78994,6120,94932,83987,34929,69386,62780,24171,67228,67353,2146,27051,36862,99299,94119,22110,13789,24354,95794,92476,36987,99552,66504,60142,56110,49551,34533,20546,38527,86353,161,3857,62654,69183,56760,35625,30708,77788,40907,6473,37658,8237,71230,56537,14787,53479,12408,61252,65487,32643,89125,66470,25859,70020,49203,51437,50086,5363,74305,44883,12656,18959,75930,6760,270,4112,93643,76105,75592,7775,1667,13374,48761,81369,80572,17059,49166,11557,64555,12177,67931,23712,63644,61175,3272,70810,10156,37546,56287,29361,31688,39755,99039,86786,19831,1706,62899,111,28607,95962,38803,91222,21845,31957,74200,40730,85713,42080,22581,30694,99937,58635,24934,91860,92917,98861,34556,20651,20898,15035,32232,82978,21108,45739,32897,88677,29286,56848,93483,54681,86934,53705,56544,897,83680,70198,31300,63824,94778,36468,76995,16426,94270,59911,50733,76225,52345,37899,3963,5905,79443,62017,61253,15910,33531,15046,44507,72995,16137,49389,53304,13249,55430,64663,39860,84581,70093,61669,85733,93380,59467,84493,75622,52258,17302,43220,88407,53447,53213,19677,79660,86893,6081,95565,59293,4641,73552,34346,7216,54611,88257,95383,35722,6841,27948,41063,45066,96965,49263,58608,65254,58798,18980,13288,38675,32567,72182,47582,91457,37274,22861,57894,57470,29840,28505,56904,61660,11832,20990,20228,79867,50463,66169,38310,72016,12835,27836,4913,41187,57280,39824,62341,25532,3184,6007,30671,46823,25143,52205,24400,75746,97538,17851,68770,44760,11979,14965,90676,71277,60224,68432,29192,85643,82023,49004,16240,32439,88030,27434,30073,69055,13432,93920,43662,18959,38051,18587,93282,54846,13393,74001,77300,61392,63025,88225,76815,18215,90207,94986,51346,41221,41321,83763,31065,60765,13402,53702,17010,60113,58147,22364,74109,67491,522,13030,14968,15305,91457,46711,94851,19092,75179,39219,44268,44196,27802,80421,94698,14184,94033,81962,24409,55931,62088,55325,23937,99715,44770,36715,97100,11968,75033,81060,51944,40186,90048,34727,70149,48215,95316,64518,33820,71486,14996,50113,87538,36416,73288,84680,24878,96382,98991,22032,5602,3005,20868,48080,16046,70505,83426,96095,34406,47541,49168,55964,80571,74249,49343,57606,57295,58580,51731,8796,24716,45668,43828,80613,83921,40404,44543,78300,20917,98046,60053,15543,45933,99601,4899,65176,21907,6620,60958,3565,82869,46905,26814,88359,60267,54171,51114,24153,62449,56969,46076,94914,24356,63033,90980,59721,79578,16059,4144,77380,73281,71830,47393,29514,42588,14406,7636,2126,60260,73629,61129,16780,93989,17056,44114,76680,51490,46202,48848]
el = 62088
#print(timeit.timeit("search_an_element(a,el)", setup="from __main__ import search_an_element,a,el"))
x = search_an_element(a,el)
print( x )