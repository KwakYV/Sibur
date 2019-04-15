# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/sibur/device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/sibur/device.proto',
  package='protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19protos/sibur/device.proto\x12\x06protos\x1a\x1fgoogle/protobuf/timestamp.proto\"R\n\x14\x44\x65viceMessageRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12)\n\x08messages\x18\x02 \x03(\x0b\x32\x17.protos.ToDeviceMessage\"\xd6\x01\n\x11\x46romDeviceMessage\x12\x0e\n\x06\x64\x65veui\x18\x01 \x01(\x0c\x12&\n\x02ts\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66\x63ntup\x18\x03 \x01(\x05\x12\x0f\n\x07\x62\x61ttery\x18\x04 \x01(\x02\x12\x0e\n\x06period\x18\x05 \x01(\x05\x12\x1a\n\x04mode\x18\x06 \x01(\x0e\x32\x0c.protos.Mode\x12\x1c\n\x05\x65vent\x18\x07 \x01(\x0e\x32\r.protos.Event\x12\x1e\n\x04\x64\x61ta\x18\x08 \x03(\x0b\x32\x10.protos.PortData\"U\n\x08PortData\x12 \n\x04port\x18\x01 \x01(\x0e\x32\x12.protos.DevicePort\x12\r\n\x05value\x18\x02 \x01(\x05\x12\x0b\n\x03min\x18\x03 \x01(\x05\x12\x0b\n\x03max\x18\x04 \x01(\x05\"y\n\x0fToDeviceMessage\x12\x0e\n\x06period\x18\x02 \x01(\x05\x12\x0b\n\x03min\x18\x03 \x01(\x05\x12\x0b\n\x03max\x18\x04 \x01(\x05\x12\x1a\n\x04mode\x18\x05 \x01(\x0e\x32\x0c.protos.Mode\x12 \n\x04port\x18\x06 \x01(\x0e\x32\x12.protos.DevicePort*5\n\x04Mode\x12\x0c\n\x08\x42OUNDARY\x10\x00\x12\n\n\x06PERIOD\x10\x01\x12\x13\n\x0f\x42OUNDARY_PERIOD\x10\x02*-\n\x05\x45vent\x12\x12\n\x0e\x42OUNDARY_EVENT\x10\x00\x12\x10\n\x0cPERIOD_EVENT\x10\x01*R\n\nDevicePort\x12\t\n\x05VIBR1\x10\x00\x12\t\n\x05VIBR2\x10\x01\x12\n\n\x06TEMPL1\x10\x02\x12\n\n\x06TEMPL2\x10\x03\x12\n\n\x06TEMPH1\x10\x04\x12\n\n\x06TEMPH2\x10\x05\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='protos.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOUNDARY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOUNDARY_PERIOD', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=581,
  serialized_end=634,
)
_sym_db.RegisterEnumDescriptor(_MODE)

Mode = enum_type_wrapper.EnumTypeWrapper(_MODE)
_EVENT = _descriptor.EnumDescriptor(
  name='Event',
  full_name='protos.Event',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOUNDARY_EVENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_EVENT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=636,
  serialized_end=681,
)
_sym_db.RegisterEnumDescriptor(_EVENT)

Event = enum_type_wrapper.EnumTypeWrapper(_EVENT)
_DEVICEPORT = _descriptor.EnumDescriptor(
  name='DevicePort',
  full_name='protos.DevicePort',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VIBR1', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIBR2', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPL1', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPL2', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPH1', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPH2', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=683,
  serialized_end=765,
)
_sym_db.RegisterEnumDescriptor(_DEVICEPORT)

DevicePort = enum_type_wrapper.EnumTypeWrapper(_DEVICEPORT)
BOUNDARY = 0
PERIOD = 1
BOUNDARY_PERIOD = 2
BOUNDARY_EVENT = 0
PERIOD_EVENT = 1
VIBR1 = 0
VIBR2 = 1
TEMPL1 = 2
TEMPL2 = 3
TEMPH1 = 4
TEMPH2 = 5



