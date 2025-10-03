# This is a dummy predictor function.
# The ML Engineer on your team will replace this with the actual model logic.

def predict_disease(image_data):
    """
    Takes image data, and returns a mock prediction.
    In the future, this function will load the trained model and pre-process
    the image to make a real prediction.
    """
    print("Dummy predictor called. In a real scenario, an ML model would process the image here.")
    
    # For now, just return a hardcoded result.
    return {
        'disease': 'Mock: Early Blight',
        'confidence': 0.92,
        'remedy': 'Apply copper-based fungicides. Ensure proper plant spacing for better air circulation.'
    }