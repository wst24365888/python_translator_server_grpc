from concurrent import futures
import time
import logging

import grpc

import src.translator_pb2 as translator_pb2
import src.translator_pb2_grpc as translator_pb2_grpc

import translatepy

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Translator(translator_pb2_grpc.TranslatorServicer):

    def __init__(self) -> None:
        super().__init__()
        self.translator = translatepy.Translator()

    def Translate(self, request, context):
        return translator_pb2.Translate(result=self.translateTo(request.sourceContent, request.sourceLang, request.targetLang))

    def translateTo(self, sourceContent, sourceLang, targetLang):
        return self.translator.translate(sourceContent, targetLang, source_language=sourceLang)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    translator_pb2_grpc.add_TranslatorServicer_to_server(Translator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
