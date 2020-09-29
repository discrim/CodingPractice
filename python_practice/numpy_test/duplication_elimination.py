from numpy import loadtxt, empty, savetxt

ori = loadtxt("DailyTracking_all_behavior.txt", dtype='str', delimiter="	", encoding='UTF8')
sin_col = ori.reshape((-1, 1))

#savetxt("DailyTracking_single_column.txt", sin_col, fmt='%s', encoding='UTF8')

no_dup = []
for ee in sin_col:
    if ee not in no_dup:
        no_dup.append(ee)
no_dup.sort()
savetxt("DailyTracking_no_dup.txt", no_dup, fmt='%s', encoding='UTF8')