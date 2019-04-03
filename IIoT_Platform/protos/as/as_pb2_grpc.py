# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos.as import as_pb2 as protos_dot_as_dot_as__pb2


class ApplicationServerServiceStub(object):
  """ApplicationServerService is the service providing the application-server interface.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HandleUplinkData = channel.unary_unary(
        '/as.ApplicationServerService/HandleUplinkData',
        request_serializer=protos_dot_as_dot_as__pb2.HandleUplinkDataRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.HandleProprietaryUplink = channel.unary_unary(
        '/as.ApplicationServerService/HandleProprietaryUplink',
        request_serializer=protos_dot_as_dot_as__pb2.HandleProprietaryUplinkRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.HandleError = channel.unary_unary(
        '/as.ApplicationServerService/HandleError',
        request_serializer=protos_dot_as_dot_as__pb2.HandleErrorRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.HandleDownlinkACK = channel.unary_unary(
        '/as.ApplicationServerService/HandleDownlinkACK',
        request_serializer=protos_dot_as_dot_as__pb2.HandleDownlinkACKRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SetDeviceStatus = channel.unary_unary(
        '/as.ApplicationServerService/SetDeviceStatus',
        request_serializer=protos_dot_as_dot_as__pb2.SetDeviceStatusRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.SetDeviceLocation = channel.unary_unary(
        '/as.ApplicationServerService/SetDeviceLocation',
        request_serializer=protos_dot_as_dot_as__pb2.SetDeviceLocationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ApplicationServerServiceServicer(object):
  """ApplicationServerService is the service providing the application-server interface.
  """

  def HandleUplinkData(self, request, context):
    """HandleUplinkData handles uplink data received from an end-device.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HandleProprietaryUplink(self, request, context):
    """HandleProprietaryUplink handles proprietary uplink payloads.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HandleError(self, request, context):
    """HandleError handles an error message.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HandleDownlinkACK(self, request, context):
    """HandleDownlinkACK handles a downlink ACK or nACK response.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDeviceStatus(self, request, context):
    """SetDeviceStatus updates the device-status for a device.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDeviceLocation(self, request, context):
    """SetDeviceLocation updates the device-location for a device.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ApplicationServerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HandleUplinkData': grpc.unary_unary_rpc_method_handler(
          servicer.HandleUplinkData,
          request_deserializer=protos_dot_as_dot_as__pb2.HandleUplinkDataRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'HandleProprietaryUplink': grpc.unary_unary_rpc_method_handler(
          servicer.HandleProprietaryUplink,
          request_deserializer=protos_dot_as_dot_as__pb2.HandleProprietaryUplinkRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'HandleError': grpc.unary_unary_rpc_method_handler(
          servicer.HandleError,
          request_deserializer=protos_dot_as_dot_as__pb2.HandleErrorRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'HandleDownlinkACK': grpc.unary_unary_rpc_method_handler(
          servicer.HandleDownlinkACK,
          request_deserializer=protos_dot_as_dot_as__pb2.HandleDownlinkACKRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SetDeviceStatus': grpc.unary_unary_rpc_method_handler(
          servicer.SetDeviceStatus,
          request_deserializer=protos_dot_as_dot_as__pb2.SetDeviceStatusRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'SetDeviceLocation': grpc.unary_unary_rpc_method_handler(
          servicer.SetDeviceLocation,
          request_deserializer=protos_dot_as_dot_as__pb2.SetDeviceLocationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'as.ApplicationServerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
