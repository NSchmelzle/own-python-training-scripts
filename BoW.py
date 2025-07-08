def bow(sentence, vocabulary):
    # tokenisieren des sentence
    sentence = sentence.split()
    bow = [0] * len(vocabulary)
    for word in vocabulary:
        if word in sentence:
            bow[vocabulary.index(word)] = 1

    for index in range(0,len(vocabulary)):
        word = vocabulary[index]
        if word in sentence:
            bow[index] = 1

    for index, word in enumerate(vocabulary):
        if word in sentence:
            bow[index] = 1

    return bow
 