"""
Sources:
    https://github.com/yuliu625/Yu-LaTeX-Academic-Automata/generators/table_conversion/df_converter.py

References:
    https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html

Synopsis:
    使用 pandas 的 Styler 构造 latex 表格。

Notes:
    约定对于基于 xlsx 格式的结果，进行自动化转换。

    基于 Styler 的方法优于直接使用 to_latex 方法。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd
from pathlib import Path

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

    @staticmethod
    def convert_and_save_df(
        df: pd.DataFrame,
        precision: int,
        label: str,
        caption: str,
        position: str,
        result_path: str,
    ) -> str:
        # path processing
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        # convert df
        latex_output = DataFrameConverter.convert_df(
            df=df,
            precision=precision,
            label=label,
            caption=caption,
            position=position,
        )
        # save latex table code
        result_path.write_text(latex_output, encoding='utf-8')
        logger.success(f"Saved latex table code to {result_path}")
        return latex_output

