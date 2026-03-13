"""
Sources:
    https://github.com/yuliu625/Yu-LaTeX-Chore-Master/data_table_conversion/df_converter.py

References:
    https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html

Synopsis:
    使用 pandas 的 Styler 构造 latex 表格。

Notes:
    约定对于基于 xlsx 格式的结果，进行自动化转换。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class DataFrameConverter:
    @staticmethod
    def convert_df(
        df: pd.DataFrame,
        precision: int,
        label: str,
        caption: str,
        position: str,
    ) -> str:
        latex_output = (
            df.style
            .format(
                precision=precision,  # 全局有效数字位数。
            )
            .format_index(
                escape='latex',  # 转义特殊字符。
            )
            .to_latex(
                label=label,
                caption=caption,
                position=position,
                # hrules=True,
                # clines='',
            )
        )
        logger.info(f"\nLaTeX output:\n{latex_output}")
        return latex_output

