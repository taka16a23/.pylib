#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""figure -- figure tag

"""
from .html_tag import HtmlTag


class Figure(HtmlTag):
    """Figure

    Figure is a HtmlTag.
    Responsibility:

    HTML の <figure> (任意のキャプション付きの図)
    要素は、図表などの自己完結型のコンテンツを表し、
    任意で (<figcaption>) 要素を使用して表されるキャプションを伴います。
    図、すなわちキャプションとその中身は一つの単位として参照されます。

    コンテンツカテゴリ	フローコンテンツ, 区分化ルート, 知覚可能コンテンツ
    許可されている内容	<figcaption> 要素とそれに続くフローコンテンツ、またはフローコンテンツとそれに続く<figcaption> 要素、またはフローコンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    許可されている ARIA ロール	group, presentation
    DOM インターフェイス

    使用上のメモ
    ふつう <figure> は画像、イラスト、グラフ、コードの断片など、
    文書の本文の流れから参照されるものの、本文の流れに影響を与えることなく、
    文書のほかの部分や付録に移動することが可能なものに用います。
    区分化ルートとなり、 <figure> 要素のコンテンツのアウトラインは、
    文書の本文のアウトラインから除外されます。
    キャプションは <figure> 要素の中に (最初または最後の子要素として)
    <figcaption> 要素を挿入することで表すことができます。
    図の中で最初に見つかった最初の <figcaption>
    要素が図のキャプションとして表示されます。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='figure', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# figure.py ends here
