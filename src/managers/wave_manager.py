from copy import deepcopy
import random

from entities.enemy import Enemy
from events.game_event import GameEvent
from wave_generation.enemy_factory import EnemyFactory
from wave_generation.enemy_type import EnemyType


class WaveManager:
    def __init__(self, game_state, event_bus, wave_defenitions = []) -> None:
        self.game_state = game_state
        self.event_bus = event_bus
        self.wave_defenitions = wave_defenitions
        if not self.wave_defenitions:
            self.generate_waves(5)

        self.active_wave = -1
        self.next_enemy_index = 0
        self.enemies_in_wave = []
        self.spawn_interval = 1.0
        self.spawn_timer = 0

        self.wave_complete_handled = False

    def next_wave(self):
        # increment wave index
        self.active_wave += 1

        # get current wave definition
        wave = self.wave_defenitions[self.active_wave]
        print(wave)
        # reset list
        self.enemies_in_wave = []
        self.spawn_timer = 0
        self.next_enemy_index = 0
        self.wave_complete_handled = False

        # spawn enemies
        for enemy_type, enemy_count in wave:
            for _ in range(enemy_count):
                enemy = EnemyFactory.create(enemy_type, self.game_state.path.pixel_path)
                self.enemies_in_wave.append(enemy)

    def update_wave(self, dt):
        if self.next_enemy_index < len(self.enemies_in_wave):
            self.spawn_timer += dt
            if self.spawn_timer >= self.spawn_interval:
                enemy = self.enemies_in_wave[self.next_enemy_index]
                self.event_bus.publish(GameEvent.ENEMY_SPAWNED, enemy)
                self.next_enemy_index += 1
                self.spawn_timer = 0
        elif self.is_wave_over() and not self.wave_complete_handled:
            print("Wave completed")
            self.wave_complete_handled = True
            self.event_bus.publish(GameEvent.WAVE_COMPLETED, self.active_wave + 1)


    def generate_waves(self, num_of_waves):        
        for i in range(num_of_waves):
            self.wave_defenitions.append(WaveManager.generate_wave_definition(i))

    def is_wave_over(self):
        return self.active_wave != -1 and self.next_enemy_index <= len(self.enemies_in_wave) and not self.game_state.enemy_manager.active_enemies

    @staticmethod
    def generate_wave_definition(wave_number: int):
        """
        Returns a list of tuples (EnemyType, count) representing the wave.
        Higher waves are harder: more enemies and stronger types.
        """
        wave_def = []

        # Base number of enemies for the wave
        base_count = 5
        total_enemies = base_count + wave_number * 2

        # Determine counts for each type
        # EASY decreases over time
        easy_count = max(1, total_enemies - wave_number)  
        # REGULAR increases as waves progress
        regular_count = min(total_enemies - easy_count, wave_number // 2)
        # HEAVY appears every 5 waves
        heavy_count = 1 if wave_number % 5 == 0 else 0

        # Shuffle to make it less predictable
        types = []
        types += [EnemyType.EASY] * easy_count
        types += [EnemyType.REGULAR] * regular_count
        types += [EnemyType.HEAVY] * heavy_count
        random.shuffle(types)

        # Convert to list of (EnemyType, count) tuples
        # Combine duplicates
        counter = {}
        for t in types:
            counter[t] = counter.get(t, 0) + 1

        for enemy_type, count in counter.items():
            wave_def.append((enemy_type, count))

        return wave_def