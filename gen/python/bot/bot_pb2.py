# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: bot/bot.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'bot/bot.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbot/bot.proto\x12\x03\x62ot\"F\n\x12SendMessageRequest\x12\x0f\n\x07\x63hat_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06images\x18\x03 \x03(\t\"&\n\x13SendMessageResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32S\n\x0fTelegramService\x12@\n\x0bSendMessage\x12\x17.bot.SendMessageRequest\x1a\x18.bot.SendMessageResponseB\x0eZ\x0c\x62ot.v1;botv1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bot.bot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\014bot.v1;botv1'
  _globals['_SENDMESSAGEREQUEST']._serialized_start=22
  _globals['_SENDMESSAGEREQUEST']._serialized_end=92
  _globals['_SENDMESSAGERESPONSE']._serialized_start=94
  _globals['_SENDMESSAGERESPONSE']._serialized_end=132
  _globals['_TELEGRAMSERVICE']._serialized_start=134
  _globals['_TELEGRAMSERVICE']._serialized_end=217
# @@protoc_insertion_point(module_scope)
