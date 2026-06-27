"""
Sources:
    https://github.com/yuliu625/Yu-LaTeX-Academic-Automata/blob/main/src/generations/content/bib_converter.py

References:
    https://pybtex.org/

Synopsis:
    Simple bibtex converter.

Notes:
    一些场景下，需要直接对 `.bib` 文件进行处理和输出。
    这个方法使用 `pybtex` 进行简单的处理。

    由于 `pybtex` 没有严格的类型标注，虽然 docstring 很完善，但这个包的 python API 只能简单使用一下。
    更多使用还是直接使用 CLI 。
"""

from __future__ import annotations
from loguru import logger

from pybtex.database import (
    parse_string,
    parse_file,
)
from pybtex.plugin import find_plugin
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class BibConverter:
    """
    Convert bibtex entries via `pybtex` .
    """

    @staticmethod
    def convert_bib_file(
        bib_file_path: str | Path,
        style: str,
        backend: str,
    ) -> str:
        bib_data = parse_file(
            file=bib_file_path,
            bib_format='bibtex',
        )
        style = find_plugin(style, 'plain')()
        backend = find_plugin(backend, 'text')()
        formatted_entries = style.format_entries(bib_data.entries.values())
        lines = [entry.text.render(backend) for entry in formatted_entries]
        final_string = "\n".join(lines)
        logger.debug(f"Bib String: \n{final_string}")
        return final_string

    @staticmethod
    def convert_bib_string(
        bib_string: str,
        style: str,
        backend: str,
    ) -> str:
        bib_data = parse_string(
            value=bib_string,
            bib_format='bibtex',
        )
        style = find_plugin(style, 'plain')()
        backend = find_plugin(backend, 'text')()
        formatted_entries = style.format_entries(bib_data.entries.values())
        lines = [entry.text.render(backend) for entry in formatted_entries]
        final_string = "\n".join(lines)
        logger.debug(f"Bib String: \n{final_string}")
        return final_string

