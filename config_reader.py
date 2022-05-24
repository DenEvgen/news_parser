
def read_config() -> dict:
    list_config = list()
    config = dict()
    with open('config.txt', 'r') as file:
        for line in file:
            if line.isspace():
                continue
            line = ''.join(line.split())
            list_config.append(line.split(":"))
        for conf in list_config:
            key = conf[0]
            value = conf[1]
            config[key] = value
    return config
