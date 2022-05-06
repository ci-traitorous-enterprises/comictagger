import pathlib

import pytest
from filenames import rnames

from comicapi.genericmetadata import md_test
from comictaggerlib.filerenamer import FileRenamer


@pytest.mark.parametrize("template, move, platform, expected", rnames)
def test_rename(template, platform, move, expected):
    fr = FileRenamer(md_test, platform=platform)
    fr.move = move
    fr.set_template(template)
    assert str(pathlib.PureWindowsPath(fr.determine_name(".cbz"))) == str(pathlib.PureWindowsPath(expected))