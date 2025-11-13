from fastapi import FastAPI #, HTTPException
import os
app = FastAPI()



@app.get('/test/{name}')
def add_name(name):
  with open('data/names.txt', 'a') as names_file:
    names_file.write(name + '\n')
  return { "msg": "saved user"}

@app.post('/caesar')
def caesar(body :dict):
  return {"encrypted_text": body['text'][::-1]}

@app.get('/fence/encrypt/{text}')
def fence_encrypt(text: str) -> str:
  return text[::-1]

@app.post('/fence/decrypt/{text}')
def fence_decrypt(text):
  return text[::-1]


