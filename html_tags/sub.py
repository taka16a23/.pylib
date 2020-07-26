#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sub -- sub tag

"""
from .html_tag import HtmlTag


class Sub(HtmlTag):
    """Sub

    Sub is a HtmlTag.
    Responsibility:

    HTML の 下付き文字要素 (<sub>) は、表記上の理由で下付き
    文字として表示するべき行内文字列を指定します。
    下付き文字は普通、小さめのテキストを使用してベースラインよりも低く表示されます。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素。
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement

    使用上のメモ
    <sub> 要素は、単純に表現や表示の結果を得るためではなく、
    表記規則上の理由、つまり、表記上の習慣や標準でテキストの位置を
    変更する必要がある場合にのみ使用してください。

    例えば、変更したベースラインをワードマークの中で使用している
    企業名にスタイル付けするために <sub> を使用することは適切ではありません。
    このような場合には CSS を使用してください
    (例えば vertical-align プロパティを、 vertical-align: sub または、
    もっと詳細にベースラインの位置を制御するために、 vertical-align: -25% など)。

    <sub> の適切な利用場面には次のようなものがあります
    (これに限定されるものでありません)。

    脚注番号のマークアップ。例については Footnote numbers を参照してください。
    数学における下付き文字の変数値のマークアップ
    （ただし、 MathML の数式を使うことも検討してください）。
    Variable subscripts を参照してください。
    化学式における原子数の記述（例えば、すべての開発者のお友達、
    C8H10N4O2 別名「カフェイン」）。 Chemical formulas を参照してください。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='sub', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sub.py ends here
