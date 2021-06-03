# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from . import dht_pb2 as dht__pb2


class DHTStub(object):
    """this protocol defines how nodes form a distributed hash table.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.rpc_ping = channel.unary_unary(
                '/DHT/rpc_ping',
                request_serializer=dht__pb2.PingRequest.SerializeToString,
                response_deserializer=dht__pb2.PingResponse.FromString,
                )
        self.rpc_store = channel.unary_unary(
                '/DHT/rpc_store',
                request_serializer=dht__pb2.StoreRequest.SerializeToString,
                response_deserializer=dht__pb2.StoreResponse.FromString,
                )
        self.rpc_find = channel.unary_unary(
                '/DHT/rpc_find',
                request_serializer=dht__pb2.FindRequest.SerializeToString,
                response_deserializer=dht__pb2.FindResponse.FromString,
                )


class DHTServicer(object):
    """this protocol defines how nodes form a distributed hash table.

    """

    def rpc_ping(self, request, context):
        """find out recipient's DHTID and possibly update its routing table
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_store(self, request, context):
        """request a node to store one or multiple data items (key - value - expiration)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rpc_find(self, request, context):
        """for given keys, request values (if stored) or a list of peers that are likely to have them
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DHTServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'rpc_ping': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_ping,
                    request_deserializer=dht__pb2.PingRequest.FromString,
                    response_serializer=dht__pb2.PingResponse.SerializeToString,
            ),
            'rpc_store': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_store,
                    request_deserializer=dht__pb2.StoreRequest.FromString,
                    response_serializer=dht__pb2.StoreResponse.SerializeToString,
            ),
            'rpc_find': grpc.unary_unary_rpc_method_handler(
                    servicer.rpc_find,
                    request_deserializer=dht__pb2.FindRequest.FromString,
                    response_serializer=dht__pb2.FindResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DHT', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DHT(object):
    """this protocol defines how nodes form a distributed hash table.

    """

    @staticmethod
    def rpc_ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DHT/rpc_ping',
            dht__pb2.PingRequest.SerializeToString,
            dht__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_store(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DHT/rpc_store',
            dht__pb2.StoreRequest.SerializeToString,
            dht__pb2.StoreResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rpc_find(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DHT/rpc_find',
            dht__pb2.FindRequest.SerializeToString,
            dht__pb2.FindResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
