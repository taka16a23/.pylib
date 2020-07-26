#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""code -- code tag

"""
from .html_tag import HtmlTag


class Code(HtmlTag):
    """Code

    Code is a HtmlTag.
    Responsibility:

    HTML の <code> 要素は、コンピューターコードの短い断片の文字列で
    あると識別できるような外見のコンテンツを表示します。
    既定では、中の文字列がユーザーエージェントの既定の等幅フォントを
    使用して表示されます。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement。Gecko 1.9.2 (Firefox 4) 以前では、この要素には HTMLSpanElement インターフェイスが実装されています。

    メモ
    複数行のコードを表すには、 <code> 要素を <pre> 要素の中に入れてください。
    <code> 要素自身は、コードの単一のフレーズや1行のみを表します。

    CSS の規則によって、 code セレクターを定義して、
    ブラウザーの既定のフォントを上書きすることができます。
    ユーザーによる設定を CSS による指定より優先させることもできます。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='code', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# code.py ends here
