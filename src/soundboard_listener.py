from pynput import keyboard
from pydub import AudioSegment
from pydub.playback import play
from load_config import get_sound_file_paths


class SoundBoardListener:
    def __init__(self) -> None:
        self.alive = False
        self.num_key_map = {str(k):k-96 for k in range(96, 106)}
        self.sound_audio_segments = []
        #self.working_path = getcwd()
        #self.numpad_active = False
        self.load_config()
        self.is_playing = False


    def on_press_default(key, message:str="pressed") -> None:
        try:
            print(key.char, message)
        except AttributeError:
            print('EXCEPTION: Special key {0} pressed'.format(
                key))
            

    def on_press_blank(self, key:keyboard.Key) -> None:
        pass


    def on_release_default(self, key:keyboard.Key, message="released") -> None | bool:
        print(key, message)
 
        if key == keyboard.Key.esc:
            # Stop listener
            self.alive = False
            return False
        

    def on_release_blank(key:keyboard.Key) -> None:
        pass


    def on_release_num_pad(self, key:keyboard.Key, debug:bool=False) -> None | bool:
        ki = str(key)[1:-1]
 
        if ki in self.num_key_map.keys() and len(ki)>=2:
            if debug:
                print(self.num_key_map[ki])
            if self.sound_audio_segments[self.num_key_map[ki]] is not None and not self.is_playing: #and self.numpad_active
                self.is_playing = True
                play(self.sound_audio_segments[self.num_key_map[ki]])
                self.is_playing = False

        #if key == keyboard.Key.num_lock:
            #self.numpad_active = not self.numpad_active
            #Thread(target=self.change_power_state, daemon=True).start()
 
        if key == keyboard.Key.esc:
            # Stop listener
            self.alive = False
            return False
        

    def start(self, on_press, on_release) -> None:
        self.alive = True
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            try:
                listener.join()
            except Exception as e:
                print(e)
                print('{0} was pressed'.format(e.args[0]))


    def debug(self) -> None:
        self.start(self.on_press_default, self.on_release_default)


    def validate_path(self, p:str) -> None | AudioSegment:
        print(p)
        if p is not None:
            return AudioSegment.from_file(p)
        else:
            return None
        
    # UNUSED FUNCTION
    def parse_power_config(self, config:str) -> bool:
        config = config.strip()
        print(config, len(config))    
        if config == "1":
            return True
        else:
            return False


    def load_config(self) -> None:
        paths = get_sound_file_paths()
        print(paths)
        self.sound_audio_segments = list(map(self.validate_path, paths))
        #chdir(self.working_path)
        #with open("soundboard_ison.txt", 'r') as sic:
         #   self.numpad_active = self.parse_power_config(sic.read())
          #  print(self.numpad_active)

    # UNUSED FUNCTION
    def change_power_state(self) -> None:
        try:
            with open("soundboard_ison.txt", 'w+') as sic:
                sic.write(str(int(self.numpad_active)))
            print("Power state save SUCCESSFUL")
        except Exception as e:
            print("Power state save FAILED")
            print(e)


if __name__ == "__main__":
    sb = SoundBoardListener()
    sb.start(sb.on_press_blank, sb.on_release_num_pad)