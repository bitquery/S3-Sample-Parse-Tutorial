# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dex_block_message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import block_message_pb2 as block__message__pb2
import token_block_message_pb2 as token__block__message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x64\x65x_block_message.proto\x12\x0c\x65vm_messages\x1a\x13\x62lock_message.proto\x1a\x19token_block_message.proto\"\xc6\x02\n\x07\x44\x65xInfo\x12\x15\n\rSmartContract\x18\x01 \x01(\x0c\x12\x11\n\tDelegated\x18\x02 \x01(\x08\x12\x13\n\x0b\x44\x65legatedTo\x18\x03 \x01(\x0c\x12\x14\n\x0cOwnerAddress\x18\x04 \x01(\x0c\x12\x14\n\x0c\x46\x65\x65Recipient\x18\x05 \x01(\x0c\x12\x14\n\x0cProtocolName\x18\x06 \x01(\t\x12\x16\n\x0eProtocolFamily\x18\x07 \x01(\t\x12\x17\n\x0fProtocolVersion\x18\x08 \x01(\t\x12%\n\x04Pair\x18\t \x01(\x0b\x32\x17.evm_messages.TokenInfo\x12+\n\nCurrencies\x18\n \x03(\x0b\x32\x17.evm_messages.TokenInfo\x12\x35\n\x14UnderlyingCurrencies\x18\x0b \x03(\x0b\x32\x17.evm_messages.TokenInfo\"n\n\nTradeAsset\x12)\n\x08\x43urrency\x18\x01 \x01(\x0b\x32\x17.evm_messages.TokenInfo\x12\x0e\n\x06\x41mount\x18\x02 \x01(\x0c\x12\n\n\x02Id\x18\x03 \x01(\x0c\x12\x0b\n\x03URI\x18\x04 \x01(\t\x12\x0c\n\x04\x44\x61ta\x18\x05 \x01(\x0c\"e\n\tTradeSide\x12\x0e\n\x06Seller\x18\x01 \x01(\x0c\x12\r\n\x05\x42uyer\x18\x02 \x01(\x0c\x12\x0f\n\x07OrderId\x18\x03 \x01(\x0c\x12(\n\x06\x41ssets\x18\x04 \x03(\x0b\x32\x18.evm_messages.TradeAsset\"s\n\x08TradeFee\x12)\n\x08\x43urrency\x18\x01 \x01(\x0b\x32\x17.evm_messages.TokenInfo\x12\x0e\n\x06\x41mount\x18\x02 \x01(\x0c\x12\n\n\x02Id\x18\x03 \x01(\x0c\x12\r\n\x05Payer\x18\x04 \x01(\x0c\x12\x11\n\tRecipient\x18\x05 \x01(\x0c\"\x91\x02\n\x08\x44\x65xTrade\x12\x18\n\x10TransactionIndex\x18\x01 \x01(\x04\x12\x11\n\tCallIndex\x18\x02 \x01(\x04\x12\x10\n\x08LogIndex\x18\x03 \x01(\x04\x12\x0e\n\x06HasLog\x18\x04 \x01(\x08\x12\"\n\x03\x44\x65x\x18\x05 \x01(\x0b\x32\x15.evm_messages.DexInfo\x12$\n\x03\x42uy\x18\x06 \x01(\x0b\x32\x17.evm_messages.TradeSide\x12%\n\x04Sell\x18\x07 \x01(\x0b\x32\x17.evm_messages.TradeSide\x12\x0e\n\x06Sender\x18\x08 \x01(\x0c\x12\x0f\n\x07Success\x18\t \x01(\x08\x12$\n\x04\x46\x65\x65s\x18\n \x03(\x0b\x32\x16.evm_messages.TradeFee\"\x88\x01\n\x0f\x44\x65xBlockMessage\x12\"\n\x05\x43hain\x18\x01 \x01(\x0b\x32\x13.evm_messages.Chain\x12)\n\x06Header\x18\x02 \x01(\x0b\x32\x19.evm_messages.BlockHeader\x12&\n\x06Trades\x18\x05 \x03(\x0b\x32\x16.evm_messages.DexTradeBCZAgithub.com/bitquery/streaming_processor/evm/messages;evm_messagesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dex_block_message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZAgithub.com/bitquery/streaming_processor/evm/messages;evm_messages'
  _DEXINFO._serialized_start=90
  _DEXINFO._serialized_end=416
  _TRADEASSET._serialized_start=418
  _TRADEASSET._serialized_end=528
  _TRADESIDE._serialized_start=530
  _TRADESIDE._serialized_end=631
  _TRADEFEE._serialized_start=633
  _TRADEFEE._serialized_end=748
  _DEXTRADE._serialized_start=751
  _DEXTRADE._serialized_end=1024
  _DEXBLOCKMESSAGE._serialized_start=1027
  _DEXBLOCKMESSAGE._serialized_end=1163
# @@protoc_insertion_point(module_scope)
