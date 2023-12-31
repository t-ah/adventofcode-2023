from pathlib import Path
import math


class Workflow:
    def __init__(self, s: str) -> None:
        self.id, rest = s.split("{", 1)
        self.conditions = rest[:-1].split(",")


def main():
    for file_name in ["p2-test.txt", "p2-input.txt"]:
        path = Path(__file__).parent / file_name
        if path.is_file():
            parts = read_input(path)
            solve([p.split("\n") for p in parts])


def solve(parts: list[list[str]]):
    workflows = {w.id: w for w in [Workflow(w) for w in parts[0]]}
    print(all_ratings(workflows["in"].conditions, {k: (1, 4000) for k in list("xmas")}, workflows))


def all_ratings(conditions, bounds, workflows):
    condition = conditions[0]
    if condition == "A":
        return count(bounds)
    if condition == "R":
        return 0
    if not ":" in condition:
        return all_ratings(workflows[condition].conditions, bounds, workflows)
    condition, target = condition.split(":", 1)
    k = condition[0]
    comp_value = int(condition[2:])
    lower, upper = bounds[k]
    if condition[1] == "<":
        if lower >= comp_value: # condition cannot apply, continue with the next
            return all_ratings(conditions[1:], bounds, workflows)
        bounds_apply = new_bounds(bounds, k, lower, min(upper, comp_value - 1))
        bounds_not_apply = new_bounds(bounds, k, comp_value, upper)
    else:
        if upper <= comp_value: # condition cannot apply, continue with the next
            return all_ratings(conditions[1:], bounds, workflows)
        bounds_apply = new_bounds(bounds, k, max(lower, comp_value + 1), upper)
        bounds_not_apply = new_bounds(bounds, k, lower, comp_value)
    if target == "A":
        return count(bounds_apply) + all_ratings(conditions[1:], bounds_not_apply, workflows)
    if target == "R":
        return all_ratings(conditions[1:], bounds_not_apply, workflows)
    return all_ratings(workflows[target].conditions, bounds_apply, workflows) + all_ratings(conditions[1:], bounds_not_apply, workflows)


def new_bounds(old_bounds, k, lower, upper):
    new_bounds = {key: val for key, val in old_bounds.items()}
    new_bounds[k] = (lower, upper)
    return new_bounds


def count(bounds):
    return math.prod([y - x + 1 for (x, y) in bounds.values()])


def read_input(path: Path) -> list[str]:
    with open(path, "r") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
