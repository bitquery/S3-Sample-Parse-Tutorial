import boto3
import lz4.frame
import block_message_pb2
import json
import binascii
import base64
import dex_block_message_pb2
import token_block_message_pb2
from google.protobuf.json_format import MessageToJson

s3 = boto3.client('s3', aws_access_key_id='your key id', aws_secret_access_key='your key', region_name='us-east-1')
bucket_name = 'demo-streaming-eth'
block_object_key = 'eth.blocks.s3/000016780000/000016780000_0xf127ae770b9b73af1be93e5a7ac19be5e3bac41673b2685c6b4619fb09af09f0_41452bd33251301d32c606c704120d027de580505d611e4fb1c5ff3ef51d0cb7.block.lz4'
dextrades_object_key = 'eth.dextrades.s3/000016780000/000016780000_0xf127ae770b9b73af1be93e5a7ac19be5e3bac41673b2685c6b4619fb09af09f0_0a81237e6f43853cf5ed19cd1a0e527fa6e5b08364d7113d796d9dc9c4b2e7cf.block.lz4'
token_object_key='eth.tokens.s3/000016780000/000016780000_0xf127ae770b9b73af1be93e5a7ac19be5e3bac41673b2685c6b4619fb09af09f0_7663bf0ba77528f26553fdd3650f05de063258a34861a92ea9bc3d113caccfce.block.lz4'

blocks_local_path = 'Your Path/s3downloadblocks.lz4'
dextrades_local_path = 'Your Paths/s3downloaddextrades.lz4'
token_local_path='Your Path/s3downloadtoken.lz4'

s3.download_file(bucket_name, block_object_key, blocks_local_path)

with open(blocks_local_path, 'rb') as f:
    compressed_data = f.read()

decompressed_data = lz4.frame.decompress(compressed_data)
print('here')
block_headers = block_message_pb2.BlockHeader()
block_headers.ParseFromString(decompressed_data)
print('here1')
# Write block_headers to a file
with open('block_headers.json', 'w') as f:
    json_string = MessageToJson(block_headers)
    f.write(json_string)



#### dextrades###


def decode_all_fields(dex_json_object):
    """
    Decodes all of the base64-encoded strings in a JSON object.

    Args:
        dex_json_object: The JSON object to decode.

    Returns:
        The decoded JSON object.
    """

    fields_to_skip = [
        "GasLimit",
        "GasUsed",
        "Time",
        "ProtocolName",
        "ProtocolFamily",
        "Name",
        "Symbol",
        "ProtocolVersion",
        "Config",
    ]

    fields_numerical = ["Number", "Amount", "BaseFee", "ChainId"]

    if isinstance(dex_json_object, dict):
        for key, value in dex_json_object.items():
            if isinstance(value, dict):

                dex_json_object[key] = decode_all_fields(value)
            elif isinstance(value, list):

                for i in range(len(value)):
                    value[i] = decode_all_fields(value[i])
            elif isinstance(value, str) and key not in fields_to_skip:

                decoded_value = base64.b64decode(value)
                hex_decoded_value = "0x" + \
                    binascii.hexlify(decoded_value).decode()
                
                if key in fields_numerical:
                    Int_hex_decoded_value=int(hex_decoded_value,16)
                    hex_decoded_value=Int_hex_decoded_value
                    print(Int_hex_decoded_value)
                dex_json_object[key] = hex_decoded_value

    elif isinstance(dex_json_object, list):
        for i, item in enumerate(dex_json_object):
            if isinstance(item, dict):
                dex_json_object[i] = decode_all_fields(item)

    return dex_json_object




s3.download_file(bucket_name, dextrades_object_key, dextrades_local_path)

with open(dextrades_local_path, 'rb') as f:
    dex_compressed_data = f.read()

dex_decompressed_data = lz4.frame.decompress(dex_compressed_data)
print('here3')

dextrades=dex_block_message_pb2.DexBlockMessage()

dextrades.ParseFromString(dex_decompressed_data)
dex_json_string = json.loads(MessageToJson(dextrades))

print(type(dex_json_string["Trades"][0]["Dex"]["Currencies"]))
for i in range(len(dex_json_string["Trades"])):
    dex_json_string["Trades"][i]["Dex"] = decode_all_fields(
        dex_json_string["Trades"][i]["Dex"])
    dex_json_string["Trades"][i]["Buy"] = decode_all_fields(
        dex_json_string["Trades"][i]["Buy"])
    dex_json_string["Trades"][i]["Sell"] = decode_all_fields(
        dex_json_string["Trades"][i]["Sell"])

dex_json_string["Header"] = decode_all_fields(dex_json_string["Header"])
dex_json_string["Chain"]= decode_all_fields(dex_json_string["Chain"])


with open('file_hex.json', 'w') as file:
    json.dump(dex_json_string, file, indent=4)



#########

## Token
print('here5')
s3.download_file(bucket_name, token_object_key, token_local_path)
with open(token_local_path, 'rb') as f:
    token_compressed_data = f.read()

token_decompressed_data = lz4.frame.decompress(token_compressed_data)

TokenInfo = token_block_message_pb2.TokenTransfer()
TokenInfo.ParseFromString(token_decompressed_data)
TokenBlockMessage  = token_block_message_pb2.TokenBlockMessage()
TokenBlockMessage.ParseFromString(token_decompressed_data)
print('here6')
# Write  to a file
with open('token.json', 'w') as f:
    json_string = MessageToJson(TokenInfo)
    f.write(json_string)
    json_string1=MessageToJson(TokenBlockMessage)
    f.write(json_string1)
