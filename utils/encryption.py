class CaesarEncryption:
  def __init__(self):
    self.a_z = [chr(i) for i in range(97,123)]

  def encrypt(self, text, offset :int):
    encrypted = ''
    for ch in text.lower():
      if ch == ' ':
        encrypted += ' '
        continue
      encrypted += self.a_z[((ord(ch)-97 + offset) % 26)]
    return encrypted

  def decrypt(self, text, offset :int):
    decrypted = ''
    for ch in text:
      if ch == ' ':
        decrypted += ' '
        continue
      decrypted += self.a_z[((ord(ch)-97 - offset) % 26)]
    return decrypted

class FenceEncryption:
  @staticmethod
  def encrypt(text):
    encrypted_1 = ''
    encrypted_2 = ''
    for i, char in enumerate(text):
      if i%2 ==0:
        encrypted_1 += char
      else:
        encrypted_2 += char
    return encrypted_1+encrypted_2

  @staticmethod
  def decrypt(text):
    l_1 = list(text[len(text)//2:])
    l_2 = list(text[:len(text)//2])
    decrypted = ''
    for i in range(len(text)):
      if l_2:
        decrypted += l_2.pop(0)
      if l_1:
        decrypted += l_1.pop(0)
    return decrypted



