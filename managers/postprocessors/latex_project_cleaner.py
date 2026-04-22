"""
Sources:
    https://github.com/yuliu625/Yu-LaTeX-Academic-Automata/postprocessors/latex_project_cleaner.py

References:
    https://github.com/google-research/arxiv-latex-cleaner

Synopsis:
    Clean up latex projext.

Notes:
    使用 arxiv-latex-cleaner 对于待提交的 latex project 进行清理无关内容。

    arxiv-latex-cleaner 的源码主要基于 RE ，因此:
        - 显式优于隐式: 涉及路径相关方法，不要用 macro 进行封装。
        - single file: latex project 尽可能构建得扁平化，不要有复杂依赖关系。

    arxiv-latex-cleaner 被设计为 CLI 调用，当前实现以 subprocess 进行。可以直接以 shell 调用该工具。
"""

from __future__ import annotations
from loguru import logger

import subprocess

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from subprocess import CompletedProcess


class LaTeXProjectCleaner:
    """
    Clean up latex projext via arxiv-latex-cleaner.
    """

    # ==== main method ====
    @staticmethod
    def clean_project(
        project_path: str,
        additional_args: list[str],
    ) -> CompletedProcess[str]:
        """
        Clean up target latex project.

        Args:
            project_path (str): target latex project directory.
            additional_args (list[str]): additional arguments passed to arxiv-latex-cleaner.
                More optional arguments can be seen via:
                ```bash
                arxiv_latex_cleaner --help
                ```

        Returns:
            CompletedProcess[str]: clean up completed process.
        """
        command = [
            'arxiv_latex_cleaner',
        ]
        # input folder
        command.extend([project_path])
        # cli configs
        command.extend(additional_args)
        # clean up
        result = subprocess.run(
            command,
            text=True,
        )
        logger.info(f"Cleaner Result: {result}")
        return result


if __name__ == '__main__':
    # setup and run the cleaner
    LaTeXProjectCleaner.clean_project(
        project_path="./Liu-et-al-paper",
        additional_args=[],
    )

