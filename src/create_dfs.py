def create_dfs(arr1, dfs, df):
    for i in range(len(arr1)):
        dfs[i] = df[df['dialog'].str.contains(arr1[i], na=False)]
    return dfs


