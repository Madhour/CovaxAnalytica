import pandas as pd
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.manifold import TSNE
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


print(os.getcwd())

df = pd.read_csv(os.getcwd()+'/vaccine_tweets_with_sentiment.csv', index_col=0)
df = df.dropna(subset=['corpus']).reset_index(drop=True)

#build document vector through tf-idf
def tfidf_model(corpus, data):

    tfidf = TfidfVectorizer(min_df = 20, max_df = 0.50, max_features = 50, stop_words = 'english').fit(corpus)
    text_matrix = tfidf.transform(corpus)
    labels = data.index.tolist()

    return tfidf, text_matrix, labels

# splits every tweet into its words
# are defined as characters surrounded by whitespace
def tokenize_corpus(corpus):
    token_list = []

    for i in range(len(corpus)):
        corpus[i] = str(corpus[i])
        token_list.append(corpus[i].split())
    return token_list

# Tags are needed for Doc2Vec
# Function maps (labels) the respective index number to every tweet 
def data_tagging(data, corpus):

    token = tokenize_corpus(corpus)
    tagged_data = []
    
    for i in range(len(data)):
        tagged_data.append(
            TaggedDocument(words=token[i], tags=[str(data.index[i])]))
        
    return tagged_data

# dimensionality reduction
# undergoes 1000 iterations and returns n (components) dimensions
def model_tsne(tokens, components):

    tsne_model = TSNE(perplexity=50, n_components=components, init='pca', n_iter=1000, random_state=38)
    new_values = tsne_model.fit_transform(tokens)
    
    return new_values

#build document vector through Doc2Vec
def doc2vec_model(tagged_data, max_epochs, data):

    model = Doc2Vec(vector_size=100, min_count=35, workers = 6, dm = 1)

    model.build_vocab(tagged_data)

    model.train(tagged_data, total_examples=model.corpus_count, epochs=max_epochs)
    model.alpha -= 0.0002
    model.min_alpha = model.alpha

    tokens = [model.docvecs[i] for i in range(len(model.docvecs))]

    return model, tokens

# Running tf-idf
fitted_tfidf, df_data, df_labels = tfidf_model(df['corpus'][:],df[:])

# exporting tf-idf results
pickle.dump(fitted_tfidf, open("tfidf_model.pickle", "wb"))
pickle.dump(df_data, open("tfidf_matrix.pickle", "wb"))
pickle.dump(df_labels, open("tfidf_labels.pickle", "wb"))
np.save(os.getcwd()+"/tfidf_tsne.npy", model_tsne(df_data.todense(), 2))

# removing the word "vaccine" from tweets as it has low information
for i in range(len(df)):
    try:
        split_list = df.corpus[i].split()
        if "vaccine" in split_list:
            split_list.remove("vaccine")
        df.corpus[i] = " ".join(split_list)
    except:
        pass 


# Running Doc2Vec
doc2vec_model, doc2vec_tokens = doc2vec_model(data_tagging(df[:], df["corpus"][:]), 60, df)

# Exporting Doc2Vec results
doc2vec_model.save(os.getcwd()+"/doc2vec")

# dimensionality reduction (2D)
np.save(os.getcwd()+"/doc2vec_tsne.npy", model_tsne(doc2vec_tokens, 2))

# dimensionality reduction (3D)
np.save(os.getcwd()+"/3d_doc2vec_tsne.npy", model_tsne(doc2vec_tokens, 3))
