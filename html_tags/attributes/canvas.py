#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""canvas -- canvas tag

"""
from .html_tag import HtmlTag


class Canvas(HtmlTag):
    """Canvas

    Canvas is a HtmlTag.
    Responsibility:

    HTML の <canvas> 要素 と Canvas スクリプティング API や WebGL API を使用して、
    グラフィックやアニメーションを描画することができます。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 埋め込みコンテンツ, 知覚可能コンテンツ
    許可されている内容	透過的コンテンツ、ただし子孫に対話型コンテンツのうち <a> 要素, <button> 要素, <input> 要素の type 属性が checkbox, radio, button のいずれか以外を含まないもの
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLCanvasElement

    属性
    height
    CSS ピクセルで示した座標空間の高さ。既定では150ピクセルに設定されています。
    moz-opaque
    canvas に半透明性がファクターになるかを知らせます。キャンバスは半透明性がないことがわかっていれば、描画パフォーマンスを最適化できます。これは Mozilla ベースのブラウザーしか対応していません。代わりに標準化された canvas.getContext('2d', { alpha: false }) を使用してください。
    width
    CSS ピクセルで示した座標空間の幅。既定では300ピクセルに設定されています。

    使用上の注意
    代替コンテンツ
    <canvas> のブロックの中で、代替コンテンツを提供することが可能 (また、提供すべき) です。その内容物は、 canvas に対応しない古いブラウザーおよび JavaScript が無効であるブラウザーで描画されます。

    </canvas> タグが必要
    <img> 要素とは異なり、 <canvas> 要素は終了タグ (</canvas>) が必要です。

    CSS と HTML におけるキャンバスの寸法指定の違い
    表示されるキャンバスの寸法は、スタイルシートを用いて変更できますが、そうすると画像はスタイルで設定した寸法に合うように拡大縮小され、最終的なグラフィックが歪んで表示されることがあります。

    キャンバスの寸法は、 HTML または JavaScript を用いて width および height 属性を <canvas> 要素に直接設定するした方がいいでしょう。

    キャンバスの最大寸法
    <canvas> 要素の最大寸法はとても広いのですが、正確な寸法はブラウザーに依存します。以下のものは様々なテストやその他の情報源 (Stack Overflow など) から収集したいくらかのデータです。

    ブラウザー	最大高	最大幅	最大面積
    Chrome	32,767 pixels	32,767 pixels	268,435,456 pixels (つまり 16,384 x 16,384)
    Firefox	32,767 pixels	32,767 pixels	472,907,776 pixels (つまり 22,528 x 20,992)
    Safari	32,767 pixels	32,767 pixels	268,435,456 pixels (つまり 16,384 x 16,384)
    IE	8,192 pixels	8,192 pixels	?
    メモ: 寸法や面積の最大値を超えると、キャンバスが使用できなくなります。 — 描画コマンドが動作しなくなります。

    例
    このコードの断片は、 HTML 文書に canvas 要素を追加するものです。ブラウザーが canvas を描画できない、あるいは canvas を読み込めない場合は、代替文字列を表示します。役に立つ代替文字列や内部の DOM を提供すると、 canvas のアクセシビリティをより高めることに役立ちます。

    <canvas id="canvas" width="300" height="300">
    キャンバスが表示する内容を記述する代替テキストです。
    </canvas>
    g

    それから JavaScript のコードで、 HTMLCanvasElement.getContext() を呼び出して描画コンテキストを取得し、キャンバスへの描画を始めます。

    <script>
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = 'green';
    ctx.fillRect(10, 10, 100, 100);
    </script>
    不透明のキャンバス
    canvas で半透明効果を使用しない場合は、ブラウザーにキャンバスが不透明であることを伝えると、描画を最適化するために内部で使用されます。このためには、描画コンテキストを取得する際に alpha に false を設定してください。

    <script>
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d', { alpha: false });
    </script>
    alpha オプションが標準化される前は、 canvas タグに moz-opaque   を使うことができました。しかし、これは Mozilla ベースのレンダリングエンジンでしか動作しないので、使用するべきではありません。この属性がいつ削除されるかを追跡するには、 bug 878155 をチェックしてください。

    <canvas id="myCanvas" moz-opaque></canvas>
    アクセシビリティの考慮事項
    代替コンテンツ
    canvas 要素は単なるビットマップであり、描かれたオブジェクトに関する情報は提供しません。キャンバスのコンテンツは、セマンティック HTML のようなアクセシビリティツールには公開されていません。一般的に、アクセシビリティに配慮したウェブサイトやアプリではキャンバスを使用しないでください。アクセシビリティを改善するには、以下のガイドが役立ちます。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        """AttributeNames
        AttributeNames is a HtmlTag.AttributeNames.
        Responsibility:

        height
        CSS ピクセルで示した座標空間の高さ。既定では150ピクセルに設定されています。
        moz-opaque
        canvas に半透明性がファクターになるかを知らせます。
        キャンバスは半透明性がないことがわかっていれば、描画パフォーマンスを最適化できます。
        これは Mozilla ベースのブラウザーしか対応していません。
        代わりに標準化された canvas.getContext('2d', { alpha: false })
        を使用してください。
        width
        CSS ピクセルで示した座標空間の幅。既定では300ピクセルに設定されています。
        """
        HEIGHT = 'height'
        WIDTH = 'width'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='canvas', tags=[], attrs=None, **kwargs)

    def set_height(self, value):
        """Set height.

        set_height(value)

        @Arguments:
        - `value`: height attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.HEIGHT, value)
        return self

    def get_height(self, ):
        """Get height attribute value.

        get_height()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.HEIGHT, None)

    def remove_height(self, ):
        """Remove height attribute.

        remove_height()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.HEIGHT in self.attrs:
            del self.attrs[self.AttributeNames.HEIGHT]
        return self

    def set_width(self, value):
        """Set width.

        set_width(value)

        @Arguments:
        - `value`: width attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.WIDTH, value)
        return self

    def get_width(self, ):
        """Get width attribute value.

        get_width()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.WIDTH, None)

    def remove_width(self, ):
        """Remove width attribute.

        remove_width()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.WIDTH in self.attrs:
            del self.attrs[self.AttributeNames.WIDTH]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# canvas.py ends here
