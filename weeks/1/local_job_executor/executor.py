import json
import typing


class LocalJobExecutor:

    def __init__(self):
        self._jobs: dict[int, list[typing.Callable | tuple | str]] = {}

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print(json.dumps({idx: func_args_state[2] for idx, func_args_state in self._jobs.items()}, indent=2))

    def submit(self, job: typing.Callable, *args) -> None:
        next_id = len(self._jobs)
        self._jobs[next_id] = [job, args, "idle"]

    def start(self) -> None:
        for idx, func_args_state in self._jobs.items():
            try:
                func_args_state[2] = "running"
                func_args_state[0](*func_args_state[1])
            except Exception as e:
                func_args_state[2] = e.args[0]
            else:
                func_args_state[2] = "success"
