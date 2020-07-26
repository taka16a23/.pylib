#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""b -- b tag

"""
from .html_tag import HtmlTag


class b(HtmlTag):
    """b

    b is a HtmlTag.
    Responsibility:

    HTML の注目付け要素 (<b>) は、要素の内容に読み手の注意を惹きたい場合で、
    他の特別な重要性が与えられないものに使用します。
    これは以前は太字要素と呼ばれており、ほとんどのブラウザーでは文字列を太字で描画していました。
    しかし、 <b> を文字列の装飾に使うべきではありません。
    太字の文字列を作成するには、 CSS の font-weight プロパティを使用し、
    特別な重要性を持つテキストを示すには <strong> 要素を使用してください。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略          不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    暗黙の ARIA ロール	対応するロールなし
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement

    使用上のメモ
    <b> は要約に現れるキーワード、レビュー文内での製品名、または、
    その他の表記上太字で記述される通例のある箇所 (但し、特別な重要性を持たない部分)
    に使用してください。
    <b> 要素を <strong>, <em>, <mark> 要素と混同しないでください。
    <strong> は特定の重要性を持った文字列を表し、 <em> はテキストを軽く強調し、
    <mark> は特定の関連性を持った文字列を表します。
    <b> はそのような特別な意味を持ちません。
    他の要素が持つ意味合いに合わないときのみ使用してください。
    同様に、 <b> 要素でタイトルや見出しをマークしないでください。
    この用途では <h1> から <h6> タグを使用します。
    さらに、スタイルシートでこれらの要素の既定のスタイルを変更できるので、
    これらの要素は太字で表示されるとは限りません。
    必要に応じて追加的な意味情報を伝える目的で <b> 要素に
    class 属性を使用することはよい使用法です
    (例えば、段落の最初の文に <b class="lead"> を設定するなど)。
    これによって、 <b> の様々な使用法が管理しやすくなり、スタイル上の変更が必要になった時、
    HTML における使用方法を変更する必要がなくなります。
    歴史的に <b> 要素は太字の文字列を作るためのものでしたが、
    HTML4 でスタイル情報が非推奨になったので <b> 要素の意味が変更されました。
    <b> 要素の使用に意味上の目的がない場合は、文字列を太字にするために代わりに CSS の
    font-weight プロパティの値を "bold" に設定してください。

    例
    <p>
    This article describes several <b class="keywords">text-level</b> elements.
    It explains their usage in an <b class="keywords">HTML</b> document.
    </p>
    Keywords are displayed with the default style of the <b>element, likely in bold.</b>
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='b', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# b.py ends here
