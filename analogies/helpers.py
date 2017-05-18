import word2vec

import os
from nlp_sockets.settings import BASE_DIR

corpus_location = os.path.join(BASE_DIR, 'assets/text8.bin')

model = word2vec.load(corpus_location)

def analogy(positive_word_list, negative_word_list):
    try:
        print("lists")
        print(positive_word_list)
        print(negative_word_list)
        indexes, metrics = model.analogy(pos=positive_word_list, neg=negative_word_list, n=1)
        bestWordMatch = model.generate_response(indexes, metrics).tolist()[0][0]

        return {'result': bestWordMatch, 'positive_word_list': positive_word_list, 'negative_word_list': negative_word_list}
    except:
        return {'error': 'invalid words entered'}