from datetime import datetime
from functools import cache

from obsws_python import ReqClient, EventClient

from stream_manager.settings import env


class OBS:
    def __init__(self):
        self.__connection = None
        self.__events = None
        self.__running = False
        self.__log = [{
            "timestamp": datetime.utcnow(),
            "type": "START",
            "event": {}
        }]

    @property
    @cache
    def _config(self) -> dict:
        _conf = env.config.get("connection", {})
        return dict(
            host=_conf["host"],
            port=_conf.get("port", 4455),
            password=_conf.get("password", None)
        )

    @property
    def client(self) -> ReqClient:
        if not self.__connection:
            self.__connection = ReqClient(**self._config)
        return self.__connection

    @property
    def events(self) -> EventClient:
        if not self.__events:
            self.__events = EventClient(**self._config)
        return self.__events

    @property
    def running(self):
        return self.__running and self.events.callback.get()

    def register(self, functions: list[callable]) -> None:
        functions = functions or [
            self.on_current_program_scene_changed,
            self.on_input_mute_state_changed,
            self.on_exit_started,
            self.on_record_state_changed
        ]
        self.events.callback.register(functions)
        self.__running = bool(self.events.callback.get()) and bool(functions)

    def add(self, event: dict) -> None:
        _ts = datetime.utcnow()
        self.__log.setdefault()
        return None


    def on_current_program_scene_changed(self, data) -> None:
        self.add({
            "scene": data.scene_name
        })

    def on_input_mute_state_changed(self, data) -> None:
        self.add({
            "scene": data.scene_name
        })

    def on_exit_started(self, data: dict) -> None:
        self.add({
            "scene": data.scene_name
        })

    def on_record_state_changed(self, data: dict) -> None:
        return None