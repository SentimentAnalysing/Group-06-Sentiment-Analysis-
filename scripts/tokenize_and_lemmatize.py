import spacy

nlp = spacy.load("en_core_web_sm")

# Tokenization
def tokenize(comment):
    doc = nlp(comment)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return tokens 

# Lemmatization
def lemmatize(tokens):
    lemmatized_tokens = [token.lemma_ for token in nlp(" ".join(tokens))]
    return " ".join(lemmatized_tokens) 
