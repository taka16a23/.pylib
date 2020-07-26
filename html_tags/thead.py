#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""thead -- thead tag

"""
from .html_tag import HtmlTag


class THead(HtmlTag):
    """THead

    THead is a HtmlTag.
    Responsibility:

    HTML の <thead> 要素は、表の列の見出しを定義する行のセットを定義します。

    コンテンツカテゴリ	なし
    許可されている内容	0 個以上の <tr> 要素
    タグの省略	開始タグは必須。 <thead> 要素の直後に <tbody> 要素または <tfoot> 要素がある場合は終了タグを省略可能。
    許可されている親要素	<table> 要素。 <thead> は (暗黙的に定義されるものであっても) <caption> 要素や <colgroup> 要素の後方かつ <tbody>, <tfoot>, <tr> の各要素の前方に配置しなければなりません。
    暗黙の ARIA ロール	rowgroup
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLTableSectionElement

    属性
    この要素にはグローバル属性があります。

    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='thead', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# thead.py ends here
