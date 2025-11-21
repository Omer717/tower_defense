from entities.enemy import Enemy
from events.event_bus import EventBus
from events.game_event import GameEvent


class EnemyManager:
    def __init__(self, game_state, event_bus: EventBus):
        self.event_bus = event_bus
        self.game_state = game_state

        self.active_enemies = []

        event_bus.subscribe(GameEvent.ENEMY_SPAWNED, self.add_enemy)

    def add_enemy(self, enemy):
        self.active_enemies.append(enemy)

    def update_enemies(self, dt):
        # --- Update all enemies ---
        for enemy in self.active_enemies[:]:
            enemy.update(dt)

            # Enemy reached end
            if enemy.reached_end():
                print("enemy reached end")
                self.active_enemies.remove(enemy)
                self.event_bus.publish(GameEvent.ENEMY_REACHED_END, enemy)
                continue

            # Enemy died
            if enemy.health <= 0:
                print("enemy died")
                self.active_enemies.remove(enemy)
                self.event_bus.publish(GameEvent.ENEMY_KILLED, enemy)

    def draw_enemies(self, screen):
        for enemy in self.active_enemies:
            enemy.draw(screen)