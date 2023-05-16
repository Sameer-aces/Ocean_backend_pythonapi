import pandas as pd

def table_calc(heading, side_heading,text):
    
    
    try:
        print('trying in excel and try block')
        df = pd.read_excel("api/services/data.xlsx")
        print('worked with excel only')
    except:
        print('failed to load excel')
        df = pd.read_csv("api/services/data.csv") 
        print('loaded successfully csv')
    "errorrr here"
    table_df= df.groupby([heading,side_heading]).aggregate({text:sum})
    
    unstack_df = table_df.unstack(-2)
    text_values = unstack_df.values.tolist()
    
    res_data = {
        "headings":         tuple(df[heading].unique()), 
        "side_headings":    tuple(df[side_heading].unique()), 
        "text_values":      text_values
                }
    # print('\n this is the tabel calculation',unstack_df,'\n\n',type(unstack_df))
    
    return res_data 