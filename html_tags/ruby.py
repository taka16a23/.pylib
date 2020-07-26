#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""ruby -- ruby tag

"""
from .html_tag import HtmlTag


class Ruby(HtmlTag):
    """Ruby

    Ruby is a HtmlTag.
    Responsibility:

    HTML の <ruby> 要素は、ルビ文字による注釈を表します。
    ルビ文字による注釈は、東アジアの文字の発音 (振り仮名) を表すためのものです。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='ruby', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ruby.py ends here
