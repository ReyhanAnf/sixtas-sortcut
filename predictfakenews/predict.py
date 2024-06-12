import joblib
import os
from sixtasSortcut.settings import BASE_DIR
from bs4 import BeautifulSoup
import requests as reqs
import joblib
from sixtasSortcut.settings import BASE_DIR
import os

vector_ic = joblib.load(os.path.join(BASE_DIR, "predictfakenews/ml/tokenize/vectorize_indonesia_content.vec"))
model_ic = joblib.load(os.path.join(BASE_DIR, "predictfakenews/ml/model/model_indonesia_content.sav"))

def scrape(url):
  content_url = reqs.get(url)
  bs4 = BeautifulSoup(content_url.content, "html.parser")
  raw = bs4.find_all("p")
  return [raw, bs4.text]

def vectokenize(tokenizer, data=[]):
  return tokenizer.transform(data)

  
def predict(url, text):
  raw = scrape(url)
  
  content = raw[1]
  token = vectokenize(vector_ic, [content])
  pred = model_ic.predict(token)
  
  return [raw[0], pred[0]]

