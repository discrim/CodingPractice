from os import listdir

from numpy import loadtxt, insert, savetxt

def main(meas, fn):
    arr = loadtxt(meas + 'Originals/' + fn, dtype='str', delimiter=',', skiprows=5)
    arr = insert(arr, 1, -1, axis=1)
    arr[:, 0] = usecLeadingZeros(arr[:, 0])
    
    rep = len(arr) // 16
    for ii in range(0, len(arr), 16):
        arr[ii:ii + 16, 1] = ii % 3
    
    savetxt(meas + 'Snapshots_Usec_leading_zeros/'+ fn, arr, fmt='%s', delimiter=',')

def usecLeadingZeros(timestamps):
    for ii, elem in enumerate(timestamps):
        ss, us = elem.split('.')
        if len(us) < 6:
            timestamps[ii] = ss + '.' + '0' * (6 - len(us)) + us
    return timestamps

def testmain():
    from numpy import asarray
    aa = asarray(['111.2', '12.345', '542.11234'])
    for ii, elem in enumerate(aa):
        ss, us = elem.split('.')
        aa[ii] = ss + '.' + '0' * (5 - len(us)) + us
    print(aa)
    
    
if __name__ == "__main__":
    meas = 'D:/Desktop/MDP/Measurements/2020-08-05_measure_1m_63.4deg/'
    filenames = listdir(meas + 'Originals')
    for fn in filenames:
        main(meas, fn)