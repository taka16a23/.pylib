#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""tbody -- tbody tag

"""
from .html_tag import HtmlTag


class Tbody(HtmlTag):
    """Tbody

    Tbody is a HtmlTag.
    Responsibility:

    HTML の表本体要素 (<tbody>) は、表の一連の行 (<tr> 要素) を内包し、
    その部分が表 (<table>) の本体部分を構成することを表します。

    <tbody> 要素は、親戚である <thead> や <tfoot> と共に有用な意味的情報を提供し、
    画面への表示や印刷ばかりでなく、アクセシビリティ目的にも利用できます。

    コンテンツカテゴリ	なし
    許可されている内容	0 個以上の <tr> 要素
    タグの省略	<table> 要素をグラフィカルに表示するにあたり、<tbody> 要素は必須ではない子要素です。ただし、<table> 要素の子要素として <tr> 要素が存在する場合は tbody を配置してはいけません。
    許可されている親要素	<table> 要素。<tbody> 要素は <caption>, <colgroup>, <thead>, <tfoot> の各要素の後に配置することができます。
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLTableSectionElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='tbody', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# tbody.py ends here
