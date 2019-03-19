# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iiot.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='iiot.proto',
  package='protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\niiot.proto\x12\x06protos\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb5\x01\n\x08Response\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x31\n\ndevicelist\x18\x02 \x01(\x0b\x32\x1d.protos.ClientDevicesResponse\x12.\n\ndevicedata\x18\x03 \x01(\x0b\x32\x1a.protos.DeviceDataResponse\x12\x38\n\rdevicehistory\x18\x04 \x01(\x0b\x32!.protos.DeviceDataHistoryResponse\"\x7f\n\x07Request\x12\x0c\n\x04type\x18\x01 \x01(\t\x12-\n\ndevicedata\x18\x02 \x01(\x0b\x32\x19.protos.DeviceDataRequest\x12\x37\n\rdevicehistory\x18\x03 \x01(\x0b\x32 .protos.DeviceDataHistoryRequest\"\'\n\x11\x44\x65viceDataRequest\x12\x12\n\ndevEuiList\x18\x01 \x03(\t\"5\n\x12\x44\x65viceDataResponse\x12\x1f\n\x07sensors\x18\x01 \x03(\x0b\x32\x0e.protos.Sensor\"V\n\x18\x44\x65viceDataHistoryRequest\x12\x12\n\ndevEuiList\x18\x01 \x03(\t\x12&\n\x02ts\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"<\n\x19\x44\x65viceDataHistoryResponse\x12\x1f\n\x07sensors\x18\x01 \x03(\x0b\x32\x0e.protos.Sensor\"8\n\x15\x43lientDevicesResponse\x12\x1f\n\x07sensors\x18\x01 \x03(\x0b\x32\x0e.protos.Sensor\"\x9d\x01\n\x06Sensor\x12\x0e\n\x06\x64\x65vEui\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x13\n\x0btemperature\x18\x03 \x01(\x01\x12\x0f\n\x07\x62\x61ttery\x18\x04 \x01(\x01\x12&\n\x02ts\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12 \n\x07history\x18\x06 \x03(\x0b\x32\x0f.protos.History\"@\n\x07History\x12&\n\x02ts\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05value\x18\x02 \x01(\x01\x32\x38\n\x03Iot\x12\x31\n\nGetDevices\x12\x0f.protos.Request\x1a\x10.protos.Response\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='protos.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.Response.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devicelist', full_name='protos.Response.devicelist', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devicedata', full_name='protos.Response.devicedata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devicehistory', full_name='protos.Response.devicehistory', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=56,
  serialized_end=237,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='protos.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.Request.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devicedata', full_name='protos.Request.devicedata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devicehistory', full_name='protos.Request.devicehistory', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=239,
  serialized_end=366,
)


_DEVICEDATAREQUEST = _descriptor.Descriptor(
  name='DeviceDataRequest',
  full_name='protos.DeviceDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='devEuiList', full_name='protos.DeviceDataRequest.devEuiList', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=368,
  serialized_end=407,
)


_DEVICEDATARESPONSE = _descriptor.Descriptor(
  name='DeviceDataResponse',
  full_name='protos.DeviceDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensors', full_name='protos.DeviceDataResponse.sensors', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=409,
  serialized_end=462,
)


_DEVICEDATAHISTORYREQUEST = _descriptor.Descriptor(
  name='DeviceDataHistoryRequest',
  full_name='protos.DeviceDataHistoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='devEuiList', full_name='protos.DeviceDataHistoryRequest.devEuiList', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='protos.DeviceDataHistoryRequest.ts', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=464,
  serialized_end=550,
)


_DEVICEDATAHISTORYRESPONSE = _descriptor.Descriptor(
  name='DeviceDataHistoryResponse',
  full_name='protos.DeviceDataHistoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensors', full_name='protos.DeviceDataHistoryResponse.sensors', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=552,
  serialized_end=612,
)


_CLIENTDEVICESRESPONSE = _descriptor.Descriptor(
  name='ClientDevicesResponse',
  full_name='protos.ClientDevicesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensors', full_name='protos.ClientDevicesResponse.sensors', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=614,
  serialized_end=670,
)


_SENSOR = _descriptor.Descriptor(
  name='Sensor',
  full_name='protos.Sensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='devEui', full_name='protos.Sensor.devEui', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='protos.Sensor.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='protos.Sensor.temperature', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='battery', full_name='protos.Sensor.battery', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='protos.Sensor.ts', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='history', full_name='protos.Sensor.history', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=673,
  serialized_end=830,
)


_HISTORY = _descriptor.Descriptor(
  name='History',
  full_name='protos.History',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ts', full_name='protos.History.ts', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.History.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=832,
  serialized_end=896,
)

