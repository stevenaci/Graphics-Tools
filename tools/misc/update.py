
class Lazy:

    subscribers:list

    def __init__(self):
        self.subscribers = []

    def update(self, kwargs: dict):
        pass

    def update_subscribers(self):
        [s.update() for s in self.subscribers]
        pass

    def add_subscriber(self, s):
        self.subscribers.append(s)
