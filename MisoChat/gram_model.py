import konlpy
from tensorflow.contrib import learn

HIDDEN_SIZE = 25
EMBEDDING_SIZE = 25
def grammar_model(X, y):
    word_vectors = learn.ops.categorical_variable(X, n_classes=n_disintegrated_words, embedding_size=EMBEDDING_SIZE, name='words')

def get_training_data_by_disintegration(sentence):
    disintegrated_sentence = konlpy.tag.Twitter().pos(sentence, norm=True, stem=True)
    original_sentence = konlpy.tag.Twitter().pos(sentence)
    inputData = []
    outputData = []
    is_asking = False

    for w, t in disintegrated_sentence:
        if t not in ['Eomi', 'Josa', 'Number', 'KoreanParticle', 'Punctuation']:
            inputData.append(w + '/' + t)
    for w, t in original_sentence:
        if t not in ['Number', 'Punctuation']:
            outputData.append(w)
    if original_sentence[-1][1] == 'Punctuation' and original_sentence[-1][0] == "?":
        if len(inputData) != 0 and len(outputData) != 0:
            is_asking = True # To Extract ask-response raw data
    return ' '.join(inputData), ' '.join(outputData), is_asking
