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
  # def encrypt(text):
  #   encrypted = [i for i in text if not text.indexof(i) %2 and i != ' '] + [i for i in text if text.index(i) %2 and i != ' ']
  #   return ''.join(encrypted)
  def encrypt(text):
    encrypted = ''
    for i, char in enumerate(text):
      if i%2 ==0:
        encrypted += char
      encrypted += char
      return encrypted

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
a = FenceEncryption()

b = a.encrypt('moshewwew+')
print(b)


