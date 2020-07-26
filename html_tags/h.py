#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""h -- h tag

"""
from .html_tag import HtmlTag


class h(HtmlTag):
    """h

    h is a HtmlTag.
    Responsibility:

    コンテンツカテゴリ	フローコンテンツ, 見出しコンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素。 <hgroup> は非推奨になったので、見出し要素をその子要素として使用しないでください。
    許可されている ARIA ロール	tab, presentation
    DOM インターフェイス

    使用上の注意
    見出し情報はユーザーエージェントによって使用される可能性があります。
    例えば、文書の目次を自動的に作成するなどです。
    フォントサイズを縮小する目的で低いレベルの見出しを使用しないでください。
    代わりに CSS の font-size を使用してください。
    見出しレベルを飛ばすことは避けてください。
    常に <h1> から始め、次に <h2>、以下も同様にしてください。
    1つのページで <h1> を2回以上使用することは避けてください。
    詳しくはDefining sections in HTML5
    ドキュメントのセクションとアウトラインを参照してください。
    """
    def __init__(self, num, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='h' + num, tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# h.py ends here
