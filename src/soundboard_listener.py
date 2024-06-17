from pynput import keyboard
from pydub import AudioSegment
from pydub.playback import play
from load_config import get_sound_file_paths
from os import getcwd, chdir


class SoundBoardListener:
    def __init__(self) -> None:
        self.alive = False
        self.num_key_map = {str(k):k-96 for k in range(96, 106)}
        self.sound_audio_segments = []
        self.load_config()
        self.numpad_active = False


    def on_press_default(key, message="pressed"):
        try:
            print(key.char, message)
        except AttributeError:
            print('EXCEPTION: Special key {0} pressed'.format(
                key))
            

    def on_press_blank(self, key):
        pass


    def on_release_default(self, key, message="released"):
        print(key, message)
 
        if key == keyboard.Key.esc:
            # Stop listener
            self.alive = False
            return False
        

    def on_release_blank(key):
        pass


    def on_release_num_pad(self, key, debug=False):
        ki = str(key)[1:-1]
 
        if ki in self.num_key_map.keys() and len(ki)>=2:
            if debug:
                print(self.num_key_map[ki])
            if self.sound_audio_segments[self.num_key_map[ki]] is not None and self.numpad_active:
                play(self.sound_audio_segments[self.num_key_map[ki]])
 
        if key == keyboard.Key.esc:
            # Stop listener
            self.alive = False
            return False
        
        if key == keyboard.Key.num_lock:
            self.numpad_active = not self.numpad_active
        

    def start(self, on_press, on_release):
        self.alive = True
        
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            try:
                listener.join()
            except Exception as e:
                print(e)
                print('{0} was pressed'.format(e.args[0]))


    def debug(self):
        self.start(self.on_press_default, self.on_release_default)


    def validate_path(self, p:str):
        print(p)
        if p is not None:
            return AudioSegment.from_file(p)
        else:
            return None


    def load_config(self):
        paths = get_sound_file_paths()
        print(paths)
        self.sound_audio_segments = list(map(self.validate_path, paths))



if __name__ == "__main__":
    sb = SoundBoardListener()
    sb.start(sb.on_press_blank, sb.on_release_num_pad)