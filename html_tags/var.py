#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""var -- var tag

"""
from .html_tag import HtmlTag


class Var(HtmlTag):
    """Var

    Var is a HtmlTag.
    Responsibility:

    HTML の変数要素 (<var>) は、数式やプログラムコード内の変数の名前を表します。
    挙動はブラウザーに依存しますが、通常は現在のフォントの斜体を使って表示されます。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始タグと終了タグの両方が必要です。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='var', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# var.py ends here
