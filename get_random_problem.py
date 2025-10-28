import ast
import logging
import random
from dataclasses import dataclass
from pathlib import Path

logging.basicConfig()
logger = logging.getLogger(__name__)

PY = ".py"
NON_SOLUTION_FILES = ["helpers.py"]


@dataclass
class Problem:
    name: str
    topic: str
    path: Path

    def __str__(self) -> str:
        return f"Problem {self.name} ({self.topic})"


def extract_problem_description(filepath: Path) -> str | None:
    if not filepath.exists():
        logger.error(f"{filepath} does not exist")
        return None
    with filepath.open() as f:
        module = ast.parse(f.read())
        docstring = ast.get_docstring(module)
        if not docstring:
            logger.error(f"Failed to get docstring from {filepath}")
        return docstring


def get_problem_name_from_file_name(filename: str) -> str:
    problem_name_full = filename.split("_")
    number, name = problem_name_full[0], problem_name_full[1:]
    return number + ". " + " ".join(w.capitalize() for w in name)


def get_topic_name_from_dir_name(dir_name: str) -> str:
    return " ".join(w.upper() for w in dir_name.split("_"))


def get_all_solved_problems() -> list[Problem]:
    root_dir = Path(".")
    topic_dirs = [d for d in root_dir.iterdir() if d.is_dir() and not d.name.startswith((".", "_"))]
    problems = []

    for td in topic_dirs:
        for file in td.iterdir():
            if file.suffix != PY or file.name in NON_SOLUTION_FILES:
                continue
            problem = Problem(
                name=get_problem_name_from_file_name(file.stem),
                topic=get_topic_name_from_dir_name(td.name),
                path=file,
            )
            problems.append(problem)

    return problems


if __name__ == "__main__":
    problems = get_all_solved_problems()
    random_problem = problems[random.randint(0, len(problems))]
    problem_description = extract_problem_description(random_problem.path)
    if not problem_description:
        raise SystemExit("Error while choosing a random problem to solve.")

    print(f"{random_problem.topic.capitalize()}:\n\n{problem_description}")
