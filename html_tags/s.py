#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""s -- s tag

"""
from .html_tag import HtmlTag


class s(HtmlTag):
    """s

    s is a HtmlTag.
    Responsibility:

    HTML の <s> 要素は取り消し線を引いた文字列を表示します。
    <s> 要素はすでに適切または正確ではなくなった事柄を表現します。
    しかし、文書の修正を示す場合、 <s> 要素は適切ではありません。
    この場合は <del> と <ins> の方が適しているので、こちらを使用してください。

    コンテンツカテゴリ	記述コンテンツまたはフローコンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='s', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# s.py ends here
