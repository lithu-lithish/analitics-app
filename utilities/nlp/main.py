import pandas as pd
import nltk
from database.pixelgen.pixelgen_database import db_pixelgen, get_images_data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from utilities.main import explode_df, groupby_count

nltk.download('punkt')
nltk.download("stopwords")
images = get_images_data(db_pixelgen)
stop_words = set(stopwords.words('english'))
punctuation_chars = set(string.punctuation)

filtered_nlp_images = images[images['prompt_type']=='your_prompt']
filtered_nlp_images['tokenize'] = filtered_nlp_images['prompt'].apply(word_tokenize)

def remove_stopwords(tokenize):
    return [word for word in tokenize if word.lower() not in stop_words and word not in punctuation_chars]

filtered_nlp_images['removed_stopwords'] = filtered_nlp_images['tokenize'].apply(remove_stopwords)
exploded_nlp_images = explode_df(filtered_nlp_images, 'removed_stopwords')
user_input_keywords = groupby_count(exploded_nlp_images, 'removed_stopwords')