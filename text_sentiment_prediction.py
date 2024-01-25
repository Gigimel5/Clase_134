import pandas as pd
import numpy as np

import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
# datos de entrenamiento
train_data = pd.read_csv("./static/data_files/tweet_emotions.csv")    
training_sentences = []

for i in range(len(train_data)):
    sentence = train_data.loc[i, "content"]
    training_sentences.append(sentence)

# cargar modelo
model = load_model("./static/model_files/Tweet_Emotion.h5")

vocab_size = 40000
max_length = 100
trunc_type = "post"
padding_type = "post"
oov_tok = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)

# asignar emoticones para diferentes emociones
emo_code_url = {
    "empty": [0, "./static/emoticons/Empty.png"],
    "sadness": [1,"./static/emoticons/Sadness.png" ],
    "enthusiasm": [2, "./static/emoticons/Enthusiasm.png"],
    "neutral": [3, "./static/emoticons/Neutral.png"],
    "worry": [4, "./static/emoticons/Worry.png"],
    "surprise": [5, "./static/emoticons/Surprise.png"],
    "love": [6, "./static/emoticons/Love.png"],
    "fun": [7, "./static/emoticons/Fun.png"],
    "hate": [8, "./static/emoticons/Hate.png"],
    "happiness": [9, "./static/emoticons/Happiness.png"],
    "boredom": [10, "./static/emoticons/Boredom.png"],
    "relief": [11, "./static/emoticons/Relief.png"],
    "anger": [12, "./static/emoticons/Anger.png"]
    
    }
# escribir la función para predecir la emoción
def predict (text):
    emotion=""
    emoticon=""
    if (text!=""):
        oracion=[]
        oracion.append(text)
        oracionT=tokenizer.text_to_sequences(oracion)
        padded=pad_sequences(oracionT, maxLen=max_length, padding=padding_type, truncating=trunc_type)
        testing_padded=np.array(padded)
        predictLabel=np.argmax(model.predict(testing_padded),axis=1)
        print(predictLabel)
        for key,value in emo_code_url.items():
            if (value[0]==predictLabel):
                emoticon=value[1]
                emotion=key
        return emotion,emoticon