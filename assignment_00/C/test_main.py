from pathlib import Path
import pytest
from assignment_00.C.main import CityCounter

TEST_INPUT_COUNT = 2
SCRIPT_FOLDER = Path(__file__).parent.absolute()
TEST_FILE_NAME_DIGIT_COUNT = 2
TEST_FILE_NAME_PREFIX = "everywhere-"


def add_leading_zeros(number: int):
    return f"{number}".zfill(TEST_FILE_NAME_DIGIT_COUNT)


TEST_GROUPS = [
    f"{TEST_FILE_NAME_PREFIX}{add_leading_zeros(i + 1)}"
    for i in range(TEST_INPUT_COUNT)
]


@pytest.mark.parametrize("group_number", TEST_GROUPS)
def test_main(group_number, capsys):
    data_in = (SCRIPT_FOLDER / f"{group_number}.in").read_text().splitlines()

    cc = CityCounter()
    for line in data_in:
        cc.run(line=line)
    cc.print()

    expected = (SCRIPT_FOLDER / f"{group_number}.ans").read_text()
    captured = capsys.readouterr()
    assert expected == captured.out
