from concurrent import futures
import logging

import const
import grpc
import score_pb2
import score_pb2_grpc

score = [
{
 'player': 'player1',
 'score': 0
 },
 {
 'player': 'player2',
 'score': 0
 }
]

class Operacoes(score_pb2_grpc.OperacoesServicer):

    def ConsultCurrentScore (self, request, context):
        #play = [ p for p in score if (p['player'] == request.player) ]
        #return score_pb2.DataScore(player=play[0]['player'], score=play[0]['score'])
        list = score_pb2.ListScore()
        for p in score:
            data = score_pb2.DataScore(player=p['player'], score=p['score'])
            list.Data_Score.append(data)
        return list

    def CalcNewScore (self, request, context):
        play = [ p for p in score if (p['player'] == request.player) ]
        newscore = play[0]['score']
        newscore = newscore + request.point
        return score_pb2.Player(player=request.player,point=newscore)

    def UpdateScore (self, request, context):
        i = 0
        while i < len(score):
            if (score[i]['player'] == request.player):
                score[i]['score'] = request.point
            i = i + 1
        return score_pb2.Status(status='OK')

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