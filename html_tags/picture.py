#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""picture -- picture tag

"""
from .html_tag import HtmlTag


class Picture(HtmlTag):
    """Picture

    Picture is a HtmlTag.
    Responsibility:

    HTML の <picture> 要素は、0個以上の <source> 要素と一つの <img> 要素を含み、
    様々な画面や端末の条件に応じた画像を提供します。
    ブラウザーは複数の <source> 子要素を検討し、その中から最も適切なものを選択します。
    適切なものがない場合や、ブラウザーが <picture> 要素に対応してない場合、
    <img> 要素の src 属性で指定された URL が選択されます。
    選択された画像は <img> 要素が占有する領域に表示されます。

    どの URL を読み込むかを選択するには、ユーザーエージェントはそれぞれの
    <source> 要素の srcset, media, type 属性を調べて、現在のページのレイアウトや、
    表示端末の特性などの条件に最も合う画像を検討します。

    <picture> をよく使う場面は以下の通りです。

    アートディレクション — 様々な media の条件に合わせて画像を切り抜いたり変更したりする
    (例えば、小さな画面では、詳細すぎないより簡単な版の画像を読み込むなど)
    特定の形式がすべてのブラウザーで対応しているわけではない場合、
    異なる画像形式で提供する
    見る人の画面に基づいて、正しい寸法や大きさを持つ適切な版の画像を読み込むことで、
    ページの読み込みをより速くする
    DPI の高い (高解像度の) ディスプレイのために高解像度版の画像を提供する場合は、
    代わりに srcset 属性を <img> に使用してください。
    これによってブラウザーはデータ節約モードでは低解像度版を選択することができ、
    media 条件を明示的に書かなくてもよくなります。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 埋め込みコンテンツ
    許可されている内容	0個以上の <source> 要素、その後に1個の <img> 要素、任意でスクリプト対応要素と混在。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	埋め込みコンテンツを含むことができるすべての要素。
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLPictureElement

    使用上のメモ
    object-position プロパティを使用して、要素の枠内で画像の位置を調整したり、
    object-fit プロパティを使用して、枠内に合わせるための画像の寸法を変更する
    方法を制御したりすることができます。

    メモ: これらのプロパティは子の <img> 要素に用い、
    <picture> 要素には用いないでください。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='picture', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# picture.py ends here
