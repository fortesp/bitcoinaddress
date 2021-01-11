# Bitcoin Address

[![](https://img.shields.io/github/v/release/fortesp/bitcoinaddress)](https://github.com/fortesp/bitcoinaddress)
[![](https://img.shields.io/github/stars/fortesp/bitcoinaddress.svg)](https://github.com/fortesp/bitcoinaddress)
[![](https://img.shields.io/github/issues/fortesp/bitcoinaddress)](https://github.com/fortesp/bitcoinaddress)
[![](https://img.shields.io/github/license/fortesp/bitcoinaddress?style)](https://github.com/fortesp/bitcoinaddress)

### Bitcoin Wallet Address Generator

This is a simple Bitcoin non-deterministic wallet address generator coded in Python 3. It generates a Private Key in different
formats (hex, wif and compressed wif) and corresponding Public Addresses, raw, P2WPKH addresses starting with prefix 1, P2SH addresses
starting with prefix 3 as part of Segwit soft fork and Bech32 addresses with prefix bc1 P2WPKH and P2WSH.

## Installation

```
pip install bitcoinaddress
```

## Usage

###### Example 1 - Mainnet

```python
from bitcoinaddress import Wallet

wallet = Wallet()
print(wallet)
```

###### Output:

```
Private Key HEX: 03902e4f09664bc177fe4e090dcd9906b432b50f15fb6151984475c1c75c35b6
Private Key WIF: 5HqrbgkWPqBy6dvCE7FoUiMuiCfFPRdtRsyi6NuCM2np8qBZxq5
Private Key WIF compressed: KwLdv6T2jmhQbswnYrcL9KZHerTpVyjozp1JNjfP5QuD3GchCwCc 
            
Public Key: 04c5389a31ce6149c28ba20d14db8540b2319e5a65000a2919fbf7a6296e7840b53f883a9483fb7f2b43f3eacd857c904d1b70ecc168571b64d8f1ab82b57eea88 
Public Key compressed: 02c5389a31ce6149c28ba20d14db8540b2319e5a65000a2919fbf7a6296e7840b5

Public Address 1: 1Bu6YxH64nfvhdDsYNEP8PftoBMqgusdPS   
Public Address 1 compressed: 18i5PtPisxbGiGGEviW7HPcnfNPmcsscwH   
Public Address 3: 38dRrGx5YbrnRWuWcJv5i2XHjYUnHE2wvv  
Public Address bc1 P2WPKH: bc1q2jxe5azr6zmhk3258av7ul6cqtu4eu4mps8f4p    
Public Address bc1 P2WSH: bc1qdveuf0egtfdnd2fnsp0lzfukn2e58czf8323ky6xt8ydew4ecfcqv3ettx  
```

###### Example 2 - Testnet

```python
from bitcoinaddress import Wallet

wallet = Wallet(testnet=True)
print(wallet)
```

###### Output:

```
Private Key HEX: 064f8f0bebfa2f65db003b56bc911535614f2764799bc89091398c1aed82e884
Private Key WIF: 91dhN38UTmqGtd3zG1GnDdnyivAP5LnWJQyyj7V7pqthirHAj4X
Private Key WIF compressed: cMny9rPzDAt58r8BjECeamPwN1eQSAKrKrrVNsd78AoCjcWxuVym 
            
Public Key: 04f7a01e30388dea9673db8cdb48b985441db785382efbcecc05abac079a6304818a907f886b0d0518e345a0288a6f1e09072f2b11d4ccb75bc67ec6c71dfef800 
Public Key compressed: 02f7a01e30388dea9673db8cdb48b985441db785382efbcecc05abac079a630481

Public Address 1: mwdHSyBBHMbcy8rogvzssvDrGyffRo3amQ   
Public Address 1 compressed: n4VzeGfAyZGR7xCXiKmABvnKXojTFJrmKH   
Public Address 3: 2MtJ3jPSD2AYgbF25fq9cm1aUCPhSmWUMcJ  
Public Address bc1 P2WPKH: tb1qlsw8qqe2aa2avzn9t9nsfjy8kwwgarwcfvfqlh    
Public Address bc1 P2WSH: tb1qp53qkcsth8ffuvr00cnlg5hde03aszzeq7y0layklhd4nwkxzejs99tlh3
```

###### Example 3 - Import Private Key

```python
from bitcoinaddress import Wallet

wallet = Wallet('5HqrbgkWPqBy6dvCE7FoUiMuiCfFPRdtRsyi6NuCM2np8qBZxq5')
print(wallet)
```

###### Output:

```
Private Key HEX: 03902e4f09664bc177fe4e090dcd9906b432b50f15fb6151984475c1c75c35b6
Private Key WIF: 5HqrbgkWPqBy6dvCE7FoUiMuiCfFPRdtRsyi6NuCM2np8qBZxq5
Private Key WIF compressed: KwLdv6T2jmhQbswnYrcL9KZHerTpVyjozp1JNjfP5QuD3GchCwCc 
            
Public Key: 04c5389a31ce6149c28ba20d14db8540b2319e5a65000a2919fbf7a6296e7840b53f883a9483fb7f2b43f3eacd857c904d1b70ecc168571b64d8f1ab82b57eea88 
Public Key compressed: 02c5389a31ce6149c28ba20d14db8540b2319e5a65000a2919fbf7a6296e7840b5

Public Address 1: 1Bu6YxH64nfvhdDsYNEP8PftoBMqgusdPS   
Public Address 1 compressed: 18i5PtPisxbGiGGEviW7HPcnfNPmcsscwH   
Public Address 3: 38dRrGx5YbrnRWuWcJv5i2XHjYUnHE2wvv  
Public Address bc1 P2WPKH: bc1q2jxe5azr6zmhk3258av7ul6cqtu4eu4mps8f4p    
Public Address bc1 P2WSH: bc1qdveuf0egtfdnd2fnsp0lzfukn2e58czf8323ky6xt8ydew4ecfcqv3ettx
```

###### Example 4 - Check attributes

```python
from bitcoinaddress import Wallet

wallet = Wallet()
print(wallet.key.__dict__)
print(wallet.key.__dict__['mainnet'].__dict__)
print(wallet.key.__dict__['testnet'].__dict__)
print(wallet.address.__dict__)
print(wallet.address.__dict__['mainnet'].__dict__)
print(wallet.address.__dict__['testnet'].__dict__)
```

## License and other

This software is distributed under the terms of the MIT License. See the file 'LICENSE' in the root directory of the present
distribution, or http://opensource.org/licenses/MIT.

Bech32 address scripts source from https://github.com/sipa/bech32/tree/master/ref/python
