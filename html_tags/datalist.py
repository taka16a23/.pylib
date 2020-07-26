#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""datalist -- datalist tag

"""
from .html_tag import HtmlTag


class Datalist(HtmlTag):
    """Datalist

    Datalist is a HtmlTag.
    Responsibility:

    HTML の <datalist> 要素は、他のコントロールで利用可能な値を表現する
    一連の <option> 要素を含みます。

    コンテンツカテゴリ	フローコンテンツ、記述コンテンツ
    許可されている内容	記述コンテンツ、または 0 個以上の <option> 要素のどちらか
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLDataListElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='datalist', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# datalist.py ends here
