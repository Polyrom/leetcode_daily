import os
import re
from dataclasses import dataclass
from enum import Enum


class Colors(str, Enum):
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"


def color_text(text: str, ansi_color: str) -> str:
    return f"{ansi_color}{text}{Colors.RESET.value}"


class Prompts:
    FILENAME = "Filename: "
    FILE_LOCATION = "File location: "
    PROBLEM_LINK = "Link to problem: "
    PROBLEM_DESC = "Problem description (type STOP and hit Enter when you're done): "
    LEETCODE_FUNC_DECL = "Function declaration line from LeetCode: "
    IS_TEST_GENERATED = "Should we generate tests (y/n)? "


IMPORT_DATACLASS = "from dataclasses import dataclass"


@dataclass
class LeetcodeProblemParams:
    filename: str
    location: str
    url: str
    desc: str
    func_decl: str
    is_test_generated: bool


@dataclass
class FunctionParam:
    name: str
    type_hint: str


@dataclass
class FunctionProps:
    name: str
    params: list[FunctionParam]
    return_type_hint: str


class LeetcodeProblemTemplate:
    def __init__(self, params: LeetcodeProblemParams) -> None:
        self.params = params

    @staticmethod
    def _extract_params(params_raw: list[str]) -> list[FunctionParam]:
        params = []
        for pr in params_raw:
            if pr == "self":
                continue
            name, type_hint = tuple(pr.strip().split(":"))
            if "Optional" in type_hint:
                opening_idx = type_hint.find("[")
                closing_idx = type_hint.find("]")
                actual_type = type_hint[opening_idx + 1 : closing_idx]
                type_hint = f"{actual_type} | None"
            else:
                type_hint = type_hint.lower().strip()
            params.append(FunctionParam(name=name.strip(), type_hint=type_hint))
        return params

    @staticmethod
    def camel_to_snake(name: str) -> str:
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
        return s2.lower()

    def _extract_func_props(self) -> FunctionProps:
        f_as_in_def_idx = self.params.func_decl.find("f")
        opening_bracket_idx = self.params.func_decl.find("(")
        closing_bracket_idx = self.params.func_decl.find(")")
        arrow_idx = self.params.func_decl.find(">")

        func_name_raw = self.params.func_decl[f_as_in_def_idx + 2 : opening_bracket_idx]
        func_name = self.camel_to_snake(func_name_raw)
        func_params = self._extract_params(
            self.params.func_decl[opening_bracket_idx + 1 : closing_bracket_idx].split(","),
        )
        return_type_hint = self.params.func_decl[arrow_idx + 2 : -1].strip()
        return FunctionProps(
            name=func_name,
            params=func_params,
            return_type_hint=return_type_hint.lower(),
        )

    @staticmethod
    def _list_func_params_for_tc_def(func_params: list[FunctionParam]) -> str:
        return "\n".join([f"{fp.name}: {fp.type_hint}" for fp in func_params])

    @staticmethod
    def _list_func_params_for_tc_call(func_params: list[FunctionParam]) -> str:
        return ", ".join([f"tc.{fp.name}" for fp in func_params])

    def _generate_test_case_part(self, func_props: FunctionProps) -> str:
        return f"""
if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        {self._list_func_params_for_tc_def(func_props.params)}
        want: {func_props.return_type_hint}

    ASSERTION_ERR_FMT = "test case '{{name}}': want={{want}}, got={{got}}"

    test_cases = [
        TestCase(),
    ]
    for tc in test_cases:
        got = {func_props.name}({self._list_func_params_for_tc_call(func_props.params)})
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
        """

    def generate(self) -> None:
        func_props = self._extract_func_props()
        test_case_part = self._generate_test_case_part(func_props)
        file_contents = (
            f'"""\n{self.params.url}\n\n{self.params.desc}\n"""\n\n'
            f"{IMPORT_DATACLASS}\n\n\n"
            f"def {func_props.name}({', '.join([p.name + ': ' + p.type_hint for p in func_props.params])}) "
            f"-> {func_props.return_type_hint}:\n    pass\n\n"
            f"{test_case_part}\n"
        )
        filepath = os.path.join(self.params.location, self.params.filename + ".py")
        with open(filepath, "w") as f:
            f.write(file_contents)
        print(f"File {filepath} generated!")


if __name__ == "__main__":
    filename = input(color_text(Prompts.FILENAME, Colors.RED.value)).strip()
    filepath = input(color_text(Prompts.FILE_LOCATION, Colors.RED.value)).strip()
    url = input(color_text(Prompts.PROBLEM_LINK, Colors.RED.value)).strip()

    print(color_text(Prompts.PROBLEM_DESC, Colors.RED.value))
    desc = []
    while True:
        data = input().strip()
        if data.lower() == "stop":
            break
        desc.append(data)
    desc = "\n".join(desc)

    func_decl = input(color_text(Prompts.LEETCODE_FUNC_DECL, Colors.RED.value)).strip()
    is_test_generated = input(color_text(Prompts.IS_TEST_GENERATED, Colors.RED.value)).strip()
    is_test_generated = is_test_generated.strip() in ("y", "yes")

    params = LeetcodeProblemParams(
        filename=filename,
        location=filepath,
        url=url,
        desc=desc,
        func_decl=func_decl,
        is_test_generated=is_test_generated,
    )
    template = LeetcodeProblemTemplate(params=params)
    template.generate()
