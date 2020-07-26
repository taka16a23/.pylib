#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""html -- html tag

"""
from .html_tag import HtmlTag


class Html(HtmlTag):
    """Html

    Html is a HtmlTag.
    Responsibility:

    HTML の <html> 要素は HTML 文書においてルート (基点) となる要素
    (トップレベル要素) であり、ルート要素とも呼ばれます。
    他のすべての要素は、この要素の子孫として配置しなければなりません。

    コンテンツカテゴリ	なし
    許可されている内容	ひとつの <head> 要素と、それに続くひとつの <body> 要素。
    タグの省略	開始タグは、 <html> 要素内の最初のノードがコメントでない場合は省略可能です。
    終了タグは、 <html> 要素の直後にコメントがない場合は省略可能です。
    許可されている親要素	なし。これは文書のルート要素です。
    許可されている ARIA ロール	なし
    DOM インターフェイス

    xmlns
    文書の XML 名前空間を指定します。
    既定値は "http://www.w3.org/1999/xhtml" です。
    これは XML パーサーで解釈される文書では必須、 text/html の文書では任意です。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        XMLNS = 'xmlns'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='html', tags=[], attrs=None, **kwargs)

    def set_xmlns(self, value):
        """Set xmlns.

        set_xmlns(value)

        @Arguments:
        - `value`: xmlns value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.XMLNS, value)

    def get_xmlns(self, ):
        """Get xmlns attribute value.

        get_xmlns()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.XMLNS, None)

    def remove_xmlns(self, ):
        """Remove xmlns attribute.

        remove_xmlns()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.XMLNS in self.attrs:
            del self.attrs[self.AttributeNames.XMLNS]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# html.py ends here
