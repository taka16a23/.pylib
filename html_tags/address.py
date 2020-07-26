#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""address -- address tag

"""
from .html_tag import HtmlTag


class Address(HtmlTag):
    """Address

    Address is a HtmlTag.
    Responsibility:

    HTML の <address> 要素は、これを含んでいる
    HTML が個人、団体、組織の連絡先を提供していることを示します。

    コンテンツカテゴリ	フローコンテンツ、知覚可能コンテンツ
    許可されている内容	フローコンテンツ。
                        ただし <address> 要素をネストしたり、見出しコンテンツ
                        (<hgroup>, <h1>, <h2>, <h3>, <h4>, <h5>, <h6>),
                        区分コンテンツ (<article>, <aside>, <section>, <nav>),
                        <header> 要素および <footer> 要素を入れたりしてはなりません。
    タグの省略          不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツ を受け入れるすべての要素。ただし <address> 要素は除く (論理的な対称性の原理によれば、親要素である <address> タグは <address> 要素を入れ子にすることができません。したがって、同じ <address> のコンテンツの親に <address> タグを置くこともできません)。
    暗黙の ARIA ロール	対応するロールなし
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement。 Gecko 2.0 (Firefox 4) より前では HTMLSpanElement インターフェイスが提供されます。

    <address> 要素の内容で提供される連絡先情報は、その文脈で適切であればどのような形でもよく、
    必要とされるあらゆる形の連絡先情報 (住所、 URL、メールアドレス、電話番号、
    ソーシャルメディアのアカウント、地理上の座標など) を含めることができます。
    <address> には連絡先情報が参照する個人、団体、組織の名前を含めてください。

    <address> は様々な文脈で使用することができ、ページヘッダーでビジネスの連絡先を提供したり、
    <article> 要素の中で <address> を含めることで、
    記事の著者を識別したりすることができます。

    使用上の注意
    <address> 要素は文書の著者の連絡先情報を表すだけのために使われる傾向があります。
    しかし最新の仕様書では、定義が更新され、様々な
    宛先をマークアップするために使用できるようになりました。
    この要素には、公開日 (<time> によるもの) のような
    連絡先情報以外の情報を含めるべきではありません。
    一般的に、 <address> 要素は現在のセクションに
    <footer> 要素があれば、その中に配置することができます。

    <address>
      You can contact author at <a href="http://www.somedomain.com/contact">
      www.somedomain.com</a>.<br>
      If you see any bugs, please <a href="mailto:webmaster@somedomain.com">
      contact webmaster</a>.<br>
      You may also want to visit us:<br>
      Mozilla Foundation<br>
      331 E Evelyn Ave<br>
      Mountain View, CA 94041<br>
      USA
    </address>

    この要素は文字列を <i> 要素や <em> 要素と同じ既定のスタイルで描画しますが、
    付加的な意味情報として連絡先情報を扱うときに
    <address> を使用するのがより適切でしょう。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='address', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# address.py ends here
