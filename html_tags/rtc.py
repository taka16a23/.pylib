#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rtc -- rtc tag

"""
from .html_tag import HtmlTag


class Rtc(HtmlTag):
    """Rtc

    Rtc is a HtmlTag.
    Responsibility:

    HTML のルビ文字列コンテナー (<rtc>) 要素は、 <ruby> 要素内で使用する <rb>
    要素にルビで与える文字列の、意味を表す注釈を包含します。
    <rb> 要素は発音の注釈 (<rt>) と意味の注釈 (<rtc>) の両方を持つことができます。

    コンテンツカテゴリ	なし
    許可されている内容	記述コンテンツまたは <rt> 要素
    タグの省略	直後に <rb>, <rtc>, <rt> 要素の開始タグがある、または親要素の終了タグがある場合は、この要素の終了タグを省略可能。
    許可されている親要素	<ruby> 要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='rtc', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rtc.py ends here
