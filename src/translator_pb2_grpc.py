# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import translator_pb2 as translator__pb2


class TranslatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Translate = channel.unary_unary(
                '/python_translator_server_grpc.Translator/Translate',
                request_serializer=translator__pb2.TranslateRequest.SerializeToString,
                response_deserializer=translator__pb2.TranslateReply.FromString,
                )


class TranslatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Translate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TranslatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Translate': grpc.unary_unary_rpc_method_handler(
                    servicer.Translate,
                    request_deserializer=translator__pb2.TranslateRequest.FromString,
                    response_serializer=translator__pb2.TranslateReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'python_translator_server_grpc.Translator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Translator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Translate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/python_translator_server_grpc.Translator/Translate',
            translator__pb2.TranslateRequest.SerializeToString,
            translator__pb2.TranslateReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
