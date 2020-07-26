#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""template -- template tag

"""
from .html_tag import HtmlTag


class Template(HtmlTag):
    """Template

    Template is a HtmlTag.
    Responsibility:

    HTML のコンテンツテンプレート (<template>) 要素 は、
    すなわちページの読み込み時にすぐには描画されないものの、
    後で JavaScript を使用してインスタンスを生成できる
    HTML を保持するメカニズムです。

    テンプレートは、文書内に格納されたコンテンツの断片として考えてください。
    ページの読み込み時にパーサーが <template> 要素の内容を処理している間、
    その内容の有効性のみが検証されます。しかし、要素の内容は描画されません。

    コンテンツカテゴリ	メタデータコンテンツ, フローコンテンツ, 記述コンテンツ, スクリプト対応要素
    許可されている内容	制限なし
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	メタデータコンテンツ, 記述コンテンツ, スクリプト対応要素 を受け付けるすべての要素。また、 span 属性を持たない <colgroup> 要素の子になることもできます。
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLTemplateElement

    属性
    この要素には、グローバル属性のみがあります。

    ただし、 HTMLTemplateElement の content プロパティは、
    読み取り専用の DocumentFragment で、テンプレートが表現する
    DOM サブツリーを保持しています。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='template', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# template.py ends here
