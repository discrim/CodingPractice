if 1:
    from pandas import DataFrame as DF
    from numpy.random import randint
    from numpy import concatenate

    #df1 = DF(randint(10, size=(5,3)), columns=['Id', 'firstVal', 'secondVal'])
    #df1 = DF({'Id': randint(10, size=(5,1)),
    #          'firstVal': randint(10, size=(5,1)),
    #          'secondVal': randint(10, size=(5,1))})
    df1 = DF({'Id': [11, 22, 33, 11, 55],
              'firstVal': [6, 7, 8, 9, 10],
              'secondVal': [11, 12, 13, 14, 15]})
    id_all = df1['Id'].unique()
    print(df1)
    print(df1[['Id', 'firstVal']])
    print(id_all)
    print()

    df2 = DF([100, 110] * 2, columns=['thirdVal'])
    df2['Id'] = concatenate((id_all[2:], id_all[2:]))
    df2 = df2[['Id', 'thirdVal']].groupby(['Id']).sum()
    id_change = df2.index.tolist()
    print(df2)
    print(id_change)
    print()
    
    '''
    df3 = DF(0, index=id_all, columns=['thirdVal'])
    print(df3)
    print()
    
    df3.update(df2)
    print(df3)
    print()
    '''
    
    #df1['thirdVal'] = df1['Id'].apply(lambda Id: df3.loc[Id])
    df1['thirdVal'] = 0
    df1[df1['Id'].isin(id_change)]['thirdVal'] = df2.loc[id_change]['thirdVal']
    print(df1)
    print()
    
    
    
    for idx in df3.index:
        print(idx)
    
    print(df1.loc[df1['firstVal'] > 8])
