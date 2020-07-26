#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""em -- em tag

"""
from .html_tag import HtmlTag


class EM(HtmlTag):
    """EM

    EM is a HtmlTag.
    Responsibility:

    HTML の <em> 要素は、強調されたテキストを示します。
    <em> 要素は入れ子にすることができ、
    入れ子の段階に応じてより強い程度の強調を表すことができます。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement。 Gecko 1.9.2 (Firefox 4) 以前では、この要素には HTMLSpanElement インターフェイスが実装されています。

    使用上のメモ
    <em> 要素は、周囲の文字列と比較して強調される言葉のためのものであり、
    ふつうは文内の一語又は数語に限定され、文自体の意味に影響します。

    通常、この要素は斜体で表示されます。
    しかしながら、単に斜体のスタイルを適用するために用いるべきではなく、
    そのような目的のためには CSS によるスタイル付けを使用してください。
    著作物（書籍、演劇、歌など）の題名を示すためには、
    <cite> 要素を使用してください。
    これも通常、斜体のスタイルとなりますが、異なる意味を持っています。
    周辺のテキストよりも高い重要性を持つテキストを示すためには、
    <strong> 要素を使用してください。

    訳注: 日本語フォントでは斜体を持たないフォントが多く、
    斜体で表示されないことがあります。

    <i> と <em>
    新しい開発者はよく、同様の結果を生み出すために
    複数の要素があることによく混乱します。
    <em> と<i> はその代表例で、どちらも文字列を斜体にするものです。
    違いは何でしょうか。どちらを使用するべきでしょうか。

    既定では、視覚的な結果は同じです。
    しかし、意味論的な意味合いは異なります。
    <em> 要素はその内容を強調することを表しますが、
    一方で <i> 要素は、外来語、架空の登場人物の考え、
    用語の定義を表す文字列など、通常の文章から外れた文字列を表します。
    （書籍や映画などの作品名には、 <cite> を使用してください。）

    つまり、どちらを使うのが正しいかは場面に依存します。
    どちらも純粋な装飾目的ではなく、それは CSS による整形の役割です。

    <em> の例は "Just do it already!" や
    "We had to do something about it" です。
    文字列を読む人やソフトウェアは、斜体の単語を強調して読み上げるでしょう。

    <i> の例は "The Queen Mary sailed last night" です。
    ここで、 "Queen Mary" という語句に強調や重要性は与えていません。
    これは単に、対象物が Mary という名前の女王ではなく
    Queen Mary という名前の船であることを示します。
    <i> の別の例として "The word the is an article" があります。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='em', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# em.py ends here
