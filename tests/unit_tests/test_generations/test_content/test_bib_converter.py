"""
Tests for `BibConverter` .
"""

from __future__ import annotations
import pytest
from loguru import logger

from src.generations.content.bib_converter import BibConverter

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


@pytest.fixture(name='bib_string')
def make_bib_string() -> str:
    bibtex_string = """
    @comment{
        This is my example comment.
    }

    @ARTICLE{Cesar2013,
      author = {Jean César},
      title = {An amazing title},
      year = {2013},
      volume = {12},
      pages = {12--23},
      journal = {Nice Journal}
    }

    @inproceedings{Cesar2012,
      author = {Jean César},
      title = {An amazing title},
      booktitle = {Some book title},
      year = {2013},
      volume = {12},
      pages = {12--23},
      journal = {Nice Journal}
    }
    """
    return bibtex_string


def test_bib_converter(
    bib_string: str,
) -> None:
    outputs = BibConverter.convert_bib_string(
        bib_string=bib_string,
        style='pybtex.style.formatting',
        backend='pybtex.backends',
    )
    logger.info(f"Bib Outputs: \n{outputs}")

