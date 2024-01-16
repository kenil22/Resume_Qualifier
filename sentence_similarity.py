import fasttext

model = fasttext.load_model('cc.en.300.bin')

def fast_text_similarity_finder(text1, text2):
    vector1 = model.get_sentence_vector(text1)
    vector2 = model.get_sentence_vector(text2)

    from scipy.spatial.distance import cosine
    similarity = 1 - cosine(vector1, vector2)
    return similarity
