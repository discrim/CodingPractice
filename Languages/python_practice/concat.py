import numpy as np
from numpy import (
c_, concatenate, asarray, dot, cross,
where, append, column_stack, row_stack, vstack
)
from numpy.random import randn
from scipy.linalg import norm

asz = asarray( [10, 10, 3] )
pa = asarray( where( randn(3) > 0.5,[-3, -3, -3], asz + 3 ) )
Tz = pa - ( asz / 2 ); Tz /= norm( Tz )
Tx = dot( [[0, -1 , 0], [1, 0, 0], [0, 0, 0]], Tz) ; Tx /= norm( Tx )
Ty = cross( Tz, Tx )
print("Tx: ", Tx)
print("Ty: ", Ty)
print("Tz: ", Tz)
print("pa: ", pa)
Ta1 = c_[Tx, Ty, Tz, pa]
T1 = c_[Ta1.T, [0, 0, 0, 1]].T
# T1 = c_[c_[Tx, Ty, Tz, pa].T, [0, 0, 0, 1]].T
print("Ta1: \n", Ta1)
print("T1: \n", T1)

#print(asarray( [Tx, Ty, Tz, pa] ).T )
T2 = append( asarray( [Tx, Ty, Tz, pa] ).T,
             asarray( [[0, 0, 0, 1]] ), axis=0 )
print("T2: \n", T2)
print("T1 == T2: \n", T1 == T2)

Tc1 = asarray( [Tx, Ty, Tz, pa] ).T
T3 = asarray( [Tc1[0], Tc1[1], Tc1[2], [0, 0, 0, 1]] )
print("T3: \n", T3)

Td1 = asarray( [Tx, Ty, Tz, pa] )
T4 = [Td1.T, [0, 0, 0, 1]]
print("Td1: \n", Td1)
print("T4: \n", T4)
# T4 = asarray( Td1.T, [0, 0, 0, 1] )

T5 = vstack( ( asarray( [Tx, Ty, Tz, pa] ).T, [0, 0, 0, 1] ) )
print("T5: \n", T5)

T6 = column_stack( ([Tx, Ty, Tz, pa], [0, 0, 0, 1] ) ).T
print("T6: \n", T6)




"""
Failure
Tba = concatenate( ( [Tx].T, [Ty].T, [Tz].T, [pa].T ), axis=1 )
print(Tba)
T2 = concatenate( ( Tba.T, [[0, 0, 0, 1]].T ), axis=1)
print(T2)
"""
