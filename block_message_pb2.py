# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: block_message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x62lock_message.proto\x12\x0c\x65vm_messages\";\n\x0b\x41\x64\x64ressCode\x12\x0c\n\x04Hash\x18\x01 \x01(\x0c\x12\x0c\n\x04Size\x18\x02 \x01(\x05\x12\x10\n\x08Suicided\x18\x03 \x01(\x08\"\xad\x02\n\x0b\x42lockHeader\x12\x0c\n\x04Hash\x18\x01 \x01(\x0c\x12\x12\n\nParentHash\x18\x02 \x01(\x0c\x12\x11\n\tUncleHash\x18\x03 \x01(\x0c\x12\x0c\n\x04Root\x18\x04 \x01(\x0c\x12\x0e\n\x06TxHash\x18\x05 \x01(\x0c\x12\x13\n\x0bReceiptHash\x18\x06 \x01(\x0c\x12\x11\n\tMixDigest\x18\x07 \x01(\x0c\x12\x10\n\x08\x43oinbase\x18\x08 \x01(\x0c\x12\r\n\x05\x42loom\x18\t \x01(\x0c\x12\r\n\x05\x45xtra\x18\n \x01(\x0c\x12\r\n\x05Nonce\x18\x0b \x01(\x04\x12\x12\n\nDifficulty\x18\x0c \x01(\x0c\x12\x0e\n\x06Number\x18\r \x01(\x0c\x12\x10\n\x08GasLimit\x18\x0e \x01(\x04\x12\x0f\n\x07GasUsed\x18\x0f \x01(\x04\x12\x0c\n\x04Time\x18\x10 \x01(\x04\x12\x0f\n\x07\x42\x61seFee\x18\x11 \x01(\x0c\"*\n\x0b\x42lockResult\x12\x0b\n\x03Gas\x18\x01 \x01(\x04\x12\x0e\n\x06\x45rrors\x18\x02 \x01(\t\",\n\tSignature\x12\t\n\x01R\x18\x01 \x01(\x0c\x12\t\n\x01V\x18\x02 \x01(\x0c\x12\t\n\x01S\x18\x03 \x01(\x0c\"$\n\x05Topic\x12\r\n\x05Index\x18\x01 \x01(\x04\x12\x0c\n\x04Hash\x18\x02 \x01(\x0c\"z\n\tLogHeader\x12\r\n\x05Index\x18\x01 \x01(\x04\x12\x0f\n\x07\x41\x64\x64ress\x18\x02 \x01(\x0c\x12\x0c\n\x04\x44\x61ta\x18\x03 \x01(\x0c\x12\x0f\n\x07Removed\x18\x04 \x01(\x08\x12.\n\x0b\x41\x64\x64ressCode\x18\x05 \x01(\x0b\x32\x19.evm_messages.AddressCode\"V\n\x03Log\x12*\n\tLogHeader\x18\x01 \x01(\x0b\x32\x17.evm_messages.LogHeader\x12#\n\x06Topics\x18\x02 \x03(\x0b\x32\x13.evm_messages.Topic\"9\n\x05Store\x12\x0f\n\x07\x41\x64\x64ress\x18\x01 \x01(\x0c\x12\x10\n\x08Location\x18\x02 \x01(\x0c\x12\r\n\x05Value\x18\x03 \x01(\x0c\"\xcc\x01\n\rReceiptHeader\x12\r\n\x05\x42loom\x18\x01 \x01(\x0c\x12\x0f\n\x07GasUsed\x18\x02 \x01(\x04\x12\x0c\n\x04Type\x18\x03 \x01(\r\x12\x17\n\x0f\x43ontractAddress\x18\x04 \x01(\x0c\x12\x19\n\x11\x43umulativeGasUsed\x18\x05 \x01(\x04\x12\x11\n\tPostState\x18\x06 \x01(\x0c\x12\x0e\n\x06Status\x18\x07 \x01(\x04\x12\x36\n\x13\x43ontractAddressCode\x18\x08 \x01(\x0b\x32\x19.evm_messages.AddressCode\"^\n\x07Receipt\x12\x32\n\rReceiptHeader\x18\x01 \x01(\x0b\x32\x1b.evm_messages.ReceiptHeader\x12\x1f\n\x04Logs\x18\x02 \x03(\x0b\x32\x11.evm_messages.Log\"$\n\x06Opcode\x12\x0c\n\x04\x43ode\x18\x01 \x01(\r\x12\x0c\n\x04Name\x18\x02 \x01(\t\"\x8e\x01\n\x0c\x43\x61ptureStart\x12\x0c\n\x04\x46rom\x18\x01 \x01(\x0c\x12\n\n\x02To\x18\x02 \x01(\x0c\x12\x0e\n\x06\x43reate\x18\x03 \x01(\x08\x12\r\n\x05Input\x18\x04 \x01(\x0c\x12\x0b\n\x03Gas\x18\x05 \x01(\x04\x12\r\n\x05Value\x18\x06 \x01(\x0c\x12)\n\x06ToCode\x18\x07 \x01(\x0b\x32\x19.evm_messages.AddressCode\"<\n\nCaptureEnd\x12\x0e\n\x06Output\x18\x01 \x01(\x0c\x12\x0f\n\x07GasUsed\x18\x02 \x01(\x04\x12\r\n\x05\x45rror\x18\x03 \x01(\t\"r\n\x08\x43ontract\x12\x15\n\rCallerAddress\x18\x01 \x01(\x0c\x12\x0e\n\x06\x43\x61ller\x18\x02 \x01(\x0c\x12\x0f\n\x07\x41\x64\x64ress\x18\x03 \x01(\x0c\x12\x10\n\x08\x43odeAddr\x18\x04 \x01(\x0c\x12\r\n\x05Input\x18\x05 \x01(\x0c\x12\r\n\x05Value\x18\x06 \x01(\x0c\"\xc2\x01\n\x0c\x43\x61ptureFault\x12\n\n\x02Pc\x18\x01 \x01(\x04\x12$\n\x06Opcode\x18\x02 \x01(\x0b\x32\x14.evm_messages.Opcode\x12\x0b\n\x03Gas\x18\x03 \x01(\x04\x12\x0c\n\x04\x43ost\x18\x04 \x01(\x04\x12\x0e\n\x06Memory\x18\x05 \x01(\x0c\x12\r\n\x05\x44\x65pth\x18\x06 \x01(\x04\x12\r\n\x05Stack\x18\x07 \x03(\x0c\x12(\n\x08\x43ontract\x18\x08 \x01(\x0b\x32\x16.evm_messages.Contract\x12\r\n\x05\x45rror\x18\t \x01(\t\"\xa4\x01\n\x0c\x43\x61ptureEnter\x12$\n\x06Opcode\x18\x01 \x01(\x0b\x32\x14.evm_messages.Opcode\x12\x0c\n\x04\x46rom\x18\x02 \x01(\x0c\x12\n\n\x02To\x18\x03 \x01(\x0c\x12\r\n\x05Input\x18\x04 \x01(\x0c\x12\x0b\n\x03Gas\x18\x05 \x01(\x04\x12\r\n\x05Value\x18\x06 \x01(\x0c\x12)\n\x06ToCode\x18\x07 \x01(\x0b\x32\x19.evm_messages.AddressCode\"=\n\x0b\x43\x61ptureExit\x12\x0e\n\x06Output\x18\x01 \x01(\x0c\x12\x0f\n\x07GasUsed\x18\x02 \x01(\x04\x12\r\n\x05\x45rror\x18\x03 \x01(\t\"\xb5\x01\n\x12\x43\x61ptureStateHeader\x12\x12\n\nEnterIndex\x18\x01 \x01(\r\x12\x11\n\tExitIndex\x18\x02 \x01(\r\x12\n\n\x02Pc\x18\x03 \x01(\x04\x12$\n\x06Opcode\x18\x04 \x01(\x0b\x32\x14.evm_messages.Opcode\x12\x0b\n\x03Gas\x18\x05 \x01(\x04\x12\x0c\n\x04\x43ost\x18\x06 \x01(\x04\x12\r\n\x05RData\x18\x07 \x01(\x0c\x12\r\n\x05\x44\x65pth\x18\x08 \x01(\x04\x12\r\n\x05\x45rror\x18\t \x01(\t\"\x90\x01\n\x0c\x43\x61ptureState\x12<\n\x12\x43\x61ptureStateHeader\x18\x01 \x01(\x0b\x32 .evm_messages.CaptureStateHeader\x12\x1e\n\x03Log\x18\x02 \x01(\x0b\x32\x11.evm_messages.Log\x12\"\n\x05Store\x18\x03 \x01(\x0b\x32\x13.evm_messages.Store\"\xf5\x01\n\x04\x43\x61ll\x12\r\n\x05Index\x18\x01 \x01(\r\x12\r\n\x05\x44\x65pth\x18\x02 \x01(\r\x12\x12\n\nEnterIndex\x18\x03 \x01(\r\x12\x11\n\tExitIndex\x18\x04 \x01(\r\x12\x13\n\x0b\x43\x61llerIndex\x18\x05 \x01(\x05\x12\x30\n\x0c\x43\x61ptureEnter\x18\x06 \x01(\x0b\x32\x1a.evm_messages.CaptureEnter\x12.\n\x0b\x43\x61ptureExit\x18\x07 \x01(\x0b\x32\x19.evm_messages.CaptureExit\x12\x31\n\rCaptureStates\x18\x08 \x03(\x0b\x32\x1a.evm_messages.CaptureState\"\xef\x01\n\x05Trace\x12!\n\x05\x43\x61lls\x18\x01 \x03(\x0b\x32\x12.evm_messages.Call\x12\x30\n\x0c\x43\x61ptureStart\x18\x02 \x01(\x0b\x32\x1a.evm_messages.CaptureStart\x12,\n\nCaptureEnd\x18\x03 \x01(\x0b\x32\x18.evm_messages.CaptureEnd\x12\x30\n\x0c\x43\x61ptureFault\x18\x04 \x01(\x0b\x32\x1a.evm_messages.CaptureFault\x12\x31\n\rCaptureStates\x18\x05 \x03(\x0b\x32\x1a.evm_messages.CaptureState\"3\n\x0b\x41\x63\x63\x65ssTuple\x12\x0f\n\x07\x41\x64\x64ress\x18\x01 \x01(\x0c\x12\x13\n\x0bStorageKeys\x18\x02 \x03(\x0c\"\xd5\x02\n\x11TransactionHeader\x12\r\n\x05Index\x18\x01 \x01(\x04\x12\x0c\n\x04Hash\x18\x02 \x01(\x0c\x12\x0b\n\x03Gas\x18\x03 \x01(\x04\x12\r\n\x05Value\x18\x04 \x01(\x0c\x12\x0c\n\x04\x44\x61ta\x18\x05 \x01(\x0c\x12\r\n\x05Nonce\x18\x06 \x01(\x04\x12\x0f\n\x07\x43hainId\x18\x07 \x01(\x0c\x12\x0c\n\x04\x43ost\x18\x08 \x01(\x0c\x12\x11\n\tGasFeeCap\x18\t \x01(\x0c\x12\x10\n\x08GasPrice\x18\n \x01(\x0c\x12\x11\n\tGasTipCap\x18\x0b \x01(\x0c\x12\x11\n\tProtected\x18\x0c \x01(\x08\x12\x0c\n\x04Type\x18\r \x01(\r\x12\n\n\x02To\x18\x0e \x01(\x0c\x12\x0c\n\x04\x46rom\x18\x0f \x01(\x0c\x12)\n\x06ToCode\x18\x10 \x01(\x0b\x32\x19.evm_messages.AddressCode\x12-\n\nAccessList\x18\x11 \x03(\x0b\x32\x19.evm_messages.AccessTuple\"\xcf\x01\n\x0bTransaction\x12:\n\x11TransactionHeader\x18\x01 \x01(\x0b\x32\x1f.evm_messages.TransactionHeader\x12*\n\tSignature\x18\x02 \x01(\x0b\x32\x17.evm_messages.Signature\x12&\n\x07Receipt\x18\x03 \x01(\x0b\x32\x15.evm_messages.Receipt\x12\"\n\x05Trace\x18\x04 \x01(\x0b\x32\x13.evm_messages.Trace\x12\x0c\n\x04Time\x18\x05 \x01(\x04\"(\n\x05\x43hain\x12\x0f\n\x07\x43hainId\x18\x01 \x01(\x0c\x12\x0e\n\x06\x43onfig\x18\x02 \x01(\t\"\xe4\x01\n\x0c\x42lockMessage\x12\"\n\x05\x43hain\x18\x01 \x01(\x0b\x32\x13.evm_messages.Chain\x12)\n\x06Header\x18\x02 \x01(\x0b\x32\x19.evm_messages.BlockHeader\x12)\n\x06Result\x18\x03 \x01(\x0b\x32\x19.evm_messages.BlockResult\x12)\n\x06Uncles\x18\x04 \x03(\x0b\x32\x19.evm_messages.BlockHeader\x12/\n\x0cTransactions\x18\x05 \x03(\x0b\x32\x19.evm_messages.TransactionBCZAgithub.com/bitquery/streaming_processor/evm/messages;evm_messagesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'block_message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZAgithub.com/bitquery/streaming_processor/evm/messages;evm_messages'
  _ADDRESSCODE._serialized_start=37
  _ADDRESSCODE._serialized_end=96
  _BLOCKHEADER._serialized_start=99
  _BLOCKHEADER._serialized_end=400
  _BLOCKRESULT._serialized_start=402
  _BLOCKRESULT._serialized_end=444
  _SIGNATURE._serialized_start=446
  _SIGNATURE._serialized_end=490
  _TOPIC._serialized_start=492
  _TOPIC._serialized_end=528
  _LOGHEADER._serialized_start=530
  _LOGHEADER._serialized_end=652
  _LOG._serialized_start=654
  _LOG._serialized_end=740
  _STORE._serialized_start=742
  _STORE._serialized_end=799
  _RECEIPTHEADER._serialized_start=802
  _RECEIPTHEADER._serialized_end=1006
  _RECEIPT._serialized_start=1008
  _RECEIPT._serialized_end=1102
  _OPCODE._serialized_start=1104
  _OPCODE._serialized_end=1140
  _CAPTURESTART._serialized_start=1143
  _CAPTURESTART._serialized_end=1285
  _CAPTUREEND._serialized_start=1287
  _CAPTUREEND._serialized_end=1347
  _CONTRACT._serialized_start=1349
  _CONTRACT._serialized_end=1463
  _CAPTUREFAULT._serialized_start=1466
  _CAPTUREFAULT._serialized_end=1660
  _CAPTUREENTER._serialized_start=1663
  _CAPTUREENTER._serialized_end=1827
  _CAPTUREEXIT._serialized_start=1829
  _CAPTUREEXIT._serialized_end=1890
  _CAPTURESTATEHEADER._serialized_start=1893
  _CAPTURESTATEHEADER._serialized_end=2074
  _CAPTURESTATE._serialized_start=2077
  _CAPTURESTATE._serialized_end=2221
  _CALL._serialized_start=2224
  _CALL._serialized_end=2469
  _TRACE._serialized_start=2472
  _TRACE._serialized_end=2711
  _ACCESSTUPLE._serialized_start=2713
  _ACCESSTUPLE._serialized_end=2764
  _TRANSACTIONHEADER._serialized_start=2767
  _TRANSACTIONHEADER._serialized_end=3108
  _TRANSACTION._serialized_start=3111
  _TRANSACTION._serialized_end=3318
  _CHAIN._serialized_start=3320
  _CHAIN._serialized_end=3360
  _BLOCKMESSAGE._serialized_start=3363
  _BLOCKMESSAGE._serialized_end=3591
# @@protoc_insertion_point(module_scope)
