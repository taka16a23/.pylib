#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""menu -- menu tag

"""
from .html_tag import HtmlTag


class Menu(HtmlTag):
    """Menu

    Menu is a HtmlTag.
    Responsibility:

    HTML の <menu> 要素は、ユーザーが実行またはアクティブ化可能な
    コマンドのグループを表します。
    これはスクリーンの上部にあるリストメニューや、
    ボタンを押したときにボタンの下部に現れるようなコンテキストメニューを含みます。

    コンテンツカテゴリ
    フローコンテンツ。要素の子が1個以上の <li> 要素を含んでいる場合は知覚可能コンテンツ。

    許可されている内容
    要素がリストメニュー状態である場合: フローコンテンツまたは0個以上の <li>, <script>, <template>。 (リストメニューは、親要素がコンテキストメニュー状態の <menu> でない場合の既定の状態です。)

    要素がコンテキストメニュー状態である場合は、任意の順序で、0個以上の <menu> (コンテキストメニュー状態に限る), <menuitem>, <hr>, <script>, <template>。

    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLMenuElement
    属性

    label
    ユーザーに対して表示する、メニューの名称です。
    入れ子のメニューで、サブメニューへアクセスできるようにするためにラベルを与えます。
    親要素がコンテキストメニュー状態の <menu> である場合に限り、必須です。

    type
    この属性は定義済みのメニューの種類を示すものであり、以下2つの値のいずれかを指定します。
    context  : ポップアップメニュー状態であり、他の要素を経由して
    アクティブになるコマンドのグループを表します。
    <button> 要素の menu 属性や、 contextmenu 属性を持つ要素を経由することが考えられます。
    <menu> 要素が別の menu 要素の入れ子になっているとき、親要素がすでにこの状態であれば、
    子要素で値が指定されていない場合の既定値になります。
    toolbar: ツールバー状態であり、ユーザーと対話するための一連のコマンドを表します。
    これは <li> が並んだ番号なしリストの形か、子要素に <li> を含まない場合は、
    利用できるコマンドを記述したフローコンテンツです。
    属性が指定されていない場合の既定値です。

    使用上の注意
    <menu> 要素と <ul> 要素はともに順序なしリストの項目を表すものですが、
    <ul> は主に項目の表示を目的とするのに対し、
    <menu> 要素は操作を行うための対話型の項目を含めるためのものです。

    HTML メニューは、コンテキストメニュー（一般的に、別の要素を右クリックすると表示される）
    またはツールバーを作成するために使用できます。

    コンテキストメニューは、「メニューで選択可能な項目を表す <menuitem> 要素」
    「メニュー内のサブメニューを表す <menu> 要素」
    「メニューの内容をセクションに分けるセパレーター行を表す <hr> 要素」を包含する
    <menu> 要素で構成されます。
    コンテキストメニューは、関連付ける要素の contextmenu 属性、
    または ボタンでアクティブにするメニュー であれば <button> 要素の
    menu 属性を使用して、メニューをアクティブ化する要素に紐づけます。

    ツールバーメニュー は、以下のいずれかをコンテンツにした
    <menu> 要素で構成されます: <li> 要素で表した項目の順不同リスト
    (それぞれの項目が、ユーザーが利用できるコマンドやオプションを表します)。
    または、(<li> 要素がない場合) 使用なコマンドやオプションを表す フローコンテンツ。

    この要素は HTML4 で非推奨になりましたが、
    HTML5.1 および HTML living standard で再導入されました。
    本ドキュメントは、現行の Firefox の実装について説明します。
    HTML 5.1 によって、type 属性の 'list' が 'toolbar' に変わりました。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        LABEL = 'label'
        TYPE = 'type'

    class Type(object):
        """Type

        Type is a object.
        Responsibility:
        """
        CONTEXT = 'context'
        TOOLBAR = 'toolbar'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='menu', tags=[], attrs=None, **kwargs)

    def set_label(self, value):
        """Set label attibutes value.

        set_label(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.LABEL, value)
        return self

    def get_label(self, ):
        """Get label attribute value.

        get_label()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.LABEL, None)

    def remove_label(self, ):
        """Remove label attribute value.

        remove_label()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.LABEL in self.attrs:
            del self.attrs[self.AttributeNames.LABEL]
        return self

    def set_type(self, value):
        """Set type attibutes value.

        set_type(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.TYPE, value)
        return self

    def get_type(self, ):
        """Get type attribute value.

        get_type()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.TYPE, None)

    def remove_type(self, ):
        """Remove type attribute value.

        remove_type()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.TYPE in self.attrs:
            del self.attrs[self.AttributeNames.TYPE]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# menu.py ends here
