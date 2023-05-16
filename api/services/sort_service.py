import pandas as pd


def sort(action: bool, x: str, y: str) -> dict:
    """
    sorts a list of given actions with dataset uploaded from the user,
    return the dictionary that contains the sorted list of columns and rows,

    Args:
        action (bool): action flag to perform sorting in ascending or descending manner. Defaults to None
        x (str): column name which is to be used for sorting from the file. Defaults to None
        y (str): row name which is to be used for sorting from the file. Defaults to None

    Returns:
        dict: sorted column names and row values 
    """
    try:
        print('trying in excel and try block')
        df = pd.read_excel("api/services/data.xlsx")
        print('worked with excel only')
    except:
        print('failed to load excel')
        df = pd.read_csv("api/services/data.csv") 
        print('loaded successfully csv')

    # print("\n================================ Im in sort API entry point================================\n ",
    #         type(df),'\n',df.columns,f'\n================================ {type(action)}================================'
    #         )
    if action == 'ascending':
        agg_df = df.groupby(by=[x]).aggregate({y: sum})
        sorted_df = agg_df.sort_values(y, ascending=True)
        # print("=========================================================\n",
        #       type(sorted_df), '\n ', sorted_df)
    elif action == 'descending':
        agg_df = df.groupby(by=[x]).aggregate({y: sum})
        sorted_df = agg_df.sort_values(y, ascending=False)

        # print("=========================================================\n",
        #       type(sorted_df), '\n ', sorted_df)
    X = tuple(sorted_df[y].keys())
    Y = tuple(sorted_df[y].values)
    sort_dict = {'column': X, 'rows': Y}

    # print(
    #     f'================================================================{sort_dict}')
    return sort_dict
