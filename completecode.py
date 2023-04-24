import boto3
import lz4.frame
import block_message_pb2
import json
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

s3.download_file(bucket_name, dextrades_object_key, dextrades_local_path)

with open(dextrades_local_path, 'rb') as f:
    dex_compressed_data = f.read()

dex_decompressed_data = lz4.frame.decompress(dex_compressed_data)
print('here3')
dextrades = dex_block_message_pb2.TradeAsset()
dextrades1=dex_block_message_pb2.DexInfo()
dextrades2=dex_block_message_pb2.TradeSide()
dextrades3=dex_block_message_pb2.TradeFee()
dextrades4=dex_block_message_pb2.DexTrade()
dextrades5=dex_block_message_pb2.DexBlockMessage()

dextrades.ParseFromString(dex_decompressed_data)
dextrades1.ParseFromString(dex_decompressed_data)

print('here4')
# Write  to a file
with open('dextrades.json', 'w') as f:
    dex_json_string = MessageToJson(dextrades)
    f.write(dex_json_string)
    dex_json_string1 = MessageToJson(dextrades1)
    f.write(dex_json_string1)
    dex_json_string2 = MessageToJson(dextrades2)
    f.write(dex_json_string2)
    dex_json_string3 = MessageToJson(dextrades3)
    f.write(dex_json_string3)

    dex_json_string4 = MessageToJson(dextrades4)
    f.write(dex_json_string4)
    dex_json_string5 = MessageToJson(dextrades5)
    f.write(dex_json_string5)


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

