#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""small -- small tag

"""
from .html_tag import HtmlTag


class Small(HtmlTag):
    """Small

    Small is a HtmlTag.
    Responsibility:

    HTML の <small> 要素は、表示上のスタイルとは関係なく、
    著作権表示や法的表記のような、注釈や小さく表示される文を表します。
    既定では、 small から x-small のように、一段階小さいフォントで
    テキストが表示されます。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始タグと終了タグの両方が必要です。
    許可されている親要素	記述コンテンツを受け入れるすべての要素、またはフローコンテンツを受け入れるすべての要素。
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='small', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# small.py ends here
