# Bitcoin Address 
### v.0.1.0
Bitcoin Wallet Address Generator

This is a simple Bitcoin wallet address generator coded in Python 3.
It generates a Private Key in different formats (hex, wif and compressed wif) and corresponding Public Addresses, raw, P2WPKH addresses starting with prefix 1, P2SH addresses starting with prefix 3 as part of Segwit soft fork and Bech32 addresses with prefix bc1 P2WPKH and P2WSH.

## Installation
```
pip install bitcoinaddress
```

## Usage
###### Example 1
```
from bitcoinaddress import Wallet

wallet = Wallet()
print(wallet)
```

###### Output:
```
Private Key HEX: c2814c56793485f803430ef28ea93ba34e1dc74a74cead43407378350a958792

Private Key WIF: 5KHwxCT8Nrb3MSiQRS5h6fqmAJWrXzi9min15xSzY1EuR3EgLHT
Private Key WIF compressed: L3joYdYKZTsFPEVkNqhhz2SDv4JmdoidiPPdNsjiwr4NLr31PkqK
Private Key WIF (TESTNET): 934aXwGfy5fBKWDh3mybyGPioxsZhAFM7fdxAaoVsjyxC7vYTv3
Private Key WIF compressed (TESTNET): cU6o1YYAzXZWYfy1mFWqMLwHYHcBJFpKnRY6VJCESxiNbbCpd33r 
                
Public Key: 04a0a7d1d00d970b0be7594b5ab12f930d8275156e2d66f92d39525a44c339aff0fb02568075a8928e9f8a865f0e9633482cf8e5b3bb27c8a7279e9afbc06f9072 
Public Key compressed: 02a0a7d1d00d970b0be7594b5ab12f930d8275156e2d66f92d39525a44c339aff0
 
Public Address 1: 1FdqdaXsPTdzHY83NLpue33S2pW1joXcWr   
Public Address 3: 3ExX4G6qPBDbMpQH6h1Ka7g26322JQtUfd  
Public Address bc1 P2WSH: bc1q27qee3seastzzqgqvyrglj763sw69rymd2m3hv4ph6u7fx2g8a6skzcqer    
Public Address bc1 P2WPKH: bc1qv2m5c60h0vnjjuyefwlczla85ctjuev0q4uqkt  
Public Address 1 (TESTNET): mv9nvdcrCV5F4ebf5uoHTxFktp6ig1jKtv   
Public Address 3 (TESTNET): 2N6Wj812rzdiwZc2pmpdCC4fHJPEC6YyLL4  
Public Address tb1 P2WSH (TESTNET): tb1q27qee3seastzzqgqvyrglj763sw69rymd2m3hv4ph6u7fx2g8a6sp2w0rv    
Public Address tb1 P2WPKH (TESTNET): tb1qv2m5c60h0vnjjuyefwlczla85ctjuev02n8ndc  
```

###### Example 2
```
from bitcoinaddress import Address, Key

key = Key()
key_dict = key.generate()
print(key_dict)

address = Address(key)
address_dict = address.generate()
print(address_dict)
```

###### Output:
```
{'hex': '669182eb2c3169e01cfc305034dc0b1df8328c274865e70d632c711ba62ec3d3', 
'wif': '5JbTZ4zCTn1rwCfdkPWLddFgqzieGaG9Qjp3iRhf7R8gNroj4KM', 
'wifc': 'Kzf6CYbTbBgoQEVXCWLVef1psFkoVjor7mxeyr2TDKWto7iHfXHh', 
'testnet': {
    'hex': '669182eb2c3169e01cfc305034dc0b1df8328c274865e70d632c711ba62ec3d3', 
    'wif': '92N68ook415zuGAvNjQFWDoeVf5MRjoLkgfzo44AT9sj9qhLBkU', 
    'wifc': 'cR25fTbK2FP4Zfxnav9d1yWtVV4DABuYBp786GUxiSAu3rpq6gkk'}}

{'pubkey': '04e61341f46b529b0fac2c5e15a67af7affceb2be7544af18d14206fff041c02c04d6ca36c97f458cfe5754ce15a8f32d4c917b5f0f5e336042ee3be77c3f58222', 
'pubkeyc': '02e61341f46b529b0fac2c5e15a67af7affceb2be7544af18d14206fff041c02c0', 
'pubaddr1': '1NaChZV4JJysct8QYcMKFHnQ2SNFpnBund', 
'pubaddr3': '34QhdWUjZjv3HLyvNYgb4AR7ikAfcdzfCW', 
'pubaddrbc1_p2wsh': 'bc1qup6umurcl7s6zw42gcxfzl346psazws74x72ty6gmlvkaxz6kv4sqsth99', 
'pubaddrbc1_p2wpkh': 'bc1qsnwc0y43fpljyl2ep0e2gtsqa55utcj4ntzwlf', 
'testnet': {
    'pubkey': '04e61341f46b529b0fac2c5e15a67af7affceb2be7544af18d14206fff041c02c04d6ca36c97f458cfe5754ce15a8f32d4c917b5f0f5e336042ee3be77c3f58222', 
    'pubkeyc': '02e61341f46b529b0fac2c5e15a67af7affceb2be7544af18d14206fff041c02c0', 
    'pubaddr1': 'n369zca37LR8Pzc2GBKh5CzitRxxhkHDhK', 
    'pubaddr3': '2MuxuhFQmBCRPV8cU3gJTg7QNw6NqTuUm2A', 
    'pubaddrbc1_p2wsh': 'tb1qup6umurcl7s6zw42gcxfzl346psazws74x72ty6gmlvkaxz6kv4shcacl2', 
    'pubaddrbc1_p2wpkh': 'tb1qsnwc0y43fpljyl2ep0e2gtsqa55utcj4edeay6'}}

```


## Authors
Pedro Fortes and others who contribute.


## License
This software is distributed under the terms of the MIT License. 
See the file 'LICENSE' in the root directory of the present distribution, or http://opensource.org/licenses/MIT.

Bech32 address scripts source from https://github.com/sipa/bech32/tree/master/ref/python
