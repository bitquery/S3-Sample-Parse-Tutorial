# Schema Sample


## Dex Trades

```JSON
{
  "Currency": {
    "SmartContract": "AQ=="
  },
  "Amount": "...",
  "Data": "..."
}{
  "SmartContract": "...",
  "FeeRecipient": "address"
}
```

## Token 

```JSON
{
  "Receiver": "address"
}{
  "Chain": {
    "ChainId": "AQ==",
    "Config": "Chain ID: ..."
  },
  "Header": {
    "Hash": "8Seudwubc68b6T5aesGb5eO6xBZzsmhca0YZ+wmvCfA=",
    "ParentHash": "WPOjY65rhz/Wzr2BNzpYLrvOH8VQ6bmf0Lf9GKgc13I=",
    "UncleHash": "HcxN6N7HXXqrhbVntszUGtMSRRuUinQT8KFC/UDUk0c=",
    "Root": "dyAy925IxO5z5pgL0BSS5mnBDFjHkeBsrtd3x+TmF9o=",
    "TxHash": "bbFnO0wqGguGsMhC1EBETujvVn6lfhDSd/o8cPr4in0=",
    "ReceiptHash": "fAJT2ZTL2W9AAPdEDzxoJuEZywPFlTSCVp1PvgCPwGc=",
    "MixDigest": "zIkWwqT5SxNyKPY5MWTv/ObnaRg7XsSnjZu0c31BO8c=",
    "Coinbase": "H5CQquKLij3OrfKBsPEoKOZ2wyY=",
    "Bloom": "...",
    "Extra": "cnN5bmMtYnVpbGRlci54eXo=",
    "Number": "AQAK4A==",
    "GasLimit": "30000000",
    "GasUsed": "11692403",
    "Time": "1678235519",
    "BaseFee": "ByGhI+U="
  },
  "Transfers": [
    {
      "CallIndex": "1",
      "Receiver": "ERERElTuslR3to+4Xtkp9zqWBYI=",
      "Amount": "DeC2s6dkAAA=",
      "Currency": {
        "SmartContract": "wCqqObIj/o0KDlxPJ+rZCDx1bMI=",
        "DelegatedTo": "wCqqObIj/o0KDlxPJ+rZCDx1bMI=",
        "ProtocolName": "erc20_deposable",
        "Name": "Wrapped Ether",
        "Symbol": "WETH",
        "Decimals": 18,
        "Fungible": true
      },
      "Success": true
    },
```
