import pygame
from src.Constants import Constants as c


class AudioController:
    """Controlador para gestionar audio, música y efectos de sonido del juego"""

    def __init__(self):
        self.music_volume = 0.5
        self.sound_volume = 0.7
        self.is_music_playing = False
        self.sounds = {}

        try:
            pygame.mixer.music.load(str(c.SOUNDTRACK_PATH))
            print("Música cargada correctamente")
        except pygame.error as e:
            print(f"Error cargando música: {e}")

        # Cargar efectos de sonido
        self._load_sound_effects()

    def _load_sound_effects(self):
        """Carga todos los efectos de sonido definidos en Constants"""
        sound_files = {
            'rotate': c.SOUND_ROTATE,
            'move': c.SOUND_MOVE,
            'drop': c.SOUND_DROP,
            'clear': c.SOUND_CLEAR,
            'gameover': c.SOUND_GAMEOVER,
        }

        for name, path in sound_files.items():
            try:
                self.sounds[name] = pygame.mixer.Sound(str(path))
                self.sounds[name].set_volume(self.sound_volume)
                print(f"Sonido {name} cargado correctamente")
            except pygame.error as e:
                print(f"Error cargando sonido {name}: {e}")
                # Crear un sonido vacío para evitar errores
                self.sounds[name] = pygame.mixer.Sound(buffer=bytearray())

    def play_sound(self, sound_name):
        """Reproduce un efecto de sonido por su nombre"""
        if sound_name in self.sounds:
            self.sounds[sound_name].play()
        else:
            print(f"Sonido '{sound_name}' no encontrado")

    def play_music(self, loops=-1):
        """Reproduce la música en bucle"""
        try:
            pygame.mixer.music.set_volume(self.music_volume)
            pygame.mixer.music.play(loops)
            self.is_music_playing = True
        except pygame.error as e:
            print(f"Error reproduciendo música: {e}")

    def stop_music(self):
        """Detiene la música"""
        pygame.mixer.music.stop()
        self.is_music_playing = False

    def pause_music(self):
        """Pausa la música"""
        pygame.mixer.music.pause()
        self.is_music_playing = False

    def unpause_music(self):
        """Reanuda la música"""
        pygame.mixer.music.unpause()
        self.is_music_playing = True

    def set_music_volume(self, volume):
        """Establece el volumen de la música (0.0 a 1.0)"""
        self.music_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.music_volume)

    def set_sound_volume(self, volume):
        """Establece el volumen de los efectos de sonido (0.0 a 1.0)"""
        self.sound_volume = max(0.0, min(1.0, volume))
        for sound in self.sounds.values():
            sound.set_volume(self.sound_volume)

    def toggle_music(self):
        """Alterna entre play/pause de la música"""
        if self.is_music_playing:
            self.pause_music()
        else:
            self.unpause_music()
