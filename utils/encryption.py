class CaesarEncryption:
  def __init__(self, offset :int):
    self.offset = offset
    self.a_z = [chr(i) for i in range(97,123)]

  def encrypt(self, text):
    encrypted = ''
    for ch in text:
      encrypted += self.a_z[((ord(ch)-97 + self.offset) % 26)]
    return encrypted

  def decrypt(self, text):
    decrypted = ''
    for ch in text:
      decrypted += self.a_z[((ord(ch)-97 - self.offset) % 26)]
    return decrypted

# class FenceEncryption:
#   def encrypt(text):
#     return {}
  
#   def decrypt(text):
#     return {}
