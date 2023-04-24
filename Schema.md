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
## Transaction

```JSON
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
    "Bloom": "U6VzYBkQWAAmPBCYixxHJA2U0BMEApawAQGlgBWKPAhARouEgAJ9oywRHgxLa9OagsVcRp2gMYB+GAlAFHZqihCR2ARkKozMaoNKPAZcgnjxgJICREU4VQUI2FGRCTEilhQvBDIG1EAFl5QISDI+SYoSImc6HUcGiEEC8hZYYQIhmBdGv+tEMNZEuI2AJhi5ptVISUFBFGjOpFxGQBGwCJvoIWBrJm/LCfBqwAVgh9KgJAAFZKuIDoiuToUHLAtBS0AjgiAIBJCASEiFMIBx0s9nYvACilAcgNWtRgIA6nBAO2c+gc3tqAoMdbGDpDiECTlwSRBcAmCCyIw7iCE8kw==",
    "Extra": "cnN5bmMtYnVpbGRlci54eXo=",
    "Number": "AQAK4A==",
    "GasLimit": "30000000",
    "GasUsed": "11692403",
    "Time": "1678235519",
    "BaseFee": "ByGhI+U="
  },
  "Reward": {
    "Total": "8x45savI0Q==",
    "Dynamic": "8x45savI0Q==",
    "TxFees": "BetwQ9oB1bA=",
    "BurntFees": "BPhSCihWDN8="
  },
  "Transactions": [
    {
      "TransactionHeader": {
        "Hash": "jrE3G7HZCaHsKn4mFPFX9yFbPzbDn2FIZfG5XuetivA=",
        "Gas": "250752",
        "Value": "DeC2s6dkAAA=",
        "Data": "5EkCLgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3gtrOnZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADUFU4AhASFzx0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAAAAAAAAAAAA4FVKR2oJJwOr2z7zXIDg120yk58AAAAAAAAAAAAAAAAwZ8MFS0pgX54ye62C2bpgSf52oOJrmXc=",
        "Nonce": "7",
        "ChainId": "AQ==",
        "Cost": "DgSHZOtcwYA=",
        "GasFeeCap": "CVxPQsU=",
        "GasPrice": "CVxPQsU=",
        "GasTipCap": "IM2btQ==",
        "Protected": true,
        "Type": 2,
        "To": "ERERElTuslR3to+4Xtkp9zqWBYI=",
        "From": "rdcDZTcww0htraJZSH3JtNXOQMU=",
        "ToCode": {
          "Hash": "shGEiTu1uJqFRoiDBwcCBF2YIbYuo7KNPoTYmrhP0j4=",
          "Size": 22484
        }
      },
      "ReceiptHeader": {
        "Bloom": "AAQAIAAAAAAgAAAAAAAABAEAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAgAAAAgAIAAAAAAAAAAAAAAQgAAAAAgICAACCAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAEAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQEAAAAAIAAAAAAAAAAAAAAAACgIAAAAAAAABAAAAAAEAAIAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAACAAAAAAAAAEAAAAAAAAAQAAAAAAAEAAAAAAAAAAAA==",
        "GasUsed": "187464",
        "Type": 2,
        "ContractAddress": "AAAAAAAAAAAAAAAAAAAAAAAAAAA=",
        "CumulativeGasUsed": "187464",
        "Status": "1",
        "ContractAddressCode": {
          "Hash": "xdJGAYb3IzySfn2y3McDwOUAtlPKgic7e/rYBF2FpHA="
        }
      },
      "TransactionFee": {
        "SenderFee": "FMP/WwI7UA==",
        "PriorityFeePerGas": "IM2btQ==",
        "EffectiveGasPrice": "B0Juv5o=",
        "GasRefund": "63288",
        "Burnt": "FGYqN/TkaA==",
        "Savings": "BgKVPjPYGA==",
        "MinerReward": "XdUjDVbo"
      },
      "TransactionStatus": {
        "Success": true
      },
      "Calls": [
        {
          "Header": {
            "CallerIndex": -1,
            "InternalCalls": 3,
            "From": "rdcDZTcww0htraJZSH3JtNXOQMU=",
            "To": "ERERElTuslR3to+4Xtkp9zqWBYI=",
            "Input": "5EkCLgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3gtrOnZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADUFU4AhASFzx0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwAAAAAAAAAAAAAAA4FVKR2oJJwOr2z7zXIDg120yk58AAAAAAAAAAAAAAAAwZ8MFS0pgX54ye62C2bpgSf52oOJrmXc=",
            "Gas": "228172",
            "Value": "DeC2s6dkAAA=",
            "Output": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAADUS6cLd6h8nGs=",
            "GasUsed": "170484",
            "Success": true,
            "Signature": {
              "Parsed": true,
              "Name": "uniswapV3Swap",
              "Signature": "uniswapV3Swap(uint256,uint256,uint256[])",
              "Abi": "{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"minReturn\",\"type\":\"uint256\"},{\"internalType\":\"uint256[]\",\"name\":\"pools\",\"type\":\"uint256[]\"}],\"name\":\"uniswapV3Swap\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"returnAmount\",\"type\":\"uint256\"}],\"stateMutability\":\"payable\",\"type\":\"function\"}",
              "SignatureHash": "5EkCLg=="
            }
          },
          "Arguments": [
            {
              "Name": "amount",
              "Value": {
                "Type": "uint256",
                "String": "1000000000000000000"
              }
            },
            {
              "Name": "minReturn",
              "Value": {
                "Type": "uint256",
                "String": "3912244908716416421661"
              }
            },
            {
              "Name": "pools",
              "Value": {
                "Type": "uint256[]",
                "Array": {
                  "Elements": [
                    {
                      "Type": "uint256",
                      "String": "86844066927987146567678238757796646856569056346800334464985562876549434348447"
                    },
                    {
                      "Type": "uint256",
                      "String": "276345522452239763537914813115977577273709459104"
                    }
                  ]
                }
              }
            }
          ],
          "ReturnValues": [
            {
              "Name": "returnAmount",
              "Value": {
                "Type": "uint256",
                "String": "3916161082108935969899"
              }
            }
          ]
        },
```
