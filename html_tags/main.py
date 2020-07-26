#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""main -- main tag

"""
from .html_tag import HtmlTag


class Main(HtmlTag):
    """Main

    Main is a HtmlTag.
    Responsibility:

    HTML の <main> 要素は、文書の <body> の主要な内容を表します。
    主要な内容とは、文書の中心的な主題、
    またはアプリケーションの中心的な機能に直接関連または拡張した内容の範囲のことです。

    文書には hidden 属性が指定されていない <main> 要素を2つ以上置くことはできません。

    コンテンツカテゴリ	フローコンテンツ, 知覚可能コンテンツ
    許可されている内容	フローコンテンツ
    タグの省略	不可。開始タグと終了タグの両方が必須。
    許可されている親要素	フローコンテンツを受け入れる場所、但し階層的に正しい main 要素であること。
    許可されている ARIA ロール	既定で <main> 要素に main ロールを適用します。また、presentation ロールも許可されます。
    DOM インターフェイス

    使用上の注意
    <main> 要素の内容は、文書で固有のものにしてください。
    この内容はサイドバー、ナビゲーションリンク、著作権表示、サイトロゴ、
    検索フォームのような、文書のセットや文書のセクションにまたがって
    繰り返されるものを除くべきです。(もちろん、主な内容が検索フォームでない限り)

    <main> は文書のアウトラインに寄与しません。
    すなわち <body> や <h2> などの見出しとは異なり、
    <main> はページの構造の DOM の概念に影響を与えません。これは情報を与えるだけです。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='main', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# main.py ends here
