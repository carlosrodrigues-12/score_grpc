from concurrent import futures
import logging

import const
import grpc
import score_pb2
import score_pb2_grpc

score = [
{
 'player': 'Player1',
 'score': 10
 },
 {
 'player': 'Player2',
 'score': 20
 }
]

'''
def CalcScore(ip_dest,player,point):
    with grpc.insecure_channel(ip_dest) as channel:
        stub = score_pb2_grpc.MessageStub(channel)
        response = stub.CalcNewScore(score_pb2.Player(player=player,point=point))
        print("Client received: " + response.message)
        return score_pb2.Player(player=player,point=point)
'''

class Operacoes(score_pb2_grpc.OperacoesServicer):

    def ConsultCurrentScore (self, request, context):
        list = score_pb2.ListScore()
        for item in score:
            data = score_pb2.DataScore(player=item['player'], score=item['score'])
            list.Data_Score.append(data)
            return list
        return score_pb2.DataScore(player=request.player,score=request.score)

    def CalcNewScore (self, request, context):
        
        return score_pb2.Player(player=request.player,point=request.point)

    def UpdateScore (self, request, context):
        
        return score_pb2.Status(status='OK')
        
'''    def UpdateScore (self, request, context):
        data = {
            "player":request.player,
            "point":request.point
        }
        ip_dest = const.registry[request.player]
        score.append(data)
        CalcScore(ip_dest,request.player,request.point)
        return score_pb2.Status(status='OK')
'''

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    score_pb2_grpc.add_OperacoesServicer_to_server(Operacoes(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    print('\n')
    serve()