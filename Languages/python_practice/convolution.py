import numpy as np
from numpy import array, sum, newaxis, append, insert
from numpy.random import rand

def vectorize_input(x, filter_size):
    """
    Args:
        x -- C x H x W --
    """
    C, H, W = x.shape
    vectorized = np.array([[x[c, i:i + filter_size, j:j + filter_size].reshape(-1)
                             for j in range(W - filter_size + 1)
                            for i in range(H - filter_size + 1)]
                           for c in range(C)]).reshape((H - filter_size + 1) * (W - filter_size + 1), -1)
    return vectorized

def vectorize_filter(w):
    return w.reshape(-1)

x = np.array(list(range(0, -16, -1)) + list(range(16))).reshape(2, 4, 4)
print(x)
print(vectorize_input(x, 3))
print(vectorize_input(x, 3).shape)

if 0:
    x = rand(10, 3, 9, 16)
    w = rand(5, 3, 3, 3)

    C = x.shape[1]
    H, W = x.shape[2:]
    Hf, Wf = w.shape[2:]

    out = []
    for xn in x:
        print("xn.shape: ", xn.shape)
        out_f = []
        for filter in w:
            print("filter.shape: ", filter.shape)
            
            conv3d = sum(array([[[sum(xn[c, i:i + Hf, j:j + Wf] * filter[c])
                                  for j in range(W - Wf + 1)]
                                 for i in range(H - Hf + 1)]
                                for c in range(C)]), axis=0)
            print("conv3d.shape: ", conv3d.shape)
            out_f.append(conv3d)
            print("len(out_f): ", len(out_f))
        
        #out_f = array(out_f)
        #print("out_f.shape: ", out_f.shape)
        out.append(out_f)

    out = array(out)
    print("out.shape: ", out.shape)

    #for xn in x:
    #    out_f = []
    #    for filter in w:
    #        vectorized_xn = 