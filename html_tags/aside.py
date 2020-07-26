#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""aside -- aside tag

"""
from .html_tag import HtmlTag


class Aside(HtmlTag):
    """Aside

    Aside is a HtmlTag.
    Responsibility:

    HTML の <aside> 要素は、文書のメインコンテンツと間接的な関係しか持っていない
    文書の部分を表現します。
    サイドバーやコールアウトボックスなどを表現するためによく使われます。

    コンテンツカテゴリ	フローコンテンツ、区分コンテンツ、知覚可能コンテンツ
    許可されている内容	フローコンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素。<aside> 要素は <address> 要素の子孫要素として配置してはならない。
    暗黙の ARIA ロール	complementary
    許可されている ARIA ロール	feed, none, note, presentation, region, search
    DOM インターフェイス

    使用上の注意
    文章中の括弧書きについては、文章の主要な流れに属するものであるといえますので、
    これをタグ付けするために <aside> 要素を使用しないでください。

    Example
    <article>
      <p>
          The Disney movie <cite>The Little Mermaid</cite> was
          first released to theatres in 1989.
      </p>
      <aside>
        <p>
          The movie earned $87 million during its initial release.
        </p>
      </aside>
      <p>
        More info about the movie...
      </p>
    </article>
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='aside', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# aside.py ends here
