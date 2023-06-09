# import pickle 

# def get_model():
#     """imports ML model pickle file and then returns that model instance

#     Returns:
#         Machine Learning Model: Desicion Tree Algorithm model
#     """    
#     # import model form the pickle file of model using pickle library 
#     model = pickle.load(open('ML_algo\ML_model\model.pkl', 'rb'))
    
#     return model
import os
import pickle
from django.conf import settings

def get_model():
    """imports ML model pickle file and then returns that model instance

    Returns:
        Machine Learning Model: Desicion Tree Algorithm model
    """    
    # Construct the full path to the pickle file.
    model_path = os.path.join(settings.BASE_DIR, 'ML_algo', 'ML_model', 'model.pkl')

    # Import model form the pickle file of model using pickle library 
    model = pickle.load(open(model_path, 'rb'))

    return model