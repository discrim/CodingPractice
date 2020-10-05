from numpy import loadtxt, unique

def main():
    txt_str = loadtxt("D:/Desktop/MDP/Measurements/2020-06-30_measure_1m_45deg/01,04.txt", dtype='str', delimiter=',', skiprows=5,)
    print(txt_str)
    #times = unique(txt[:, 0])
    
    txt_float = txt_str[:, :4].astype(float)
    print(txt_float)

if __name__ == '__main__':
    main()