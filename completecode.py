import boto3
import lz4.frame
import block_message_pb2
import json
import dex_block_message_pb2
from google.protobuf.json_format import MessageToJson

s3 = boto3.client('s3', aws_access_key_id='YOUR ID', aws_secret_access_key='YOUR KEY', region_name='us-east-1')
bucket_name = 'demo-streaming-eth'
block_object_key = 'eth.blocks.s3/000016780000/000016780000_0xf127ae770b9b73af1be93e5a7ac19be5e3bac41673b2685c6b4619fb09af09f0_41452bd33251301d32c606c704120d027de580505d611e4fb1c5ff3ef51d0cb7.block.lz4'
dextrades_object_key = 'eth.blocks.s3/000016780000/000016780000_0xf127ae770b9b73af1be93e5a7ac19be5e3bac41673b2685c6b4619fb09af09f0_41452bd33251301d32c606c704120d027de580505d611e4fb1c5ff3ef51d0cb7.dextrades.lz4'

blocks_local_path = 'YOUR PATH/s3downloadblocks.lz4'
dextrades_local_path = 'YOUR PATH/s3downloaddextrades.lz4'

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
dextrades = dex_block_message_pb2.DexInfo()
dextrades.ParseFromString(dex_decompressed_data)
print('here4')
# Write  to a file
with open('dextrades.json', 'w') as f:
    dex_json_string = MessageToJson(dextrades)
    f.write(dex_json_string)



