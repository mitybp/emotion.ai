import pandas as pd
import numpy as np

import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


train_data = pd.read_csv("./static/assets/data_files/tweet_emotions.csv")    
training_sentences = []

for i in range(len(train_data)):
    sentence = train_data.loc[i, "content"]
    training_sentences.append(sentence)

model = load_model("./static/assets/model_files/Tweet_Emotion.h5")

vocab_size = 40000
max_length = 100
trunc_type = "post"
padding_type = "post"
oov_tok = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)

emo_code_url = {
    "Empty": [0, "./static/assets/emoticons/Empty.png"],
    "Sadness": [1,"./static/assets/emoticons/Sadness.png" ],
    "Enthusiastic": [2, "./static/assets/emoticons/Enthusiastic.png"],
    "Neutral": [3, "./static/assets/emoticons/Neutral.png"],
    "Worry": [4, "./static/assets/emoticons/Worry.png"],
    "Surprise": [5, "./static/assets/emoticons/Surprise.png"],
    "Love": [6, "./static/assets/emoticons/Love.png"],
    "Fun": [7, "./static/assets/emoticons/fun.png"],
    "Hate": [8, "./static/assets/emoticons/hate.png"],
    "Happiness": [9, "./static/assets/emoticons/happiness.png"],
    "Boredom": [10, "./static/assets/emoticons/boredom.png"],
    "Relief": [11, "./static/assets/emoticons/relief.png"],
    "Anger": [12, "./static/assets/emoticons/anger.png"]
}

def predict(text):

    predicted_emotion=""
    predicted_emotion_img_url=""
    
    if  text!="":
        sentence = []
        sentence.append(text)

        sequences = tokenizer.texts_to_sequences(sentence)

        padded = pad_sequences(
            sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type
        )
        testing_padded = np.array(padded)

        predicted_class_label = np.argmax(model.predict(testing_padded), axis=1)        
        print(predicted_class_label)   
        for key, value in emo_code_url.items():
            if value[0]==predicted_class_label:
                predicted_emotion_img_url=value[1]
                predicted_emotion=key
        return predicted_emotion, predicted_emotion_img_url
