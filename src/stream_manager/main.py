import time
from stream_manager.obj.connections import OBS

def run() -> None:
    """
    the main loop
    :return: None
    """
    obs = OBS()
    obs.register()
    while obs.running:
        time.sleep(0.1)


if __name__ == "__main__":
    run()
