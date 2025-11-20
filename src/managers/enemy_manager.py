from entities.enemy import Enemy
from events.event_bus import EventBus
from events.game_event import GameEvent


class EnemyManager:
    def __init__(self, game_state, event_bus: EventBus):
        self.enemies = []
        self.event_bus = event_bus
        self.game_state = game_state

    def spawn_enemy(self, path):
        enemy = Enemy(path)
        self.enemies.append(enemy)

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()
            if not enemy.reached_end():
                self.enemies.remove(enemy)
                self.event_bus.publish(GameEvent.ENEMY_REACHED_END)
                

    def draw_enemies(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)