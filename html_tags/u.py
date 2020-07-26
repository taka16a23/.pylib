#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""u -- u tag

"""
from .html_tag import HtmlTag


class u(HtmlTag):
    """u

    u is a HtmlTag.
    Responsibility:

    HTML の非言語的注釈要素 (<u>) は、非言語的に注釈があることを示す方法で
    表示する行内テキストの区間を示します。
    これは既定で単純な実線の下線として表示されますが、
    CSS を使用して変更することもできます。

    <u> を使用するのがどのような場合に適切で、どのような場合に適切でないのかについての詳細は、使用上のメモを参照してください。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='u', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# u.py ends here
