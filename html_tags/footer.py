#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""footer -- footer tag

"""
from .html_tag import HtmlTag


class Footer(HtmlTag):
    """Footer

    Footer is a HtmlTag.
    Responsibility:

    HTML の <footer> 要素 は、直近の区分コンテンツまたは
    区分化ルート要素のフッターを表します。
    フッターには通常、そのセクションの著作者に関する情報、
    関連文書へのリンク、著作権情報等を含めます。

    コンテンツカテゴリ	フローコンテンツ, 知覚可能コンテンツ
    許可されている内容	フローコンテンツ。但し、他の <footer> や <header> の子孫がないもの。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素。ただし、 <address>, <header>, 他の <footer> の子孫要素として配置してはならない。
    許可されている ARIA ロール	group, presentation
    DOM インターフェイス	HTMLElement

    使用上のメモ
    セクションの著作者や編集者の連絡先情報は、多くの場合 <footer> 要素内に
    <address> 要素として配置します。
    <footer> 要素は区分コンテンツではありません。
    つまり、この要素が新たなアウトラインを生成することはありません
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='footer', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# footer.py ends here
