#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""table -- table tag

"""
from .html_tag import HtmlTag


class Table(HtmlTag):
    """Table

    Table is a HtmlTag.
    Responsibility:

    HTML の <table> 要素は表形式のデータ、つまり、
    行と列の組み合わせによるセルに含まれたデータによる二次元の表で表現される情報です。

    コンテンツカテゴリ	フローコンテンツ
    許可されている内容
    以下の順となる。
    任意の1個の <caption> 要素
    0個以上の <colgroup> 要素
    任意の1個の <thead> 要素
    次の2つの選択肢から1つ:
    0個以上の <tbody> 要素
    1個以上の <tr> 要素
    任意の1個の <tfoot> 要素
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素。
    許可されている ARIA ロール	全て
    DOM インターフェイス	HTMLTableElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='table', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# table.py ends here
