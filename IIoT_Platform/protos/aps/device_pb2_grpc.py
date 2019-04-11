# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos.aps import device_pb2 as protos_dot_aps_dot_device__pb2


class DeviceServiceStub(object):
  """DeviceService is the service managing the devices.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/api.DeviceService/Create',
        request_serializer=protos_dot_aps_dot_device__pb2.CreateDeviceRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Get = channel.unary_unary(
        '/api.DeviceService/Get',
        request_serializer=protos_dot_aps_dot_device__pb2.GetDeviceRequest.SerializeToString,
        response_deserializer=protos_dot_aps_dot_device__pb2.GetDeviceResponse.FromString,
        )
    self.List = channel.unary_unary(
        '/api.DeviceService/List',
        request_serializer=protos_dot_aps_dot_device__pb2.ListDeviceRequest.SerializeToString,
        response_deserializer=protos_dot_aps_dot_device__pb2.ListDeviceResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/api.DeviceService/Delete',
        request_serializer=protos_dot_aps_dot_device__pb2.DeleteDeviceRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Update = channel.unary_unary(
        '/api.DeviceService/Update',
        request_serializer=protos_dot_aps_dot_device__pb2.UpdateDeviceRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CreateKeys = channel.unary_unary(
        '/api.DeviceService/CreateKeys',
        request_serializer=protos_dot_aps_dot_device__pb2.CreateDeviceKeysRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetKeys = channel.unary_unary(
        '/api.DeviceService/GetKeys',
        request_serializer=protos_dot_aps_dot_device__pb2.GetDeviceKeysRequest.SerializeToString,
        response_deserializer=protos_dot_aps_dot_device__pb2.GetDeviceKeysResponse.FromString,
        )
    self.UpdateKeys = channel.unary_unary(
        '/api.DeviceService/UpdateKeys',
        request_serializer=protos_dot_aps_dot_device__pb2.UpdateDeviceKeysRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteKeys = channel.unary_unary(
        '/api.DeviceService/DeleteKeys',
        request_serializer=protos_dot_aps_dot_device__pb2.DeleteDeviceKeysRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Activate = channel.unary_unary(
        '/api.DeviceService/Activate',
        request_serializer=protos_dot_aps_dot_device__pb2.ActivateDeviceRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Deactivate = channel.unary_unary(
        '/api.DeviceService/Deactivate',
        request_serializer=protos_dot_aps_dot_device__pb2.DeactivateDeviceRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetActivation = channel.unary_unary(
        '/api.DeviceService/GetActivation',
        request_serializer=protos_dot_aps_dot_device__pb2.GetDeviceActivationRequest.SerializeToString,
        response_deserializer=protos_dot_aps_dot_device__pb2.GetDeviceActivationResponse.FromString,
        )
    self.GetRandomDevAddr = channel.unary_unary(
        '/api.DeviceService/GetRandomDevAddr',
        request_serializer=protos_dot_aps_dot_device__pb2.GetRandomDevAddrRequest.SerializeToString,
        response_deserializer=protos_dot_aps_dot_device__pb2.GetRandomDevAddrResponse.FromString,
        )
    self.StreamFrameLogs = channel.unary_stream(
        '/api.DeviceService/StreamFrameLogs',
        request_serializer=protos_dot_aps_dot_device__pb2.StreamDeviceFrameLogsRequest.SerializeToString,
        response_deserializer=protos_dot_aps_dot_device__pb2.StreamDeviceFrameLogsResponse.FromString,
        )
    self.StreamEventLogs = channel.unary_stream(
        '/api.DeviceService/StreamEventLogs',
        request_serializer=protos_dot_aps_dot_device__pb2.StreamDeviceEventLogsRequest.SerializeToString,
        response_deserializer=protos_dot_aps_dot_device__pb2.StreamDeviceEventLogsResponse.FromString,
        )


class DeviceServiceServicer(object):
  """DeviceService is the service managing the devices.
  """

  def Create(self, request, context):
    """Create creates the given device.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get returns the device matching the given DevEUI.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """List returns the available devices.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Delete deletes the device matching the given DevEUI.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Update updates the device matching the given DevEUI.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateKeys(self, request, context):
    """CreateKeys creates the given device-keys.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetKeys(self, request, context):
    """GetKeys returns the device-keys for the given DevEUI.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateKeys(self, request, context):
    """UpdateKeys updates the device-keys.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteKeys(self, request, context):
    """DeleteKeys deletes the device-keys for the given DevEUI.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Activate(self, request, context):
    """Activate (re)activates the device (only when ABP is set to true).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Deactivate(self, request, context):
    """Deactivate de-activates the device.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetActivation(self, request, context):
    """GetActivation returns the current activation details of the device (OTAA and ABP).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRandomDevAddr(self, request, context):
    """GetRandomDevAddr returns a random DevAddr taking the NwkID prefix into account.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamFrameLogs(self, request, context):
    """StreamFrameLogs streams the uplink and downlink frame-logs for the given DevEUI.
    * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.
    * This endpoint does not work from a web-browser.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamEventLogs(self, request, context):
    """StreamEventLogs stream the device events (uplink payloads, ACKs, joins, errors).
    * This endpoint is intended for debugging only.
    * This endpoint does not work from a web-browser.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DeviceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=protos_dot_aps_dot_device__pb2.CreateDeviceRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=protos_dot_aps_dot_device__pb2.GetDeviceRequest.FromString,
          response_serializer=protos_dot_aps_dot_device__pb2.GetDeviceResponse.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=protos_dot_aps_dot_device__pb2.ListDeviceRequest.FromString,
          response_serializer=protos_dot_aps_dot_device__pb2.ListDeviceResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=protos_dot_aps_dot_device__pb2.DeleteDeviceRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=protos_dot_aps_dot_device__pb2.UpdateDeviceRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CreateKeys': grpc.unary_unary_rpc_method_handler(
          servicer.CreateKeys,
          request_deserializer=protos_dot_aps_dot_device__pb2.CreateDeviceKeysRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetKeys': grpc.unary_unary_rpc_method_handler(
          servicer.GetKeys,
          request_deserializer=protos_dot_aps_dot_device__pb2.GetDeviceKeysRequest.FromString,
          response_serializer=protos_dot_aps_dot_device__pb2.GetDeviceKeysResponse.SerializeToString,
      ),
      'UpdateKeys': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateKeys,
          request_deserializer=protos_dot_aps_dot_device__pb2.UpdateDeviceKeysRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteKeys': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteKeys,
          request_deserializer=protos_dot_aps_dot_device__pb2.DeleteDeviceKeysRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Activate': grpc.unary_unary_rpc_method_handler(
          servicer.Activate,
          request_deserializer=protos_dot_aps_dot_device__pb2.ActivateDeviceRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Deactivate': grpc.unary_unary_rpc_method_handler(
          servicer.Deactivate,
          request_deserializer=protos_dot_aps_dot_device__pb2.DeactivateDeviceRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetActivation': grpc.unary_unary_rpc_method_handler(
          servicer.GetActivation,
          request_deserializer=protos_dot_aps_dot_device__pb2.GetDeviceActivationRequest.FromString,
          response_serializer=protos_dot_aps_dot_device__pb2.GetDeviceActivationResponse.SerializeToString,
      ),
      'GetRandomDevAddr': grpc.unary_unary_rpc_method_handler(
          servicer.GetRandomDevAddr,
          request_deserializer=protos_dot_aps_dot_device__pb2.GetRandomDevAddrRequest.FromString,
          response_serializer=protos_dot_aps_dot_device__pb2.GetRandomDevAddrResponse.SerializeToString,
      ),
      'StreamFrameLogs': grpc.unary_stream_rpc_method_handler(
          servicer.StreamFrameLogs,
          request_deserializer=protos_dot_aps_dot_device__pb2.StreamDeviceFrameLogsRequest.FromString,
          response_serializer=protos_dot_aps_dot_device__pb2.StreamDeviceFrameLogsResponse.SerializeToString,
      ),
      'StreamEventLogs': grpc.unary_stream_rpc_method_handler(
          servicer.StreamEventLogs,
          request_deserializer=protos_dot_aps_dot_device__pb2.StreamDeviceEventLogsRequest.FromString,
          response_serializer=protos_dot_aps_dot_device__pb2.StreamDeviceEventLogsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.DeviceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))