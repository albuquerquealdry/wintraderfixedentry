from websocket import create_connection
import stomper as stomper

def sendOrder(order):
    ws = create_connection("ws://localhost:8080/orderServer")
    print("Sending 'Hello, World'...")
    ws.send(stomper.send("/app/sendOrderV2/teste", order))
    print("Sent")
    ws.close()

def sendInformation(dataRequest):
    conectWB= create_connection("ws://localhost:8080/orderServer")
    conectWB.send(stomper.send("/app/sendOrderToTraderOffice/",dataRequest))
    conectWB.close()

