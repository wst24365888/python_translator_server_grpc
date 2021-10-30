# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: translator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='translator.proto',
  package='translator_grpc',
  syntax='proto3',
  serialized_options=b'\n\032com.xyphuz.translator_grpcB\016TranslatorGRPCP\001\242\002\004CXTG',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10translator.proto\x12\x0ftranslator_grpc\"Q\n\x10TranslateRequest\x12\x15\n\rsourceContent\x18\x01 \x01(\t\x12\x12\n\nsourceLang\x18\x02 \x01(\t\x12\x12\n\ntargetLang\x18\x03 \x01(\t\" \n\x0eTranslateReply\x12\x0e\n\x06result\x18\x01 \x01(\t2_\n\nTranslator\x12Q\n\tTranslate\x12!.translator_grpc.TranslateRequest\x1a\x1f.translator_grpc.TranslateReply\"\x00\x42\x35\n\x1a\x63om.xyphuz.translator_grpcB\x0eTranslatorGRPCP\x01\xa2\x02\x04\x43XTGb\x06proto3'
)




_TRANSLATEREQUEST = _descriptor.Descriptor(
  name='TranslateRequest',
  full_name='translator_grpc.TranslateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sourceContent', full_name='translator_grpc.TranslateRequest.sourceContent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sourceLang', full_name='translator_grpc.TranslateRequest.sourceLang', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetLang', full_name='translator_grpc.TranslateRequest.targetLang', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=118,
)


_TRANSLATEREPLY = _descriptor.Descriptor(
  name='TranslateReply',
  full_name='translator_grpc.TranslateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='translator_grpc.TranslateReply.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=152,
)

DESCRIPTOR.message_types_by_name['TranslateRequest'] = _TRANSLATEREQUEST
DESCRIPTOR.message_types_by_name['TranslateReply'] = _TRANSLATEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TranslateRequest = _reflection.GeneratedProtocolMessageType('TranslateRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSLATEREQUEST,
  '__module__' : 'translator_pb2'
  # @@protoc_insertion_point(class_scope:translator_grpc.TranslateRequest)
  })
_sym_db.RegisterMessage(TranslateRequest)

TranslateReply = _reflection.GeneratedProtocolMessageType('TranslateReply', (_message.Message,), {
  'DESCRIPTOR' : _TRANSLATEREPLY,
  '__module__' : 'translator_pb2'
  # @@protoc_insertion_point(class_scope:translator_grpc.TranslateReply)
  })
_sym_db.RegisterMessage(TranslateReply)


DESCRIPTOR._options = None

_TRANSLATOR = _descriptor.ServiceDescriptor(
  name='Translator',
  full_name='translator_grpc.Translator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=154,
  serialized_end=249,
  methods=[
  _descriptor.MethodDescriptor(
    name='Translate',
    full_name='translator_grpc.Translator.Translate',
    index=0,
    containing_service=None,
    input_type=_TRANSLATEREQUEST,
    output_type=_TRANSLATEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSLATOR)

DESCRIPTOR.services_by_name['Translator'] = _TRANSLATOR

# @@protoc_insertion_point(module_scope)
