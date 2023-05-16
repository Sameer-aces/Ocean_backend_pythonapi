import pickle 

def get_model():
    """imports ML model pickle file and then returns that model instance

    Returns:
        Machine Learning Model: Desicion Tree Algorithm model
    """    
    # import model form the pickle file of model using pickle library 
    model = pickle.load(open('ML_algo\ML_model\model.pkl', 'rb'))
    
    return model
