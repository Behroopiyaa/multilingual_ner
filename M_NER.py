#Here we will be using three models for language german,english and portugese hence we will be downloading the model using following command

#!python -m spacy download de_core_news_sm

#!python -m spacy download en_core_web_sm

#!python -m spacy download pt_core_news_sm




import spacy
def entites(raw_text,lang_code): 
    
    nlp = spacy.load(str(lang_code) + "_core_news_sm")
    text = nlp(raw_text)
    for word in text.ents:
        return word.text,word.label_,word.start_char,word.end_char


entites('George Washington ging nach Washington','de')