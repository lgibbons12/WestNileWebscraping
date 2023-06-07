def get_df(dfls, first_cell):
    for df in dfls:
        if df.columns[0] == first_cell:
            return df

def get_index(dfls, first_cell):
    for i, df in enumerate(dfls):
        if df.columns[0] == first_cell:
            return i
