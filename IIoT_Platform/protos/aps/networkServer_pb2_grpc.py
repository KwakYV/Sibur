# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos.aps import networkServer_pb2 as protos_dot_as_dot_networkServer__pb2


class NetworkServerServiceStub(object):
  """NetworkServerService is the service managing network-servers.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/api.NetworkServerService/Create',
        request_serializer=protos_dot_as_dot_networkServer__pb2.CreateNetworkServerRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_networkServer__pb2.CreateNetworkServerResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/api.NetworkServerService/Get',
        request_serializer=protos_dot_as_dot_networkServer__pb2.GetNetworkServerRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_networkServer__pb2.GetNetworkServerResponse.FromString,
        )
    self.Update = channel.unary_unary(
        '/api.NetworkServerService/Update',
        request_serializer=protos_dot_as_dot_networkServer__pb2.UpdateNetworkServerRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Delete = channel.unary_unary(
        '/api.NetworkServerService/Delete',
        request_serializer=protos_dot_as_dot_networkServer__pb2.DeleteNetworkServerRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.List = channel.unary_unary(
        '/api.NetworkServerService/List',
        request_serializer=protos_dot_as_dot_networkServer__pb2.ListNetworkServerRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_networkServer__pb2.ListNetworkServerResponse.FromString,
        )


class NetworkServerServiceServicer(object):
  """NetworkServerService is the service managing network-servers.
  """

  def Create(self, request, context):
    """Create creates the given network-server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get returns the network-server matching the given id.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Update updates the given network-server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Delete deletes the network-server matching the given id.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """List lists the available network-servers.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NetworkServerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=protos_dot_as_dot_networkServer__pb2.CreateNetworkServerRequest.FromString,
          response_serializer=protos_dot_as_dot_networkServer__pb2.CreateNetworkServerResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=protos_dot_as_dot_networkServer__pb2.GetNetworkServerRequest.FromString,
          response_serializer=protos_dot_as_dot_networkServer__pb2.GetNetworkServerResponse.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=protos_dot_as_dot_networkServer__pb2.UpdateNetworkServerRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=protos_dot_as_dot_networkServer__pb2.DeleteNetworkServerRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=protos_dot_as_dot_networkServer__pb2.ListNetworkServerRequest.FromString,
          response_serializer=protos_dot_as_dot_networkServer__pb2.ListNetworkServerResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.NetworkServerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))