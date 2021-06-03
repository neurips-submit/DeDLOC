# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: runtime.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='runtime.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rruntime.proto\"\x18\n\tExpertUID\x12\x0b\n\x03uid\x18\x01 \x01(\t\"%\n\nExpertInfo\x12\x17\n\x0fserialized_info\x18\x01 \x01(\x0c\"6\n\rExpertRequest\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x18\n\x07tensors\x18\x02 \x03(\x0b\x32\x07.Tensor\"*\n\x0e\x45xpertResponse\x12\x18\n\x07tensors\x18\x02 \x03(\x0b\x32\x07.Tensor\"\x83\x01\n\x06Tensor\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\x12\x0c\n\x04size\x18\x02 \x03(\r\x12\x15\n\rrequires_grad\x18\x03 \x01(\x08\x12\r\n\x05\x64type\x18\x04 \x01(\t\x12%\n\x0b\x63ompression\x18\x05 \x01(\x0e\x32\x10.CompressionType\x12\x0e\n\x06\x63hunks\x18\x06 \x01(\x05*`\n\x0f\x43ompressionType\x12\x08\n\x04NONE\x10\x00\x12\x11\n\rMEANSTD_16BIT\x10\x01\x12\x0b\n\x07\x46LOAT16\x10\x02\x12\x11\n\rQUANTILE_8BIT\x10\x03\x12\x10\n\x0cUNIFORM_8BIT\x10\x04\x32\x8d\x01\n\x11\x43onnectionHandler\x12\x1f\n\x04info\x12\n.ExpertUID\x1a\x0b.ExpertInfo\x12*\n\x07\x66orward\x12\x0e.ExpertRequest\x1a\x0f.ExpertResponse\x12+\n\x08\x62\x61\x63kward\x12\x0e.ExpertRequest\x1a\x0f.ExpertResponseb\x06proto3'
)

_COMPRESSIONTYPE = _descriptor.EnumDescriptor(
  name='CompressionType',
  full_name='CompressionType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MEANSTD_16BIT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOAT16', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUANTILE_8BIT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNIFORM_8BIT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=316,
  serialized_end=412,
)
_sym_db.RegisterEnumDescriptor(_COMPRESSIONTYPE)

CompressionType = enum_type_wrapper.EnumTypeWrapper(_COMPRESSIONTYPE)
NONE = 0
MEANSTD_16BIT = 1
FLOAT16 = 2
QUANTILE_8BIT = 3
UNIFORM_8BIT = 4



_EXPERTUID = _descriptor.Descriptor(
  name='ExpertUID',
  full_name='ExpertUID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='ExpertUID.uid', index=0,
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
  serialized_start=17,
  serialized_end=41,
)


_EXPERTINFO = _descriptor.Descriptor(
  name='ExpertInfo',
  full_name='ExpertInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialized_info', full_name='ExpertInfo.serialized_info', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=43,
  serialized_end=80,
)


_EXPERTREQUEST = _descriptor.Descriptor(
  name='ExpertRequest',
  full_name='ExpertRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='ExpertRequest.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tensors', full_name='ExpertRequest.tensors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=82,
  serialized_end=136,
)


_EXPERTRESPONSE = _descriptor.Descriptor(
  name='ExpertResponse',
  full_name='ExpertResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensors', full_name='ExpertResponse.tensors', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=138,
  serialized_end=180,
)


_TENSOR = _descriptor.Descriptor(
  name='Tensor',
  full_name='Tensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffer', full_name='Tensor.buffer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='Tensor.size', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requires_grad', full_name='Tensor.requires_grad', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='Tensor.dtype', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compression', full_name='Tensor.compression', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='Tensor.chunks', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=183,
  serialized_end=314,
)

_EXPERTREQUEST.fields_by_name['tensors'].message_type = _TENSOR
_EXPERTRESPONSE.fields_by_name['tensors'].message_type = _TENSOR
_TENSOR.fields_by_name['compression'].enum_type = _COMPRESSIONTYPE
DESCRIPTOR.message_types_by_name['ExpertUID'] = _EXPERTUID
DESCRIPTOR.message_types_by_name['ExpertInfo'] = _EXPERTINFO
DESCRIPTOR.message_types_by_name['ExpertRequest'] = _EXPERTREQUEST
DESCRIPTOR.message_types_by_name['ExpertResponse'] = _EXPERTRESPONSE
DESCRIPTOR.message_types_by_name['Tensor'] = _TENSOR
DESCRIPTOR.enum_types_by_name['CompressionType'] = _COMPRESSIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExpertUID = _reflection.GeneratedProtocolMessageType('ExpertUID', (_message.Message,), {
  'DESCRIPTOR' : _EXPERTUID,
  '__module__' : 'runtime_pb2'
  # @@protoc_insertion_point(class_scope:ExpertUID)
  })
_sym_db.RegisterMessage(ExpertUID)

ExpertInfo = _reflection.GeneratedProtocolMessageType('ExpertInfo', (_message.Message,), {
  'DESCRIPTOR' : _EXPERTINFO,
  '__module__' : 'runtime_pb2'
  # @@protoc_insertion_point(class_scope:ExpertInfo)
  })
_sym_db.RegisterMessage(ExpertInfo)

ExpertRequest = _reflection.GeneratedProtocolMessageType('ExpertRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPERTREQUEST,
  '__module__' : 'runtime_pb2'
  # @@protoc_insertion_point(class_scope:ExpertRequest)
  })
_sym_db.RegisterMessage(ExpertRequest)

ExpertResponse = _reflection.GeneratedProtocolMessageType('ExpertResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPERTRESPONSE,
  '__module__' : 'runtime_pb2'
  # @@protoc_insertion_point(class_scope:ExpertResponse)
  })
_sym_db.RegisterMessage(ExpertResponse)

Tensor = _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), {
  'DESCRIPTOR' : _TENSOR,
  '__module__' : 'runtime_pb2'
  # @@protoc_insertion_point(class_scope:Tensor)
  })
_sym_db.RegisterMessage(Tensor)



_CONNECTIONHANDLER = _descriptor.ServiceDescriptor(
  name='ConnectionHandler',
  full_name='ConnectionHandler',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=415,
  serialized_end=556,
  methods=[
  _descriptor.MethodDescriptor(
    name='info',
    full_name='ConnectionHandler.info',
    index=0,
    containing_service=None,
    input_type=_EXPERTUID,
    output_type=_EXPERTINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='forward',
    full_name='ConnectionHandler.forward',
    index=1,
    containing_service=None,
    input_type=_EXPERTREQUEST,
    output_type=_EXPERTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='backward',
    full_name='ConnectionHandler.backward',
    index=2,
    containing_service=None,
    input_type=_EXPERTREQUEST,
    output_type=_EXPERTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONNECTIONHANDLER)

DESCRIPTOR.services_by_name['ConnectionHandler'] = _CONNECTIONHANDLER

# @@protoc_insertion_point(module_scope)