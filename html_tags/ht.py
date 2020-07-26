#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""ht -- ht tag

"""
from .html_tag import HtmlTag


class HR(HtmlTag):
    """HR

    HR is a HtmlTag.
    Responsibility:

    HTML の <hr> 要素は、段落レベルの要素間において、
    テーマの意味的な区切りを表します。
    例えば、話の場面の切り替えや、節内での話題の転換などです。

    以前はこれは水平の区切り線として定義されていました。
    現在でもブラウザーでは水平線として表示されますが、
    この要素は表示論的な用語ではなく意味論的な用語で定義されましたので、
    水平線を引きたいのであれば、適切な CSS を使用して行うようにしてください。

    コンテンツカテゴリー	フローコンテンツ
    許可されている内容	なし。これは空要素です。
    タグの省略	開始タグは必須。終了タグを記述してはならない。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    許可されている ARIA ロール	presentation
    DOM インターフェイス	HTMLHRElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='hr', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ht.py ends here
