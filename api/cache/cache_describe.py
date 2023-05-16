
def set_cache_description(records,fields,duplicates):
    global description
    description= {
        'total_records': records,
        'total_fields': fields,
        'total_duplicates': duplicates,
        
    }
    
def get_cache_description():
    global description
    return description