_DEVICEMESSAGEREQUEST = _descriptor.Descriptor(
  name='DeviceMessageRequest',
  full_name='protos.DeviceMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dev_eui', full_name='protos.DeviceMessageRequest.dev_eui', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messages', full_name='protos.DeviceMessageRequest.messages', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=70,
  serialized_end=152,
)


_FROMDEVICEMESSAGE = _descriptor.Descriptor(
  name='FromDeviceMessage',
  full_name='protos.FromDeviceMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deveui', full_name='protos.FromDeviceMessage.deveui', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='protos.FromDeviceMessage.ts', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fcntup', full_name='protos.FromDeviceMessage.fcntup', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='battery', full_name='protos.FromDeviceMessage.battery', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='protos.FromDeviceMessage.period', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='protos.FromDeviceMessage.mode', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='protos.FromDeviceMessage.event', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='protos.FromDeviceMessage.data', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=155,
  serialized_end=369,
)


_PORTDATA = _descriptor.Descriptor(
  name='PortData',
  full_name='protos.PortData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='protos.PortData.port', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.PortData.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='protos.PortData.min', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='protos.PortData.max', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=371,
  serialized_end=456,
)


_TODEVICEMESSAGE = _descriptor.Descriptor(
  name='ToDeviceMessage',
  full_name='protos.ToDeviceMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='period', full_name='protos.ToDeviceMessage.period', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min', full_name='protos.ToDeviceMessage.min', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='protos.ToDeviceMessage.max', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='protos.ToDeviceMessage.mode', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='protos.ToDeviceMessage.port', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=458,
  serialized_end=579,
)

_DEVICEMESSAGEREQUEST.fields_by_name['messages'].message_type = _TODEVICEMESSAGE
_FROMDEVICEMESSAGE.fields_by_name['ts'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FROMDEVICEMESSAGE.fields_by_name['mode'].enum_type = _MODE
_FROMDEVICEMESSAGE.fields_by_name['event'].enum_type = _EVENT
_FROMDEVICEMESSAGE.fields_by_name['data'].message_type = _PORTDATA
_PORTDATA.fields_by_name['port'].enum_type = _DEVICEPORT
_TODEVICEMESSAGE.fields_by_name['mode'].enum_type = _MODE
_TODEVICEMESSAGE.fields_by_name['port'].enum_type = _DEVICEPORT
DESCRIPTOR.message_types_by_name['DeviceMessageRequest'] = _DEVICEMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['FromDeviceMessage'] = _FROMDEVICEMESSAGE
DESCRIPTOR.message_types_by_name['PortData'] = _PORTDATA
DESCRIPTOR.message_types_by_name['ToDeviceMessage'] = _TODEVICEMESSAGE
DESCRIPTOR.enum_types_by_name['Mode'] = _MODE
DESCRIPTOR.enum_types_by_name['Event'] = _EVENT
DESCRIPTOR.enum_types_by_name['DevicePort'] = _DEVICEPORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceMessageRequest = _reflection.GeneratedProtocolMessageType('DeviceMessageRequest', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEMESSAGEREQUEST,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeviceMessageRequest)
  ))
_sym_db.RegisterMessage(DeviceMessageRequest)

FromDeviceMessage = _reflection.GeneratedProtocolMessageType('FromDeviceMessage', (_message.Message,), dict(
  DESCRIPTOR = _FROMDEVICEMESSAGE,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.FromDeviceMessage)
  ))
_sym_db.RegisterMessage(FromDeviceMessage)

PortData = _reflection.GeneratedProtocolMessageType('PortData', (_message.Message,), dict(
  DESCRIPTOR = _PORTDATA,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.PortData)
  ))
_sym_db.RegisterMessage(PortData)

ToDeviceMessage = _reflection.GeneratedProtocolMessageType('ToDeviceMessage', (_message.Message,), dict(
  DESCRIPTOR = _TODEVICEMESSAGE,
  __module__ = 'protos.sibur.device_pb2'
  # @@protoc_insertion_point(class_scope:protos.ToDeviceMessage)
  ))
_sym_db.RegisterMessage(ToDeviceMessage)


# @@protoc_insertion_point(module_scope)