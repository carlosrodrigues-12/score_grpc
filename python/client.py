from __future__ import print_function
import logging

import grpc
import score_pb2
import score_pb2_grpc
import sys
import const
global myidentify

def run():
    with grpc.insecure_channel(const.CHAT_SERVER_HOST) as channel:
        stub = score_pb2_grpc.OperacoesStub(channel)

        # Score
        response = stub.ConsultCurrentScore(score_pb2.ConsultPlayer(player=myidentify))
        # print ('Employee\'s data: ' + str(response))
        print(response)

if __name__ == '__main__':
    logging.basicConfig()
    myip = str(sys.argv[1])
    run()