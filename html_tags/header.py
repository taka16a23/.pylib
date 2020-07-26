#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""header -- header tag

"""
from .html_tag import HtmlTag


class Header(HtmlTag):
    """Header

    Header is a HtmlTag.
    Responsibility:

    HTML の <header> 要素は、導入的なコンテンツ、
    ふつうは導入部やナビゲーション等のグループを表します。
    見出し要素だけでなく、ロゴ、検索フォーム、作者名、
    その他の要素を含むこともできます。

    コンテンツカテゴリ	フローコンテンツ, 知覚可能コンテンツ
    許可されている内容	フローコンテンツ。但し、子孫に他の <header> や <footer> がないこと。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素。ただし、<address>、<footer>、他の <header> 要素の子孫要素として配置してはなりません。
    許可されている ARIA ロール	group, presentation
    DOM インターフェイス

    使用上の注意
    <header> 要素は区分コンテンツではありません。
    つまり、この要素が新たなアウトラインを生成することはありません。
    すなわち header 要素は通常、自身を囲む section の見出し
    (h1–h6 要素) を含むことを意図していますが、必須ではありません。

    歴史的な使用法
    <header> 要素は HTML5 まで仕様書には現れていませんでしたが、
    実は HTML の最初期に存在していました。
    the very first website に見られるように、元は <head>
    要素として使用されていました。ある時点で、別な名前を使用することが決定されました。
    これによって <header> が自由になり、のちに別な役割を担う
    ことができるようになりました。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='header', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# header.py ends here
