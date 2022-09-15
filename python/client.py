from __future__ import print_function
import logging
from urllib import response

import grpc
import score_pb2
import score_pb2_grpc
import sys
import const

def run(myidentify,point,op):
    with grpc.insecure_channel(const.CHAT_SERVER_HOST) as channel:
        stub = score_pb2_grpc.OperacoesStub(channel)

        if (op == 1):
            response = stub.ConsultCurrentScore(score_pb2.EmptyMessage())
            print(f'SCORE ATUAL\n{response}')
        else:
            response = stub.ConsultCurrentScore(score_pb2.EmptyMessage())
            print(f'SCORE ATUAL\n{response}')

            calc = stub.CalcNewScore(score_pb2.Player(player=myidentify,point=point))
            print(f'CALC SCORE {myidentify} = {calc.point}')

            upd = stub.UpdateScore(score_pb2.Player(player=myidentify,point=calc.point))
            print(f'NEW SCORE\n{upd}')

if __name__ == '__main__':
    logging.basicConfig()
    myidentify = str(sys.argv[1])
    print(f'PLAYER: {myidentify}')
    while True:
        op = int(input("1 CONSULTA - 2 UPDATE SCORE: "))
        if(op == 1):
            run(myidentify,point=0,op)
        else:
            point = int(input("ENTER POINT: "))
            run(myidentify,point,op)