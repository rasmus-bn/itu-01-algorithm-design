from pathlib import Path
import pytest
from assignment_01.A.main import run

TEST_INPUT_COUNT = 10
SCRIPT_FOLDER = Path(__file__).parent.absolute()
TEST_GROUPS = [i + 1 for i in range(TEST_INPUT_COUNT)]
FILE_NAME_DIGIT_COUNT = 2


def add_leading_zeros(number: int):
    return f"{number}".zfill(FILE_NAME_DIGIT_COUNT)


@pytest.mark.parametrize("group_number", TEST_GROUPS)
def test_main(group_number, capsys):
    data_in = (
        (SCRIPT_FOLDER / f"{add_leading_zeros(group_number)}.in")
        .read_text()
        .splitlines()
    )

    run(input=data_in)

    expected = (SCRIPT_FOLDER / f"{add_leading_zeros(group_number)}.ans").read_text()
    captured = capsys.readouterr()
    assert expected == captured.out
