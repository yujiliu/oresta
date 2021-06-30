import orest_core


if __name__ == "__main__":
    orest_core


try:
    with open('TEMP/config', 'r') as config:
        username = config.readline[11:]
except FileNotFoundError:
    username = ''
