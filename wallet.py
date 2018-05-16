import time
import hashlib
import string
import base58
import ecdsa
import random
import math
import binascii

""" Bitcoin Wallet Generator v0.2

         Pedro Fortes - 05/2018

         https://bitcoincore.org/en/segwit_wallet_dev/
         https://pypi.python.org/pypi/ecdsa - ECDSA manual"""

class Keys:

        def __init__(self):
            self.privkeyhex  = ''
            self.privkeywif = ''
            self.privkeywifcompressed = ''
            
            self.pubkey   = ''
            self.pubkeycompressed   = ''
            self.pubaddr1 = ''
            self.pubaddr3 = ''
            self.pubaddrbc1 = ''
 
 
        def seed(self):                                         
            t = int(time.time())
            return str(random.getrandbits(3000) - t)
                        

        def privatekey(self, seed=None):
                
            if(seed==None): seed = self.seed() 
            self.privkeyhex = hashlib.sha256(seed.encode())
                
         
        def privatekeywif(self):
 
            prefix = b'\x80'
            suffix = b'\x01'
            
            d = prefix + self.privkeyhex.digest()     
     
            checksum   = self.doublehash256(d).digest()[:4]
            checksum_c = self.doublehash256(d + suffix).digest()[:4]

            self.privkeywif = base58.b58encode(d + checksum) 
            self.privkeywifcompressed = base58.b58encode(d + suffix + checksum_c) 
         

        def hash160(self, v):
            r = hashlib.new('ripemd160')
            r.update(hashlib.sha256(v).digest())
            return r


        def doublehash256(self, v):
            return hashlib.sha256(hashlib.sha256(v).digest())


        def ecdsaSECP256k1(self, digest):
            # SECP256k1 - Bitcoin elliptic curve 
            sk = ecdsa.SigningKey.from_string(digest, curve=ecdsa.SECP256k1)                    
            return sk.get_verifying_key()

                                
        def publicaddress1(self):

            prefix_a = b'\x04'
            prefix_b = b'\x00'

            digest = self.privkeyhex.digest()
                                  
            p = prefix_a + self.ecdsaSECP256k1(digest).to_string() # 1 + 32 bytes + 32 bytes
            self.pubkey = str(binascii.hexlify(p).decode('utf-8'))
                            
            hash160 = self.hash160(p)

            m = prefix_b + hash160.digest()
            checksum = self.doublehash256(m).digest()[:4]        
        
            self.pubaddr1 = base58.b58encode(m + checksum)                  
             

        def publicaddress3(self):
 
            prefix_even = b'\x02'
            prefix_odd = b'\x03'
            prefix_a = prefix_odd
            prefix_b = b'\x05'
            prefix_redeem = b'\x00\x14'


            digest = self.privkeyhex.digest()
            
            ecdsa_digest = self.ecdsaSECP256k1(digest).to_string()
 
            x_coord = ecdsa_digest[:int(len(ecdsa_digest)/2)]
            y_coord = ecdsa_digest[int(len(ecdsa_digest)/2):]            

            if (int(binascii.hexlify(y_coord),16) % 2 == 0): prefix_a = prefix_even
            
            p = prefix_a + x_coord
            
            self.pubkeycompressed = str(binascii.hexlify(p).decode('utf-8'))

 
            redeem_script = self.hash160(prefix_redeem + self.hash160(p).digest()).digest() # 20 bytes
 
            m = prefix_b + redeem_script
            checksum = self.doublehash256(m).digest()[:4]        
        
            self.pubaddr3 = base58.b58encode(m + checksum)



        def publicaddressbc1(self):

            # soon     
        
            self.pubaddrbc1 = ''          
            
                                        
        def generate(self, seed=None):

            self.privatekey(seed)
            self.privatekeywif()
            
            self.publicaddress1()
            self.publicaddress3()
            self.publicaddressbc1()

        def __str__(self):
                
            return '\nPrivate Key HEX: {0}\nPrivate Key WIF: {1}\nPrivate Key WIF compressed: {2}\n\nPublic Key: {3}\nPublic Key compressed: {4}\n\nPublic Address 1: {5}\nPublic Address 3: {6}\nPublic Address bc1: {7}' \
             .format(self.privkeyhex.hexdigest(), self.privkeywif, self.privkeywifcompressed, self.pubkey, self.pubkeycompressed, self.pubaddr1, self.pubaddr3, self.pubaddrbc1)


if __name__ == "__main__":
        
        wallet = Keys()
        
        wallet.generate()
           
        print(wallet)
  
