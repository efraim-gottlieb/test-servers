from fastapi import FastAPI, HTTPException
import os
from utils.encryption import CaesarEncryption as caesar
from utils.encryption import FenceEncryption as fence


app = FastAPI()

caesar_encryption = caesar()
fence_encryption = fence()

@app.get('/test/{name}')
def add_name(name):
  if not os.path.isdir('data'):
    os.mkdir('data')
  with open('data/names.txt', 'a') as names_file:
    names_file.write(name + '\n')
  return { "msg": "saved user"}

@app.post('/caesar')
def caesar(body :dict):
  if body['mode'] == 'encrypt':
    return {'encrypted_text' : caesar_encryption.encrypt(body['text'], body['offset'])}
  if body['mode'] == 'decrypt':
    return {'decrypted_text' : caesar_encryption.decrypt(body['text'], body['offset'])}

@app.get('/fence/encrypt')
def fence_encrypt(text: str):
  return {'encrypted_text' : fence_encryption.encrypt(text)}

@app.post('/fence/decrypt')
def fence_decrypt(text):
  return {'decrypted_text' : fence_encryption.decrypt(text) }



