

def set_cache_data(data):
    """saves the cache data

    Args:
        data (dictionary): file uplaoded from the dictionary
    """    
    global dataSource
    dataSource = data
    
    
def get_cache_data(): 
    global dataSource
    
    return dataSource