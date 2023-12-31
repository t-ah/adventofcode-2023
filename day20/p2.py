from abc import abstractmethod
from pathlib import Path
from collections import deque


# step 1: look at the program
# step 2: print stuff
# step 3: calculator
class Module:
    def __init__(self, name: str, targets: list[str]):
        self.name = name
        self.targets = targets

    @abstractmethod
    def pulse(self, high: bool, sender: str):
        ...


class FFModule(Module):
    def pulse(self, high: bool, sender: str):
        if not high:
            self.on = not self.on
            return [(self.name, target, self.on) for target in self.targets]
        return []

    def __init__(self, name: str, targets: list[str]):
        super().__init__(name, targets)
        self.on = False


class ConModule(Module):
    def pulse(self, high: bool, sender: str):
        self.inputs[sender] = high
        no_lows = sum([1 for v in self.inputs.values() if not v]) == 0  # count lows
        self.prev = not no_lows
        return [(self.name, target, self.prev) for target in self.targets]

    def __init__(self, name: str, targets: list[str]):
        super().__init__(name, targets)
        self.inputs = {}
        self.prev = False

    def add_input(self, name: str):
        self.inputs[name] = False


def main():
    for file_name in ["p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            lines = read_input(path)
            solve(lines)


def push(modules, start_pulses, step):
    pulses = deque(start_pulses)
    count = {True: 0, False: 0}
    while pulses:
        sender, target, high = pulses.popleft()
        if sender in ["kv", "jg", "rz", "mr"] and high:
            print(step, sender)
        count[high] += 1
        if target in modules:
            pulses.extend(modules[target].pulse(high, sender))
        else:
            if target == "rx" and not high:
                return True
    return False


def solve(lines: list[str]):
    modules = {}
    bc_targets = []
    for line in lines:
        left, right = line.split(" -> ")
        targets = right.split(", ")
        name = left[1:]
        if left[0] == "%":
            modules[name] = FFModule(name, targets)
        elif left[0] == "&":
            modules[name] = ConModule(name, targets)
        else:
            bc_targets = targets
    for module in modules.values():
        for target in module.targets:
            if target in modules:
                target_module = modules[target]
                if type(target_module) is ConModule:
                    target_module.add_input(module.name)
    for target in bc_targets:
        target_module = modules[target]
        if type(target_module) is ConModule:
            target_module.add_input("broadcaster")
    start_pulses = [("broadcaster", target, False) for target in bc_targets]
    i = 1
    while True:
        if push(modules, start_pulses, i):
            break
        i += 1
    print(i)


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


if __name__ == "__main__":
    main()
