from pathlib import Path
import pytest
from assignment_00.B.main import run

TEST_INPUT_COUNT = 3
SCRIPT_FOLDER = Path(__file__).parent.absolute()
FILE_NAME_DIGIT_COUNT = 2


def add_leading_zeros(number: int):
    return f"{number}".zfill(FILE_NAME_DIGIT_COUNT)


TEST_GROUPS = [add_leading_zeros(i + 1) for i in range(TEST_INPUT_COUNT)]


@pytest.mark.parametrize("group_number", TEST_GROUPS)
def test_main(group_number, capsys):
    data_in = (SCRIPT_FOLDER / f"{group_number}.in").read_text().splitlines()

    for line in data_in:
        run(line=line)

    expected = (SCRIPT_FOLDER / f"{group_number}.ans").read_text()
    captured = capsys.readouterr()
    assert expected == captured.out
