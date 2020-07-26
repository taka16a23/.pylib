#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""embded -- embded tag

"""
from .html_tag import HtmlTag


class Embded(HtmlTag):
    """Embded

    Embded is a HtmlTag.
    Responsibility:

    HTML の <embed> 要素は、外部のコンテンツを文書中の指定された場所に埋め込みます。
    コンテンツは外部アプリケーションや、対話型コンテンツの他の出所
    (ブラウザーのプラグインなど) によって提供されます。

    メモ: 本文書は、 HTML5 の一部として定義された要素についてのみ記載します。
    以前の標準化されていない要素の実装については扱いません。

    最近のほとんどのブラウザーは、ブラウザーのプラグインの対応を非推奨にして削除しているため、
    サイトを平均的なユーザーのブラウザーで操作できるようにしたいのであれば、
    <embed> に頼ることは賢明ではないということを意識しておいてください。

    コンテンツカテゴリ	フローコンテンツ、記述コンテンツ、埋め込みコンテンツ、対話型コンテンツ、知覚可能コンテンツ
    許可されている内容	なし。これは空要素です。
    タグの省略	開始タグは必須。終了タグを記述してはならない。
    許可されている親要素	埋め込みコンテンツを受け入れるすべての要素。
    許可されている ARIA ロール	application, document, img, presentation
    DOM インターフェイス

    属性

    height
    このリソースを表示する高さを CSS ピクセル値で示します。
    絶対的な値でなければなりません。パーセント値は使用できません。
    src
    埋め込むリソースの URL を示します。
    type
    インスタンス化するプラグインを選択するために使用する MIME タイプ。
    width
    このリソースを表示する幅を CSS ピクセル値で示します。
    絶対的な値でなければなりません。パーセント値は使用できません。

    使用上のメモ
    object-position プロパティを使用して、
    要素のフレーム内の埋め込みオブジェクトの位置を調整することができ、
    object-fit プロパティを使用して、
    オブジェクトの寸法をフレーム内にどのように合わせるかを制御することができます。

    アクセシビリティの考慮事項
    embed 要素に title 属性を使用してコンテンツにラベルを付けるようにしてください。
    そうすれば、読み上げソフトのような支援技術を使用して捜査してい
    る人々が内容を理解することができるようになります。
    題名がないと、埋め込みコンテンツが何であるかを特定することができません。
    このようにして文脈を見失うと、特に embed 要素が動画や音声のような
    対話的なコンテンツを含んでいたとに、混乱したり時間を浪費したりします。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        HEIGHT = 'height'
        WIDTH = 'width'
        SRC = 'src'
        TYPE = 'type'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='embded', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# embded.py ends here
