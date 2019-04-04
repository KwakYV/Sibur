# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/as/internal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import importlib
protos_dot_as_dot_annotations__pb2 = importlib.import_module('protos.as.annotations_pb2')
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import importlib
protos_dot_as_dot_user__pb2 = importlib.import_module('protos.as.user_pb2')


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/as/internal.proto',
  package='api',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18protos/as/internal.proto\x12\x03\x61pi\x1a\x1bprotos/as/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x14protos/as/user.proto\"8\n\x0fProfileSettings\x12%\n\x1d\x64isable_assign_existing_users\x18\x01 \x01(\x08\"\xc8\x01\n\x10OrganizationLink\x12\'\n\x0forganization_id\x18\x01 \x01(\x03R\x0eorganizationID\x12\x19\n\x11organization_name\x18\x02 \x01(\t\x12\x10\n\x08is_admin\x18\x03 \x01(\x08\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1c\n\rLoginResponse\x12\x0b\n\x03jwt\x18\x01 \x01(\t\"\x80\x01\n\x0fProfileResponse\x12\x17\n\x04user\x18\x01 \x01(\x0b\x32\t.api.User\x12,\n\rorganizations\x18\x03 \x03(\x0b\x32\x15.api.OrganizationLink\x12&\n\x08settings\x18\x04 \x01(\x0b\x32\x14.api.ProfileSettings\"D\n\x13GlobalSearchRequest\x12\x0e\n\x06search\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\"?\n\x14GlobalSearchResponse\x12\'\n\x06result\x18\x01 \x03(\x0b\x32\x17.api.GlobalSearchResult\"\xa8\x02\n\x12GlobalSearchResult\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x12\'\n\x0forganization_id\x18\x03 \x01(\x03R\x0eorganizationID\x12\x19\n\x11organization_name\x18\x04 \x01(\t\x12%\n\x0e\x61pplication_id\x18\x05 \x01(\x03R\rapplicationID\x12\x18\n\x10\x61pplication_name\x18\x06 \x01(\t\x12$\n\x0e\x64\x65vice_dev_eui\x18\x07 \x01(\tR\x0c\x64\x65viceDevEUI\x12\x13\n\x0b\x64\x65vice_name\x18\x08 \x01(\t\x12\x1f\n\x0bgateway_mac\x18\t \x01(\tR\ngatewayMAC\x12\x14\n\x0cgateway_name\x18\n \x01(\t\"F\n\x10\x42randingResponse\x12\x0c\n\x04logo\x18\x01 \x01(\t\x12\x14\n\x0cregistration\x18\x02 \x01(\t\x12\x0e\n\x06\x66ooter\x18\x03 \x01(\t2\xf7\x02\n\x0fInternalService\x12N\n\x05Login\x12\x11.api.LoginRequest\x1a\x12.api.LoginResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/api/internal/login:\x01*\x12V\n\x07Profile\x12\x16.google.protobuf.Empty\x1a\x14.api.ProfileResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/api/internal/profile\x12Y\n\x08\x42randing\x12\x16.google.protobuf.Empty\x1a\x15.api.BrandingResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/api/internal/branding\x12\x61\n\x0cGlobalSearch\x12\x18.api.GlobalSearchRequest\x1a\x19.api.GlobalSearchResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/api/internal/searchb\x06proto3')
  ,
  dependencies=[protos_dot_as_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,protos_dot_as_dot_user__pb2.DESCRIPTOR,])




_PROFILESETTINGS = _descriptor.Descriptor(
  name='ProfileSettings',
  full_name='api.ProfileSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disable_assign_existing_users', full_name='api.ProfileSettings.disable_assign_existing_users', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=146,
  serialized_end=202,
)


_ORGANIZATIONLINK = _descriptor.Descriptor(
  name='OrganizationLink',
  full_name='api.OrganizationLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='api.OrganizationLink.organization_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='organizationID', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organization_name', full_name='api.OrganizationLink.organization_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_admin', full_name='api.OrganizationLink.is_admin', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='api.OrganizationLink.created_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='api.OrganizationLink.updated_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=205,
  serialized_end=405,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='api.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='api.LoginRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='api.LoginRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=407,
  serialized_end=457,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='api.LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jwt', full_name='api.LoginResponse.jwt', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=459,
  serialized_end=487,
)


