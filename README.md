# pyBitcoinAddress
Bitcoin Wallet Address Generator

This is a simple Bitcon wallet address generator coded in Python 3.
It generates a Private Key in different formats (hex, wif and compressed wif) and corresponding Public Addresses, raw, P2WPKH addresses starting with prefix 1 and P2SH addresses starting with prefix 3 as part of Segwit soft fork.

* soon Bench32 addresses starting with prefix bc1

# Usage:
python wallet.py

# Output:
```
Private Key HEX: 37450b5785141a486208d6b58774d4e9f1c7915257c0d578e795c587bb6ac4f7
Private Key WIF: 5JEdNXQuhB4uqLMARdEhX5TJGtFKXjszjknqVeTX3EdZMFVRHU2
Private Key WIF compressed: Ky59Y1EXaKSGCLPzbgwTqkf5F7CCngG5qiHK3SL3asAMnGEAeFG2

Public Key: 0408834b6c3744bc8f286ede05166f3ef75810642cdf65fd0cbc5cf6916a5da605c67f1e641c4b07c4dd79a6a52509aa5264c3596930b3baa42355ca83be39ce24
Public Key compressed: 0208834b6c3744bc8f286ede05166f3ef75810642cdf65fd0cbc5cf6916a5da605

Public Address 1: 19iPwjvPUZfHfTSGnVmcEhjiAvKiDYNxfp
Public Address 3: 331qUgRgz1AyzzRqo3ZLGkeJcGZQbUhtDp
Public Address bc1: 
```
