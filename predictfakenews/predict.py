import joblib
import os
from sixtasSortcut.settings import BASE_DIR
from bs4 import BeautifulSoup
import requests as reqs
from googletrans import Translator
import os
import re

vector_it = joblib.load(os.path.join(BASE_DIR, "predictfakenews/ml/tokenize/vectorize_indonesia_title.vec"))
vector_ic = joblib.load(os.path.join(BASE_DIR, "predictfakenews/ml/tokenize/vectorize_indonesia_content.vec"))
vector_et = joblib.load(os.path.join(BASE_DIR, "predictfakenews/ml/tokenize/vectorize_english_title.vec"))
vector_ec = joblib.load(os.path.join(BASE_DIR, "predictfakenews/ml/tokenize/vectorize_english_content.vec"))


model_it = joblib.load(os.path.join(BASE_DIR, "predictfakenews/ml/model/model_indonesia_title.sav"))
model_ic = joblib.load(os.path.join(BASE_DIR, "predictfakenews/ml/model/model_indonesia_content.sav"))
model_et = joblib.load(os.path.join(BASE_DIR, "predictfakenews/ml/model/model_english_title.sav"))
model_ec = joblib.load(os.path.join(BASE_DIR, "predictfakenews/ml/model/model_english_content.sav"))

def scrape(url):
  content_url = reqs.get(url)
  bs4 = BeautifulSoup(content_url.content, "html.parser")
  raw = bs4.find_all("p")
  
  title = str(bs4.title).split("<title>")[1].split("</title>")[0]
  text = bs4.text
  to_predict = [title, text]
  titleraw = str(bs4.title)
  
  return {"raw": raw, "title" : titleraw, "to_predict": to_predict}

def remove_punk(word):
  lower_string = word.lower()
  # remove numbers
  no_number_string = re.sub(r'\d+','',lower_string)
  # remove all punctuation except words and space
  no_punc_string = re.sub(r'[^\w\s]','', no_number_string) 
  # remove white spaces
  no_wspace_string = no_punc_string.strip()
  return no_wspace_string

def vectokenize(tokenizer, data=[]):
  return tokenizer.transform(data)

def translate(word):
  translator = Translator()
  translation = translator.translate( word, dest='en')
  return translation.text
  
def predict(url, text):
  if len(url) > 6 :
    content = scrape(url)
    to_predict = content["to_predict"]
    
    to_predict_en = translate(str(to_predict[0]))
    
    veci_t = vectokenize(vector_it, [to_predict[0]])
    veci_c = vectokenize(vector_ic, [to_predict[1]])
    vece_t = vectokenize(vector_et, [to_predict_en])
    vece_c = vectokenize(vector_ec, [to_predict[1]])
    
    predi_t1 = model_it.predict(veci_t)[0]
    predi_c1 = model_ic.predict(veci_c)[0]
    prede_t1 = model_et.predict(vece_t)[0]
    prede_c1 = model_ec.predict(vece_c)
    predi_t2 = model_it.predict(veci_t)[0]
    predi_c2 = model_ic.predict(veci_c)[0]
    prede_t2 = model_et.predict(vece_t)[0]
    prede_c2 = model_ec.predict(vece_c)
    
    
    def r2n(pred):
      if pred == "REAL":
        return 0
      elif pred == "FAKE":
        return 1
    
      
    prede_ts1 = r2n(prede_t1)
    prede_cs1 = r2n(prede_c1)
    prede_ts2 = r2n(prede_t2)
    prede_cs2 = r2n(prede_c2)

    
    
    result =  (predi_t1 + predi_c1 + prede_ts1 + prede_cs1 + predi_t2 + predi_c2 + prede_ts2 + prede_cs2) / 8 * 100
    print(result , "% Hoaks")
    
    return [content["raw"], content["title"], result]
  
  elif len(text) > 10 :
    veci_t = vectokenize(vector_it, [text])
    predi_t = model_it.predict(veci_t)[0]
    
    raw = f"<p>{text}</p>"
    
    return [raw, predi_t * 1/1 * 100]
  
  else:
    return [f"<p>Text should minimum 10 caracter</p>", 100]

