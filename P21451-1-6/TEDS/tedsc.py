import logging
import os
import signal
import time

import uvloop
import asyncio
import gmqtt

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

STOP = asyncio.Event()


def on_connect(client, flags, rc, properties):
    logging.info('[CONNECTED {}]'.format(client._client_id))


def on_message(client, topic, payload, qos, properties):
    logging.info('[RECV MSG {}] TOPIC: {} PAYLOAD: {} QOS: {} PROPERTIES: {}'
                 .format(client._client_id, topic, payload, qos, properties))
    payload = payload.decode('utf-8')
    print("PAYLOAD:"+payload)

def on_disconnect(client, packet, exc=None):
    logging.info('[DISCONNECTED {}]'.format(client._client_id))


def on_subscribe(client, mid, qos):
    logging.info('[SUBSCRIBED {}] QOS: {}'.format(client._client_id, qos))


def assign_callbacks_to_client(client):
    # helper function which sets up client's callbacks
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe


def ask_exit(*args):
    STOP.set()


async def main(broker_host, broker_port, token):
    # create client instance, kwargs (session expiry interval and maximum packet size)
    # will be send as properties in connect packet
    sub_client = gmqtt.Client("service-res", session_expiry_interval=600, maximum_packet_size=65535)

    assign_callbacks_to_client(sub_client)
    sub_client.set_auth_credentials(token, None)
    await sub_client.connect(broker_host, broker_port)

    # two overlapping subscriptions with different subscription identifiers
    sub_client.subscribe('/PRISM/SERVICE/1451RES', qos=1, subscription_identifier=1)

    pub_client = gmqtt.Client("service-req")

    assign_callbacks_to_client(pub_client)
    pub_client.set_auth_credentials(token, None)
    await pub_client.connect(broker_host, broker_port)

    pub_client.publish('/PRISM/NCAP/1451OPE', 'METATEDS/TEMP', qos=1, content_type='utf-8',
                       message_expiry_interval=60, response_topic='/PRISM/SERVICE/1451RES', user_property=('time', str(time.time())))

    await STOP.wait()
    await pub_client.disconnect()
    await sub_client.disconnect(session_expiry_interval=0)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
#    logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.ERROR)

    host = os.environ.get('HOST', '192.168.0.10')
    port = 1883
    token = os.environ.get('TOKEN', 'fake token')

    loop.add_signal_handler(signal.SIGINT, ask_exit)
    loop.add_signal_handler(signal.SIGTERM, ask_exit)

    loop.run_until_complete(main(host, port, token))