#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""data -- data tag

"""
from .html_tag import HtmlTag


class Data(HtmlTag):
    """Data

    Data is a HtmlTag.
    Responsibility:

    HTML の <data> 要素は、与えられたコンテンツの機械可読な翻訳にリンクします。
    コンテンツが時刻または日付に関連するものであれば、
    <time> 要素を使用する必要があります。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLDataElement

    value
    この属性は要素の内容を機械可読な形式で指定します。

    例
    以下の例は商品名を表示しますが、それぞれの商品名に商品番号も結びつけます。

    <p>新製品</p>
    <ul>
      <li><data value="398">ミニケチャップ</data></li>
      <li><data value="399">ジャンボケチャップ</data></li>
      <li><data value="400">メガジャンボケチャップ</data></li>
    </ul>
    """
    class AttributeNames(HtmlTag.AttributeNames):
        """AttributeNames

        AttributeNames is a HtmlTag.AttributeNames.
        Responsibility:

        value
        この属性は要素の内容を機械可読な形式で指定します。
        """
        VALUE = 'value'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='value', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# data.py ends here
