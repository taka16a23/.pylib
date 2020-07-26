#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""figcaption -- figcaption tag

"""
from .html_tag import HtmlTag


class FigCaption(HtmlTag):
    """FigCaption

    FigCaption is a HtmlTag.
    Responsibility:

    HTML の <figcaption> 要素または図キャプション要素は、
    親の <figure> 要素内にあるその他のコンテンツを説明する
    キャプションや凡例を表します。

    コンテンツカテゴリ	なし
    許可されている内容	フローコンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	<figure> 要素。 <figcaption> 要素は最初または最後の子要素でなければなりません。
    許可されている ARIA ロール	group、 presentation
    DOM インターフェイス
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='figcaption', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# figcaption.py ends here
