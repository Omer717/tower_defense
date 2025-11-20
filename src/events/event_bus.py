from events.game_event import GameEvent

class EventBus:
    def __init__(self):
        self.listeners = {event: [] for event in GameEvent}

    def subscribe(self, event: GameEvent, callback):
        self.listeners[event].append(callback)

    def publish(self, event: GameEvent, data=None):
        for callback in self.listeners[event]:
            callback(data)
