import pickle
import numpy as np
from ML_algo.ML_model.ML_model import get_model
from ML_algo.services.label_encode import encode 

def prediction(data:dict=None)->dict:
    """_summary_

    Args:
        data (dict, optional): _description_. Defaults to None.

    Returns:
        dict: _description_
    """    
    model = get_model()
    
    sample:dict = encode(data)
    
    arr = list(sample.values())
    narr = np.array(arr)
    print(f'{type(narr) } \t {narr}')
    
    predicted_value = model.predict([arr]).tolist()[0]
    
    return { predicted_value}
    
    
    ...