_RESPONSE.fields_by_name['devicelist'].message_type = _CLIENTDEVICESRESPONSE
_RESPONSE.fields_by_name['devicedata'].message_type = _DEVICEDATARESPONSE
_RESPONSE.fields_by_name['devicehistory'].message_type = _DEVICEDATAHISTORYRESPONSE
_REQUEST.fields_by_name['devicedata'].message_type = _DEVICEDATAREQUEST
_REQUEST.fields_by_name['devicehistory'].message_type = _DEVICEDATAHISTORYREQUEST
_DEVICEDATARESPONSE.fields_by_name['sensors'].message_type = _SENSOR
_DEVICEDATAHISTORYREQUEST.fields_by_name['ts'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEVICEDATAHISTORYRESPONSE.fields_by_name['sensors'].message_type = _SENSOR
_CLIENTDEVICESRESPONSE.fields_by_name['sensors'].message_type = _SENSOR
_SENSOR.fields_by_name['ts'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SENSOR.fields_by_name['history'].message_type = _HISTORY
_HISTORY.fields_by_name['ts'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['DeviceDataRequest'] = _DEVICEDATAREQUEST
DESCRIPTOR.message_types_by_name['DeviceDataResponse'] = _DEVICEDATARESPONSE
DESCRIPTOR.message_types_by_name['DeviceDataHistoryRequest'] = _DEVICEDATAHISTORYREQUEST
DESCRIPTOR.message_types_by_name['DeviceDataHistoryResponse'] = _DEVICEDATAHISTORYRESPONSE
DESCRIPTOR.message_types_by_name['ClientDevicesResponse'] = _CLIENTDEVICESRESPONSE
DESCRIPTOR.message_types_by_name['Sensor'] = _SENSOR
DESCRIPTOR.message_types_by_name['History'] = _HISTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'iiot_pb2'
  # @@protoc_insertion_point(class_scope:protos.Response)
  ))
_sym_db.RegisterMessage(Response)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'iiot_pb2'
  # @@protoc_insertion_point(class_scope:protos.Request)
  ))
_sym_db.RegisterMessage(Request)

DeviceDataRequest = _reflection.GeneratedProtocolMessageType('DeviceDataRequest', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEDATAREQUEST,
  __module__ = 'iiot_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeviceDataRequest)
  ))
_sym_db.RegisterMessage(DeviceDataRequest)

DeviceDataResponse = _reflection.GeneratedProtocolMessageType('DeviceDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEDATARESPONSE,
  __module__ = 'iiot_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeviceDataResponse)
  ))
_sym_db.RegisterMessage(DeviceDataResponse)

DeviceDataHistoryRequest = _reflection.GeneratedProtocolMessageType('DeviceDataHistoryRequest', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEDATAHISTORYREQUEST,
  __module__ = 'iiot_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeviceDataHistoryRequest)
  ))
_sym_db.RegisterMessage(DeviceDataHistoryRequest)

DeviceDataHistoryResponse = _reflection.GeneratedProtocolMessageType('DeviceDataHistoryResponse', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEDATAHISTORYRESPONSE,
  __module__ = 'iiot_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeviceDataHistoryResponse)
  ))
_sym_db.RegisterMessage(DeviceDataHistoryResponse)

ClientDevicesResponse = _reflection.GeneratedProtocolMessageType('ClientDevicesResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTDEVICESRESPONSE,
  __module__ = 'iiot_pb2'
  # @@protoc_insertion_point(class_scope:protos.ClientDevicesResponse)
  ))
_sym_db.RegisterMessage(ClientDevicesResponse)

Sensor = _reflection.GeneratedProtocolMessageType('Sensor', (_message.Message,), dict(
  DESCRIPTOR = _SENSOR,
  __module__ = 'iiot_pb2'
  # @@protoc_insertion_point(class_scope:protos.Sensor)
  ))
_sym_db.RegisterMessage(Sensor)

History = _reflection.GeneratedProtocolMessageType('History', (_message.Message,), dict(
  DESCRIPTOR = _HISTORY,
  __module__ = 'iiot_pb2'
  # @@protoc_insertion_point(class_scope:protos.History)
  ))
_sym_db.RegisterMessage(History)



_IOT = _descriptor.ServiceDescriptor(
  name='Iot',
  full_name='protos.Iot',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=898,
  serialized_end=954,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetDevices',
    full_name='protos.Iot.GetDevices',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IOT)

DESCRIPTOR.services_by_name['Iot'] = _IOT

# @@protoc_insertion_point(module_scope)
