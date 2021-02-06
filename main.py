from task_env import TaskEnv
from threading import Thread
import os, time

taskEnv = TaskEnv()


class Program(Thread):
    def __init__(self, task_env):
        Thread.__init__(self)
        print('program')

    def run(self):
        while True:
            # taskEnv.kafka.poll
            print('run')
            time.sleep(1)

if __name__ == '__main__':
    for t in [Program(taskEnv)]:
        t.start()