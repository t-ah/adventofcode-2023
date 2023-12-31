from pathlib import Path
import re


class Condition:
    def __init__(self, s: str) -> None:
        parts = s.split(":")
        if len(parts) > 1:
            self.target = parts[1]
            cond = parts[0]
            if cond[1] == ">":
                self.applies = lambda rating: rating[cond[0]] > int(cond[2:])
            else:
                self.applies = lambda rating: rating[cond[0]] < int(cond[2:])
        else:
            self.target = parts[0]
            self.applies = lambda _: True


class Workflow:
    def __init__(self, s: str) -> None:
        self.id, rest = s.split("{", 1)
        self.conditions = [Condition(s) for s in rest[:-1].split(",")]


def main():
    for file_name in ["p1-test.txt", "p1-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            parts = read_input(path)
            solve([p.split("\n") for p in parts])


def solve(parts: list[list[str]]):
    _workflows, _ratings = parts
    _workflows = [Workflow(w) for w in _workflows]
    ratings = [{r[0]: int(r[1]) for r in re.findall(r'(\w+)=(\d+)', rating)} for rating in _ratings]
    workflows = {w.id: w for w in _workflows}
    accepted_ratings = [r for r in ratings if accepted(r, workflows)]
    print(sum([sum(r.values()) for r in accepted_ratings]))


def accepted(rating, workflows):
    next_workflow = workflows["in"]
    while next_workflow:
        workflow = next_workflow
        for condition in workflow.conditions:
            if condition.applies(rating):
                target = condition.target
                if target == "A":
                    return True
                if target == "R":
                    return False
                next_workflow = workflows[target]
                break


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
