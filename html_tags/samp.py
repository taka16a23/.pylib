#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""samp -- samp tag

"""
from .html_tag import HtmlTag


class Samp(HtmlTag):
    """Samp

    Samp is a HtmlTag.
    Responsibility:

    HTML のサンプル要素 (<samp>) は、コンピュータープログラムからの
    サンプル出力を表す行内文字列を含めるために使用されます。
    内容は普通、ブラウザーの既定の等幅フォント（Courier や Lucida Console など）
    を使用して表示されます。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement

    使用上のメモ
    CSS 規則を定義して <samp> 要素におけるブラウザーの
    既定フォントを上書きすることができます。
    ただし、ブラウザの設定が指定したCSSよりも優先される可能性があります。

    既定のフォントを上書きする CSS は次のようになります。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='samp', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# samp.py ends here
