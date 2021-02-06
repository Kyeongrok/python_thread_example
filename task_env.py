class TaskEnv:
    kafka = None
    def __init__(self):

        self.kafka = KafkaUtil()
        print('init kafka')

class KafkaUtil:

    def __init__(self):
        print('kafka')
        # config map을 {}로 받음
        # receive secret as {}

        self.consume = None
        self.produce = None