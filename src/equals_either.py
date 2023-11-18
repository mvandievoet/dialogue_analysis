
def equals_either(df, pony1, pony2):
    df1 = df[(df['pony']==pony1) | (df['pony']==pony2)]
    return df1
