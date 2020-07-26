#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""abbr -- abbr tag

"""
from .html_tag import HtmlTag


class Abbr(HtmlTag):
    """Abbr

    Abbr is a HtmlTag.
    Responsibility:

    HTML の略語要素 (<abbr>) は略語や頭字語を表します。
    任意で title 属性で、略語の完全形または説明を提供することができます。
    title 属性はこの完全な説明のみを含み、それ以外を含んではいけません。

    属性
    この要素にはグローバル属性のみに対応しています。
    title 属性は <abbr> 要素と共に使用すると、特定の意味論的な意味を持ちます。
    これは完全な人間が読める形の説明または略語の完全形を含む必要があります。
    この文字列は、マウスポインターが要素の上で静止したとき、
    ブラウザーがツールチップとして表示することが良くあります。

    それぞれの <abbr>要素は他の独立しています。
    同じ文書内で他の省略形ではない表現の文字列に自動的に結びつかない場合は、
    title を使用してください。

    使用上のメモ
    よくある使用例
    必ずしもすべての略語を <abbr> でマークアップする必要はありません。
    しかし、有用な場合がいくつかあります。

    略語が使用され、文書コンテンツの流れの外で完全形や定義を提供したい場合は、
    <abbr> を適切な title と共に使用してください。
    読み手にとってなじみのない略語を定義する場合、用語を <abbr> を使用して表現し、
    title 属性や行内文字列で定義を提供してください。
    テキスト内に略語が存在し、意味の注釈が必要な場合、 <abbr> 要素は有用です。
    一方、これは整形やスクリプトの目的で使用することができます。
    <abbr> は <dfn> との組み合わせで、略語や頭字語の用語の定義を行なうことができます。
    以下の略語の定義の例をご覧ください。
    文法的な考慮事項
    文法的に数を表現する言語（つまり、項目の数が文の文法に影響する言語）では、
    <abbr> 要素内の title 属性で同じ文法的な数値を使用してください。
    これは、アラビア語のように2よりも大きい数の文法を持つ言語で特に重要ですが、
    英語にも当てはまります。

    既定のスタイル
    この要素の目的は単に作者の利便性のためであり、
    すべてのブラウザーが既定でこの要素を行内 (display: inline) で表示します。
    ただし、既定のスタイルはブラウザーによりさまざまです。

    Internet Explorer など一部のブラウザーは、この要素を
    <span> 要素と同じスタイルを適用します。
    Opera、Firefox などのブラウザーは、この要素の内容に点線の下線を引きます。
    ごく一部のブラウザーは、ドットの下線を引くだけでなく、
    小さな大文字で表示するものがあります。本件を扱う CSS に font-variant: none
    のようなスタイルを追加することで、このようなスタイルを避けることができます。

    example
    <p>Ashok's joke made me <abbr title="Laugh Out Loud">LOL</abbr> big time.</p>
    """

    class AttributeNames(HtmlTag.AttributeNames):
        TITLE = 'title'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='abbr', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# abbr.py ends here
