# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/GetVolumeMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/GetVolumeMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n)pyatv/mrp/protobuf/GetVolumeMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\"+\n\x10GetVolumeMessage\x12\x17\n\x0foutputDeviceUID\x18\x01 \x01(\t:=\n\x10getVolumeMessage\x12\x10.ProtocolMessage\x18\x35 \x01(\x0b\x32\x11.GetVolumeMessage'
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


GETVOLUMEMESSAGE_FIELD_NUMBER = 53
getVolumeMessage = _descriptor.FieldDescriptor(
  name='getVolumeMessage', full_name='getVolumeMessage', index=0,
  number=53, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_GETVOLUMEMESSAGE = _descriptor.Descriptor(
  name='GetVolumeMessage',
  full_name='GetVolumeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputDeviceUID', full_name='GetVolumeMessage.outputDeviceUID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['GetVolumeMessage'] = _GETVOLUMEMESSAGE
DESCRIPTOR.extensions_by_name['getVolumeMessage'] = getVolumeMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetVolumeMessage = _reflection.GeneratedProtocolMessageType('GetVolumeMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETVOLUMEMESSAGE,
  '__module__' : 'pyatv.mrp.protobuf.GetVolumeMessage_pb2'
  # @@protoc_insertion_point(class_scope:GetVolumeMessage)
  })
_sym_db.RegisterMessage(GetVolumeMessage)

getVolumeMessage.message_type = _GETVOLUMEMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(getVolumeMessage)

# @@protoc_insertion_point(module_scope)