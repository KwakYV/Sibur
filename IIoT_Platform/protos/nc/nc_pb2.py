# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/nc/nc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos.gw import gw_pb2 as protos_dot_gw_dot_gw__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/nc/nc.proto',
  package='nc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12protos/nc/nc.proto\x12\x02nc\x1a\x1bgoogle/protobuf/empty.proto\x1a\x12protos/gw/gw.proto\"t\n\x1bHandleUplinkMetaDataRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12!\n\x07tx_info\x18\x02 \x01(\x0b\x32\x10.gw.UplinkTXInfo\x12!\n\x07rx_info\x18\x03 \x03(\x0b\x32\x10.gw.UplinkRXInfo\"O\n\x1dHandleUplinkMACCommandRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x0b\n\x03\x63id\x18\x02 \x01(\r\x12\x10\n\x08\x63ommands\x18\x06 \x03(\x0c\x32\xc4\x01\n\x18NetworkControllerService\x12Q\n\x14HandleUplinkMetaData\x12\x1f.nc.HandleUplinkMetaDataRequest\x1a\x16.google.protobuf.Empty\"\x00\x12U\n\x16HandleUplinkMACCommand\x12!.nc.HandleUplinkMACCommandRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,protos_dot_gw_dot_gw__pb2.DESCRIPTOR,])




_HANDLEUPLINKMETADATAREQUEST = _descriptor.Descriptor(
  name='HandleUplinkMetaDataRequest',
  full_name='nc.HandleUplinkMetaDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dev_eui', full_name='nc.HandleUplinkMetaDataRequest.dev_eui', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_info', full_name='nc.HandleUplinkMetaDataRequest.tx_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rx_info', full_name='nc.HandleUplinkMetaDataRequest.rx_info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=191,
)


_HANDLEUPLINKMACCOMMANDREQUEST = _descriptor.Descriptor(
  name='HandleUplinkMACCommandRequest',
  full_name='nc.HandleUplinkMACCommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dev_eui', full_name='nc.HandleUplinkMACCommandRequest.dev_eui', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cid', full_name='nc.HandleUplinkMACCommandRequest.cid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commands', full_name='nc.HandleUplinkMACCommandRequest.commands', index=2,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=272,
)

_HANDLEUPLINKMETADATAREQUEST.fields_by_name['tx_info'].message_type = protos_dot_gw_dot_gw__pb2._UPLINKTXINFO
_HANDLEUPLINKMETADATAREQUEST.fields_by_name['rx_info'].message_type = protos_dot_gw_dot_gw__pb2._UPLINKRXINFO
DESCRIPTOR.message_types_by_name['HandleUplinkMetaDataRequest'] = _HANDLEUPLINKMETADATAREQUEST
DESCRIPTOR.message_types_by_name['HandleUplinkMACCommandRequest'] = _HANDLEUPLINKMACCOMMANDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HandleUplinkMetaDataRequest = _reflection.GeneratedProtocolMessageType('HandleUplinkMetaDataRequest', (_message.Message,), dict(
  DESCRIPTOR = _HANDLEUPLINKMETADATAREQUEST,
  __module__ = 'protos.nc.nc_pb2'
  # @@protoc_insertion_point(class_scope:nc.HandleUplinkMetaDataRequest)
  ))
_sym_db.RegisterMessage(HandleUplinkMetaDataRequest)

HandleUplinkMACCommandRequest = _reflection.GeneratedProtocolMessageType('HandleUplinkMACCommandRequest', (_message.Message,), dict(
  DESCRIPTOR = _HANDLEUPLINKMACCOMMANDREQUEST,
  __module__ = 'protos.nc.nc_pb2'
  # @@protoc_insertion_point(class_scope:nc.HandleUplinkMACCommandRequest)
  ))
_sym_db.RegisterMessage(HandleUplinkMACCommandRequest)



_NETWORKCONTROLLERSERVICE = _descriptor.ServiceDescriptor(
  name='NetworkControllerService',
  full_name='nc.NetworkControllerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=275,
  serialized_end=471,
  methods=[
  _descriptor.MethodDescriptor(
    name='HandleUplinkMetaData',
    full_name='nc.NetworkControllerService.HandleUplinkMetaData',
    index=0,
    containing_service=None,
    input_type=_HANDLEUPLINKMETADATAREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HandleUplinkMACCommand',
    full_name='nc.NetworkControllerService.HandleUplinkMACCommand',
    index=1,
    containing_service=None,
    input_type=_HANDLEUPLINKMACCOMMANDREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NETWORKCONTROLLERSERVICE)

DESCRIPTOR.services_by_name['NetworkControllerService'] = _NETWORKCONTROLLERSERVICE

# @@protoc_insertion_point(module_scope)
