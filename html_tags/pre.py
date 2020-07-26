#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""pre -- pre tag

"""
from .html_tag import HtmlTag


class Pre(HtmlTag):
    """Pre

    Pre is a HtmlTag.
    Responsibility:

    HTML <pre> 要素は、整形済みテキスト (preformatted text) を表します。
    この要素内のテキストは一般的に、ファイル内でのレイアウトをそのまま反映して
    等幅 ("monospace") フォントで表示されます。
    この要素内のホワイトスペース文字はそのまま表示します。

    コンテンツカテゴリ	フローコンテンツ、知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLPreElement

    アクセシビリティの考慮事項
    整形済みテキストを使用して作られた絵や図に対して、別な説明を提供することは重要です。
    この別な説明は、明確かつ簡潔に絵や図の中身を説明するものにしてください。

    弱視の人や、読み上げソフトのような支援技術を使用している人は、
    順番に読んだときに整形済みテキストで表現されているものが何か理解できないかもしれません。

    <figure> 及び <figcaption> 要素の組み合わせに、 id 及び ARIA role 及び
    aria-labelledby 属性を補ったもので、整形済みテキストを図形として扱い、
    figcaption を図形の別の説明として提供することができます。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='pre', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# pre.py ends here
