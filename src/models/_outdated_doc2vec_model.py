import pandas as pd
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.manifold import TSNE
import os

print(os.getcwd())

df = pd.read_csv(os.getcwd()+'/data/processed/processed_vaccine_tweets.csv', index_col=0)
df = df.drop(index=[54230, 56897,81029]).reset_index(drop=True)


def tokenize_corpus(corpus):

    token_list = []
    for i in range(len(corpus)):
        corpus[i] = str(corpus[i])
        token_list.append(corpus[i].split())
    return token_list

def data_tagging(data, corpus):

    token = tokenize_corpus(corpus)
    tagged_data = []
    
    for i in range(len(data)):
        tagged_data.append(
            TaggedDocument(words=token[i], tags=[str(data.index[i])]))
        
    return tagged_data

def model_tsne(tokens):

    tsne_model = TSNE(perplexity=50, n_components=2, init='pca', n_iter=500, random_state=38)
    new_values = tsne_model.fit_transform(tokens)
    
    return new_values

def doc2vec_model(tagged_data, max_epochs, data):

    model = Doc2Vec(vector_size=100, min_count=35, workers = 6, dm = 1)

    model.build_vocab(tagged_data)


    model.train(tagged_data, total_examples=model.corpus_count, epochs=max_epochs)
    model.alpha -= 0.0002
    model.min_alpha = model.alpha

    tokens = [model.docvecs[i] for i in range(len(model.docvecs))]

    return model, tokens
    
doc2vec_model, doc2vec_tokens = doc2vec_model(data_tagging(df[:], df["corpus"][:]), 30, df)

doc2vec_model.save(os.getcwd()+"/models/doc2vec")

np.save(os.getcwd()+"/models/doc2vec_tsne.npy", model_tsne(doc2vec_tokens))
