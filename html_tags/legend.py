#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""legend -- legend tag

"""
from .html_tag import HtmlTag


class Legend(HtmlTag):
    """Legend

    Legend is a HtmlTag.
    Responsibility:

    HTML の <legend> 要素は、その親要素である <fieldset> の内容のキャプションを表します。

    コンテンツカテゴリ	なし
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	<fieldset> 要素。<legend> 要素は <fieldset> の最初の子要素として配置しなくてはならない。
    許可されている ARIA ロール	なし
    DOM インターフェイス
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='legend', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# legend.py ends here
