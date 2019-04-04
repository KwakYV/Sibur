# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos.as import gatewayProfile_pb2 as protos_dot_as_dot_gatewayProfile__pb2


class GatewayProfileServiceStub(object):
  """GatewayProfileService is the service managing the gateway-profiles.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/api.GatewayProfileService/Create',
        request_serializer=protos_dot_as_dot_gatewayProfile__pb2.CreateGatewayProfileRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_gatewayProfile__pb2.CreateGatewayProfileResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/api.GatewayProfileService/Get',
        request_serializer=protos_dot_as_dot_gatewayProfile__pb2.GetGatewayProfileRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_gatewayProfile__pb2.GetGatewayProfileResponse.FromString,
        )
    self.Update = channel.unary_unary(
        '/api.GatewayProfileService/Update',
        request_serializer=protos_dot_as_dot_gatewayProfile__pb2.UpdateGatewayProfileRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Delete = channel.unary_unary(
        '/api.GatewayProfileService/Delete',
        request_serializer=protos_dot_as_dot_gatewayProfile__pb2.DeleteGatewayProfileRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.List = channel.unary_unary(
        '/api.GatewayProfileService/List',
        request_serializer=protos_dot_as_dot_gatewayProfile__pb2.ListGatewayProfilesRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_gatewayProfile__pb2.ListGatewayProfilesResponse.FromString,
        )


class GatewayProfileServiceServicer(object):
  """GatewayProfileService is the service managing the gateway-profiles.
  """

  def Create(self, request, context):
    """Create creates the given gateway-profile.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get returns the gateway-profile matching the given id.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Update updates the given gateway-profile.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Delete deletes the gateway-profile matching the given id.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """List returns the existing gateway-profiles.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GatewayProfileServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=protos_dot_as_dot_gatewayProfile__pb2.CreateGatewayProfileRequest.FromString,
          response_serializer=protos_dot_as_dot_gatewayProfile__pb2.CreateGatewayProfileResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=protos_dot_as_dot_gatewayProfile__pb2.GetGatewayProfileRequest.FromString,
          response_serializer=protos_dot_as_dot_gatewayProfile__pb2.GetGatewayProfileResponse.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=protos_dot_as_dot_gatewayProfile__pb2.UpdateGatewayProfileRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=protos_dot_as_dot_gatewayProfile__pb2.DeleteGatewayProfileRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=protos_dot_as_dot_gatewayProfile__pb2.ListGatewayProfilesRequest.FromString,
          response_serializer=protos_dot_as_dot_gatewayProfile__pb2.ListGatewayProfilesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.GatewayProfileService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
