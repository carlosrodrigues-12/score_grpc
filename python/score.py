from concurrent import futures
import logging

import const
import grpc
import score_pb2
import score_pb2_grpc

score = []

def CalcScore(ip_dest,player,point):
    with grpc.insecure_channel(ip_dest) as channel:
        stub = score_pb2_grpc.MessageStub(channel)
        response = stub.CalcNewScore(score_pb2.Player(player=player,point=point))
        print("Client received: " + response.message)
        return response.message

class Message(score_pb2_grpc.MessageServicer):

    def ConsultCurrentScore (self, request, context):
        return score_pb2.DataScore(score=score)
        
    def UpdateScore (self, request, context):
        data = {
            "player":request.player,
            "point":request.point
        }
        ip_dest = const.registry[request.player]
        score.append(data)
        CalcScore(ip_dest,request.player,request.point)
        return score_pb2.Status(status='OK')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    score_pb2_grpc.add_MessageServicer_to_server(Message(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    print('\n')
    serve()