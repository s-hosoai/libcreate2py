import paho.mqtt.client as mqtt


class CourseMQTT(object):
    def __init__(self, host, subscribe_topic="/course/corner/#"):
        super(CourseMQTT, self).__init__()
        self.topic = subscribe_topic
        client = mqtt.Client(protocol=mqtt.MQTTv311)
        client.connect(host, keepalive=60)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        self.client = client
        self.target = ""
        self.listeners=[]

    def on_connect(self, client, userdata, flags, respons_code):
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        event = ""
        if (int(msg.payload) == 1):
            event="enterTarget"
        else:
            event="leaveTarget"
        self.target = msg.topic.split("/")[-1]
        for callback in self.listeners:
            callback([event])

    def wait_message(self):
        self.client.loop_forever()

    def add_event_listener(self, listener):
        self.listeners.append(listener)

# def notify(events):
#     for e in events:
#         print(e+" to "+main.target)
#
# main = CourseMQTT("localhost")
# main.add_event_listener(notify)
# main.wait_message()
