#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""ul -- ul tag

"""
from .html_tag import HtmlTag


class Ul(HtmlTag):
    """Ul

    Ul is a HtmlTag.
    Responsibility:

    HTML の <ul> 要素は、項目の順序なしリストを表します。
    一般的に、行頭記号を伴うリストとして描画されます。

    コンテンツカテゴリ	フローコンテンツ。また、 <ul> 要素の子に少なくとも 1 個 <li> 要素を包含する場合は、知覚可能コンテンツ。
    許可されている内容	0個以上の <li> または <script> 、 <template> 要素。 <li> 要素の子孫としてさらに <ol> 要素や <ul> 要素を配置することも可能。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    許可されている ARIA ロール	directory, group, listbox, menu, menubar, radiogroup, tablist, toolbar, tree, presentation
    DOM インターフェイス	HTMLUListElement

    使用上のメモ
    <ul> 要素は、数的な順序がなく、その配置順に意味を持たない項目を持つリストを表します。
    通常、順序なしリストの項目はドット、円形、四角形などいくつかの形式による
    行頭記号を伴って描画されます。行頭記号のスタイルは HTML
    仕様書のページでは定義されていませんが、 CSS の list-style-type
    プロパティを用いて変更することが可能です。
    <ol> 要素と <ul> 要素は、必要なだけ深く入れ子にすることができます。
    さらに言えば、入れ子になったリストが <ol> と <ul> の間で
    変化することにで制限はありません。
    <ol> と <ul> は、どちらも項目のリストを表します。
    両者の違いは、 <ol> 要素では順序に意味があることです。
    使い分けの目安としては、項目の順序を変更してみてください。
    意味が変わるようであれば <ol> 要素を使用し、そうでない場合は
    <ul> 要素を使用することができます。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='ul', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ul.py ends here
