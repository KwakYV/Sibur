# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protos.as import application_pb2 as protos_dot_as_dot_application__pb2


class ApplicationServiceStub(object):
  """ApplicationService is the service managing applications.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/api.ApplicationService/Create',
        request_serializer=protos_dot_as_dot_application__pb2.CreateApplicationRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_application__pb2.CreateApplicationResponse.FromString,
        )
    self.Get = channel.unary_unary(
        '/api.ApplicationService/Get',
        request_serializer=protos_dot_as_dot_application__pb2.GetApplicationRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_application__pb2.GetApplicationResponse.FromString,
        )
    self.Update = channel.unary_unary(
        '/api.ApplicationService/Update',
        request_serializer=protos_dot_as_dot_application__pb2.UpdateApplicationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Delete = channel.unary_unary(
        '/api.ApplicationService/Delete',
        request_serializer=protos_dot_as_dot_application__pb2.DeleteApplicationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.List = channel.unary_unary(
        '/api.ApplicationService/List',
        request_serializer=protos_dot_as_dot_application__pb2.ListApplicationRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_application__pb2.ListApplicationResponse.FromString,
        )
    self.CreateHTTPIntegration = channel.unary_unary(
        '/api.ApplicationService/CreateHTTPIntegration',
        request_serializer=protos_dot_as_dot_application__pb2.CreateHTTPIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetHTTPIntegration = channel.unary_unary(
        '/api.ApplicationService/GetHTTPIntegration',
        request_serializer=protos_dot_as_dot_application__pb2.GetHTTPIntegrationRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_application__pb2.GetHTTPIntegrationResponse.FromString,
        )
    self.UpdateHTTPIntegration = channel.unary_unary(
        '/api.ApplicationService/UpdateHTTPIntegration',
        request_serializer=protos_dot_as_dot_application__pb2.UpdateHTTPIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteHTTPIntegration = channel.unary_unary(
        '/api.ApplicationService/DeleteHTTPIntegration',
        request_serializer=protos_dot_as_dot_application__pb2.DeleteHTTPIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.CreateInfluxDBIntegration = channel.unary_unary(
        '/api.ApplicationService/CreateInfluxDBIntegration',
        request_serializer=protos_dot_as_dot_application__pb2.CreateInfluxDBIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.GetInfluxDBIntegration = channel.unary_unary(
        '/api.ApplicationService/GetInfluxDBIntegration',
        request_serializer=protos_dot_as_dot_application__pb2.GetInfluxDBIntegrationRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_application__pb2.GetInfluxDBIntegrationResponse.FromString,
        )
    self.UpdateInfluxDBIntegration = channel.unary_unary(
        '/api.ApplicationService/UpdateInfluxDBIntegration',
        request_serializer=protos_dot_as_dot_application__pb2.UpdateInfluxDBIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.DeleteInfluxDBIntegration = channel.unary_unary(
        '/api.ApplicationService/DeleteInfluxDBIntegration',
        request_serializer=protos_dot_as_dot_application__pb2.DeleteInfluxDBIntegrationRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListIntegrations = channel.unary_unary(
        '/api.ApplicationService/ListIntegrations',
        request_serializer=protos_dot_as_dot_application__pb2.ListIntegrationRequest.SerializeToString,
        response_deserializer=protos_dot_as_dot_application__pb2.ListIntegrationResponse.FromString,
        )


class ApplicationServiceServicer(object):
  """ApplicationService is the service managing applications.
  """

  def Create(self, request, context):
    """Create creates the given application.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get returns the requested application.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Update updates the given application.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Delete deletes the given application.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """List lists the available applications.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateHTTPIntegration(self, request, context):
    """CreateHTTPIntegration creates a HTTP application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHTTPIntegration(self, request, context):
    """GetHTTPIntegration returns the HTTP application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateHTTPIntegration(self, request, context):
    """UpdateHTTPIntegration updates the HTTP application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteHTTPIntegration(self, request, context):
    """DeleteIntegration deletes the HTTP application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateInfluxDBIntegration(self, request, context):
    """CreateInfluxDBIntegration create an InfluxDB application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetInfluxDBIntegration(self, request, context):
    """GetInfluxDBIntegration returns the InfluxDB application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateInfluxDBIntegration(self, request, context):
    """UpdateInfluxDBIntegration updates the InfluxDB application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteInfluxDBIntegration(self, request, context):
    """DeleteInfluxDBIntegration deletes the InfluxDB application-integration.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListIntegrations(self, request, context):
    """ListIntegrations lists all configured integrations.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ApplicationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=protos_dot_as_dot_application__pb2.CreateApplicationRequest.FromString,
          response_serializer=protos_dot_as_dot_application__pb2.CreateApplicationResponse.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=protos_dot_as_dot_application__pb2.GetApplicationRequest.FromString,
          response_serializer=protos_dot_as_dot_application__pb2.GetApplicationResponse.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=protos_dot_as_dot_application__pb2.UpdateApplicationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=protos_dot_as_dot_application__pb2.DeleteApplicationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=protos_dot_as_dot_application__pb2.ListApplicationRequest.FromString,
          response_serializer=protos_dot_as_dot_application__pb2.ListApplicationResponse.SerializeToString,
      ),
      'CreateHTTPIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.CreateHTTPIntegration,
          request_deserializer=protos_dot_as_dot_application__pb2.CreateHTTPIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetHTTPIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.GetHTTPIntegration,
          request_deserializer=protos_dot_as_dot_application__pb2.GetHTTPIntegrationRequest.FromString,
          response_serializer=protos_dot_as_dot_application__pb2.GetHTTPIntegrationResponse.SerializeToString,
      ),
      'UpdateHTTPIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateHTTPIntegration,
          request_deserializer=protos_dot_as_dot_application__pb2.UpdateHTTPIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteHTTPIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteHTTPIntegration,
          request_deserializer=protos_dot_as_dot_application__pb2.DeleteHTTPIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'CreateInfluxDBIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.CreateInfluxDBIntegration,
          request_deserializer=protos_dot_as_dot_application__pb2.CreateInfluxDBIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'GetInfluxDBIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.GetInfluxDBIntegration,
          request_deserializer=protos_dot_as_dot_application__pb2.GetInfluxDBIntegrationRequest.FromString,
          response_serializer=protos_dot_as_dot_application__pb2.GetInfluxDBIntegrationResponse.SerializeToString,
      ),
      'UpdateInfluxDBIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateInfluxDBIntegration,
          request_deserializer=protos_dot_as_dot_application__pb2.UpdateInfluxDBIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'DeleteInfluxDBIntegration': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteInfluxDBIntegration,
          request_deserializer=protos_dot_as_dot_application__pb2.DeleteInfluxDBIntegrationRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListIntegrations': grpc.unary_unary_rpc_method_handler(
          servicer.ListIntegrations,
          request_deserializer=protos_dot_as_dot_application__pb2.ListIntegrationRequest.FromString,
          response_serializer=protos_dot_as_dot_application__pb2.ListIntegrationResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.ApplicationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
