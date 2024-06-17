from os import listdir, getcwd, chdir, mkdir, path

def last_element(item):
    return item[-1]

def check_file():
    if "soundboard_essential_config.txt" not in listdir(getcwd()):
        with open("soundboard_essential_config.txt", 'w+') as ecf:
            ecf.write(f"""CONFIG_DIRECTORY = {getcwd()}""")

    if "soundboard_ison.txt" not in listdir(getcwd()):
        with open("soundboard_ison.txt", 'w+') as sic:
            sic.write("0")
            
    
    with open("soundboard_essential_config.txt", 'r') as ecf:
        ecf_config_vars = list(map(last_element, map(str.split,ecf.readlines())))
        print("CONFIG_DIRECTORY: ", ecf_config_vars)
        return ecf_config_vars

def check_config():
    config_dir = check_file()[0]
    chdir(config_dir)

    config_dir_content = listdir()
    config_directories_paths = []

    for i in [str(n) for n in range(0,10)]:
        if i not in config_dir_content:
            print("EXCEPTION: Config directory for key", i, "not found")
            mkdir(i)
            config_directories_paths.append(None)
        else:
            print("Found config dir:", i, sep="\t")
            config_directories_paths.append(path.join(getcwd(), i))

    return config_directories_paths


def get_sound_file_paths():
    config_dirs = check_config()
    for i in range(len(config_dirs)):
        if config_dirs[i] is not None:
            chdir(config_dirs[i])
            if len(listdir()) > 0:
                filename = listdir()[0]
                ext = filename.split(".")[-1]
                if ext == "mp3" or ext == "mp4" or ext == "wav":
                    config_dirs[i] = path.join(getcwd(), filename)
                    continue
            
            config_dirs[i] = None

    return config_dirs