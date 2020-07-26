#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sup -- sup tag

"""
from .html_tag import HtmlTag


class Sup(HtmlTag):
    """Sup

    Sup is a HtmlTag.
    Responsibility:

    HTML の 上付き文字要素 (<sup>) は、
    表記上の理由で上付き文字として表示するべき行内文字列を指定します。
    上付き文字は普通、小さめのテキストを使用して高いベースラインで表示されます。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement

    使用上のメモ
    <sup> 要素は、単純に表現や表示の結果を得るためではなく、
    表記規則上の理由、つまり、表記上の習慣や規則でテキストの位置を
    変更する必要がある場合にのみ使用してください。

    例えば、高いベースラインを使用しているビジネスや製品の
    ワードマークをスタイル付けするには、 <sup> ではなく CSS を使用してください
    (例えば vertical-align)。例えば、 vertical-align: super とするか、
    ベースラインを50%上げるのであれば、 vertical-align: 50% とするかしてください。

    <sup> の適切な使用例には次のようなものがあります
    (但し、制約するものではありません)。

    べき乗の表示、例えば "x3"。これには、特に複雑な場合には、
    MathML の使用を検討する価値があるかもしれません。
    以下の例のべき乗を参照してください
    一部の言語で特定の略語を表示する際の superior lettering。
    例えば、フランス語では、 "mademoiselle" は "Mlle" のように略すことができます。
    例は Superior lettering を参照してください。
    序数の表現、たとえば "fourth." を "4th" と表現すること。
    例は Ordinal numbers を参照してください。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='sup', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sup.py ends here
