#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""caption -- caption tag

"""
from .html_tag import HtmlTag


class Caption(HtmlTag):
    """Caption

    Caption is a HtmlTag.
    Responsibility:

    HTML の表キャプション要素 (<caption>) は、表のキャプション (またはタイトル) を
    指定するもので、使用される場合は常に <table> の最初の子要素として
    配置しなければなりません。スタイルや表との間の相対的な位置は、
    CSS の caption-side および text-align プロパティを使用して変更することができます。

    コンテンツカテゴリ	なし
    許可されている内容	フローコンテンツ
    タグの省略	要素の直後に ASCII 空白文字やコメントが続かない場合、終了タグは省略可能です。
    許可されている親要素	<table> 要素。table 要素の最初の子要素としてのみ配置可能。
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLTableCaptionElement

    使用上の注意
    <caption> を含む <table> 要素が <figure> 要素の唯一の子孫である場合は、
    <caption> の代わりに <figcaption> 要素を使用してください。

    例
    <caption> 要素の使用例については、<table> 要素のページを参照してください。

    <table>
      <caption>Example Caption</caption>
      <tr>
        <th>Login</th>
        <th>Email</th>
      </tr>
      <tr>
        <td>user1</td>
        <td>user1@sample.com</td>
      </tr>
      <tr>
        <td>user2</td>
        <td>user2@sample.com</td>
      </tr>
    </table>
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='caption', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# caption.py ends here