_PROFILERESPONSE = _descriptor.Descriptor(
  name='ProfileResponse',
  full_name='api.ProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='api.ProfileResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizations', full_name='api.ProfileResponse.organizations', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='api.ProfileResponse.settings', index=2,
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
  serialized_start=490,
  serialized_end=618,
)


_GLOBALSEARCHREQUEST = _descriptor.Descriptor(
  name='GlobalSearchRequest',
  full_name='api.GlobalSearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='search', full_name='api.GlobalSearchRequest.search', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='api.GlobalSearchRequest.limit', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='api.GlobalSearchRequest.offset', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=620,
  serialized_end=688,
)


_GLOBALSEARCHRESPONSE = _descriptor.Descriptor(
  name='GlobalSearchResponse',
  full_name='api.GlobalSearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='api.GlobalSearchResponse.result', index=0,
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
  serialized_start=690,
  serialized_end=753,
)


_GLOBALSEARCHRESULT = _descriptor.Descriptor(
  name='GlobalSearchResult',
  full_name='api.GlobalSearchResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='api.GlobalSearchResult.kind', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='api.GlobalSearchResult.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='api.GlobalSearchResult.organization_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='organizationID', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organization_name', full_name='api.GlobalSearchResult.organization_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_id', full_name='api.GlobalSearchResult.application_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='applicationID', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_name', full_name='api.GlobalSearchResult.application_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_dev_eui', full_name='api.GlobalSearchResult.device_dev_eui', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='deviceDevEUI', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='api.GlobalSearchResult.device_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gateway_mac', full_name='api.GlobalSearchResult.gateway_mac', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gatewayMAC', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gateway_name', full_name='api.GlobalSearchResult.gateway_name', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=756,
  serialized_end=1052,
)


_BRANDINGRESPONSE = _descriptor.Descriptor(
  name='BrandingResponse',
  full_name='api.BrandingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logo', full_name='api.BrandingResponse.logo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registration', full_name='api.BrandingResponse.registration', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='footer', full_name='api.BrandingResponse.footer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1054,
  serialized_end=1124,
)

_ORGANIZATIONLINK.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ORGANIZATIONLINK.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PROFILERESPONSE.fields_by_name['user'].message_type = protos_dot_as_dot_user__pb2._USER
_PROFILERESPONSE.fields_by_name['organizations'].message_type = _ORGANIZATIONLINK
_PROFILERESPONSE.fields_by_name['settings'].message_type = _PROFILESETTINGS
_GLOBALSEARCHRESPONSE.fields_by_name['result'].message_type = _GLOBALSEARCHRESULT
DESCRIPTOR.message_types_by_name['ProfileSettings'] = _PROFILESETTINGS
DESCRIPTOR.message_types_by_name['OrganizationLink'] = _ORGANIZATIONLINK
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
DESCRIPTOR.message_types_by_name['ProfileResponse'] = _PROFILERESPONSE
DESCRIPTOR.message_types_by_name['GlobalSearchRequest'] = _GLOBALSEARCHREQUEST
DESCRIPTOR.message_types_by_name['GlobalSearchResponse'] = _GLOBALSEARCHRESPONSE
DESCRIPTOR.message_types_by_name['GlobalSearchResult'] = _GLOBALSEARCHRESULT
DESCRIPTOR.message_types_by_name['BrandingResponse'] = _BRANDINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProfileSettings = _reflection.GeneratedProtocolMessageType('ProfileSettings', (_message.Message,), dict(
  DESCRIPTOR = _PROFILESETTINGS,
  __module__ = 'protos.as.internal_pb2'
  # @@protoc_insertion_point(class_scope:api.ProfileSettings)
  ))
_sym_db.RegisterMessage(ProfileSettings)

