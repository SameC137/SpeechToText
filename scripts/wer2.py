from jiwer import wer
import numpy as np
from utils import int_sequence_to_text
from tensorflow.keras import backend as K

def calculate_wer_entire(model,features,text):
    assert len(features) == len(text), "Length of features and text needs to be the same"
    
    predictions=make_predictions(model,features)
    error=wer(text,predictions)
    return error


def make_predictions(model,features):
    predictions=[]
    for i in features:
        data_point=i.T
        prediction = model.predict(np.expand_dims(i.T, axis=0))
        output_length = [model.output_length(data_point.shape[0])]
        pred_ints = (K.eval(K.ctc_decode(
                prediction, output_length, greedy=False)[0][0])+1).flatten().tolist()
        predicted = ''.join(int_sequence_to_text(pred_ints)).replace("<SPACE>", " ")

        predictions.append(predicted)
    return predictions