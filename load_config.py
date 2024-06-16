from os import listdir, getcwd, chdir, mkdir, path

def last_element(item):
    return item[-1]

def check_file():
    if "soundboard_essential_config.txt" not in listdir(getcwd()):
        with open("soundboard_essential_config.txt", 'w+') as ecf:
            ecf.write(f"""CONFIG_DIRECTORY = {getcwd()}""")
            
    
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
            print("Found config:", i, end="\t")
            config_directories_paths.append(path.join(getcwd(), i))

    return config_directories_paths


def get_sound_file_paths():
    config_dirs = check_config()
    for i in range(len(config_dirs)):
        if config_dirs[i] is not None:
            chdir(config_dirs[i])
            filename = listdir()[0]
            config_dirs[i] = path.join(getcwd(), filename)

    return config_dirs