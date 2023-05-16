
def encode(data_dict)->dict:
    """Perfroms label encoding and returns a dictionary

    Args:
        data_dict (dictionary): data of claimants received from the client side 

    Returns:
        dict: returns the encoded dictionary
    """        
    for key in data_dict.keys():
        
        # if the key is Area_Service then encode it here
        if key== 'Area_Service':
        
            if(data_dict[key]=='Hudson Valley'):
                data_dict[key]=1
            elif(data_dict[key]=='Western NY'):
                data_dict[key]=2
            elif(data_dict[key]=='Central NY'):
                data_dict[key]=3
            elif(data_dict[key]=='Capital/Adirond'):
                data_dict[key]=4
            elif(data_dict[key]=='Finger Lakes'):
                data_dict[key]=5
            elif(data_dict[key]=='New York City'):
                data_dict[key]=6
            else:
                data_dict[key]=7
        # if key in data_dict is Age then encode it here
        if key == 'Age':
            
            if(data_dict[key]>= 0 or data_dict[key] <=17):
                data_dict[key]=1
                
            elif(data_dict[key]>= 18 or data_dict[key] <=29):
                data_dict[key]=2
                
            elif(data_dict[key]>= 30 or data_dict[key] <=49):
                data_dict[key]=3
                
            elif(data_dict[key]>=50 or data_dict[key] <=69):
                data_dict[key]=4
                
            else:
                data_dict[key]=5
                
        #  if key is Gender then encode it here
        if key == 'Gender':
            
            if(data_dict[key]=='F'):
                data_dict[key]=0
            elif(data_dict[key]=='M'):
                data_dict[key]=1
            else:
                data_dict[key]=2
        
        # if key is Cultural_group then encode it here
        if key == 'Cultural_group':
            
            if(data_dict[key]=='White'):
                data_dict[key]=0
            elif(data_dict[key]=='Black/African American'):
                data_dict[key]=1
            elif(data_dict[key]=='Other Race'):
                data_dict[key]=2
            else:
                data_dict[key]=3 
        
        # if key is admission type then encode it here 
        if key == 'Admission_type':
            if data_dict[key]=='Emergency':
                data_dict[key]=1
                
            elif data_dict[key]=='Elective':
                data_dict[key]=2
                
            elif data_dict[key]=='Urgent':
                data_dict[key]=3
                
            elif data_dict[key]=='Newborn':
                data_dict[key]=4
                
            elif data_dict[key]=='Trauma':
                data_dict[key]=5
                
            else:
                data_dict[key]=6
        # if key is Surgical description then encode it here 
        if key == 'Surg_Description':
            if data_dict[key]=='Medical':
                data_dict[key]=0
            else:
                data_dict[key]=1
        
        # if key is Emergency Department then encode it here
        if key == 'EmergencyDept_yes_No':
            if data_dict[key]=='N':
                data_dict[key]=0
            else:
                data_dict[key]=1
                
        # if key is Payment Typology then encode it here
        if key =='Payment_Typology':
            
            if data_dict[key]=='Medicare':
                data_dict[key]= 1
            elif data_dict[key]=='Medicaid':
                data_dict[key]= 2
            elif data_dict[key]== 'Other Governments':
                data_dict[key]= 3
            elif data_dict[key]== 'Department of Corrections':
                data_dict[key]= 4
            elif data_dict[key]== 'Private Health Insurance':
                data_dict[key]= 5
                
    return data_dict