OrganizationLink = _reflection.GeneratedProtocolMessageType('OrganizationLink', (_message.Message,), dict(
  DESCRIPTOR = _ORGANIZATIONLINK,
  __module__ = 'protos.as.internal_pb2'
  # @@protoc_insertion_point(class_scope:api.OrganizationLink)
  ))
_sym_db.RegisterMessage(OrganizationLink)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGINREQUEST,
  __module__ = 'protos.as.internal_pb2'
  # @@protoc_insertion_point(class_scope:api.LoginRequest)
  ))
_sym_db.RegisterMessage(LoginRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOGINRESPONSE,
  __module__ = 'protos.as.internal_pb2'
  # @@protoc_insertion_point(class_scope:api.LoginResponse)
  ))
_sym_db.RegisterMessage(LoginResponse)

ProfileResponse = _reflection.GeneratedProtocolMessageType('ProfileResponse', (_message.Message,), dict(
  DESCRIPTOR = _PROFILERESPONSE,
  __module__ = 'protos.as.internal_pb2'
  # @@protoc_insertion_point(class_scope:api.ProfileResponse)
  ))
_sym_db.RegisterMessage(ProfileResponse)

GlobalSearchRequest = _reflection.GeneratedProtocolMessageType('GlobalSearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALSEARCHREQUEST,
  __module__ = 'protos.as.internal_pb2'
  # @@protoc_insertion_point(class_scope:api.GlobalSearchRequest)
  ))
_sym_db.RegisterMessage(GlobalSearchRequest)

GlobalSearchResponse = _reflection.GeneratedProtocolMessageType('GlobalSearchResponse', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALSEARCHRESPONSE,
  __module__ = 'protos.as.internal_pb2'
  # @@protoc_insertion_point(class_scope:api.GlobalSearchResponse)
  ))
_sym_db.RegisterMessage(GlobalSearchResponse)

GlobalSearchResult = _reflection.GeneratedProtocolMessageType('GlobalSearchResult', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALSEARCHRESULT,
  __module__ = 'protos.as.internal_pb2'
  # @@protoc_insertion_point(class_scope:api.GlobalSearchResult)
  ))
_sym_db.RegisterMessage(GlobalSearchResult)

BrandingResponse = _reflection.GeneratedProtocolMessageType('BrandingResponse', (_message.Message,), dict(
  DESCRIPTOR = _BRANDINGRESPONSE,
  __module__ = 'protos.as.internal_pb2'
  # @@protoc_insertion_point(class_scope:api.BrandingResponse)
  ))
_sym_db.RegisterMessage(BrandingResponse)



_INTERNALSERVICE = _descriptor.ServiceDescriptor(
  name='InternalService',
  full_name='api.InternalService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1127,
  serialized_end=1502,
  methods=[
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='api.InternalService.Login',
    index=0,
    containing_service=None,
    input_type=_LOGINREQUEST,
    output_type=_LOGINRESPONSE,
    serialized_options=_b('\202\323\344\223\002\030\"\023/api/internal/login:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='Profile',
    full_name='api.InternalService.Profile',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_PROFILERESPONSE,
    serialized_options=_b('\202\323\344\223\002\027\022\025/api/internal/profile'),
  ),
  _descriptor.MethodDescriptor(
    name='Branding',
    full_name='api.InternalService.Branding',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_BRANDINGRESPONSE,
    serialized_options=_b('\202\323\344\223\002\030\022\026/api/internal/branding'),
  ),
  _descriptor.MethodDescriptor(
    name='GlobalSearch',
    full_name='api.InternalService.GlobalSearch',
    index=3,
    containing_service=None,
    input_type=_GLOBALSEARCHREQUEST,
    output_type=_GLOBALSEARCHRESPONSE,
    serialized_options=_b('\202\323\344\223\002\026\022\024/api/internal/search'),
  ),
])
_sym_db.RegisterServiceDescriptor(_INTERNALSERVICE)

DESCRIPTOR.services_by_name['InternalService'] = _INTERNALSERVICE

# @@protoc_insertion_point(module_scope)
