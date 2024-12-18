import spacy

def get_token_lemmas(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    token_lemmas = []

    for token in doc:
        token_lemmas.append(token.lemma_)

    return token_lemmas