#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""ditails -- ditails tag

"""
from .html_tag import HtmlTag


class Details(HtmlTag):
    """Details

    Details is a HtmlTag.
    Responsibility:

    HTML の詳細折りたたみ要素 (<details>) は、ウィジェットが
    open 状態になった時のみ情報が表示される折りたたみウィジェットを作成します。
    概要やラベルは <summary> 要素を使用して提供することができます。

    折りたたみウィジェットはふつう、回転して開閉状態を示す小さな三角形を使用し、
    その隣のラベルと共に画面上に表現されます。
    <details> 要素の最初の子要素が <summary> の場合は、
    <summary> 要素が折りたたみウィジェットのラベルとして使用されます。

    HTML の詳細折りたたみ要素 (<details>) は、ウィジェットが open
    状態になった時のみ情報が表示される折りたたみウィジェットを作成します。
    概要やラベルは <summary> 要素を使用して提供することができます。

    折りたたみウィジェットはふつう、回転して開閉状態を示す小さな三角形を使用し、
    その隣のラベルと共に画面上に表現されます。
    <details> 要素の最初の子要素が <summary> の場合は、
    <summary> 要素が折りたたみウィジェットのラベルとして使用されます。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        """AttributeNames

        AttributeNames is a HtmlTag.AttributeNames.
        Responsibility:

        open
        この論理属性は、ページ読み込み時に詳細内容、
        つまり <details> 要素の内容が表示されるよう指定するものです。
        既定値は false であり、詳細内容は表示しません。

        イベント
        HTML で対応している通常のイベントに加えて、 <details> 要素は toggle イベントに対応しており、開閉状態が変化するたびに <details> 要素が呼び出されます。イベントは状態が変化した後に送信され、もしブラウザーがイベントを送信する前に状態が2回以上変化しても、イベントは合体して1回しか送信されません。

        ウィジェットの状態が変化したことを検出するために、 toggle イベントをリスンすることができます。

        details.addEventListener("toggle", event => {
        if (details.open) {
        /* 要素が開いた方に切り替わった */
        } else {
        /* 要素が閉じた方に切り替わった */
        }
        });
        """
        OPEN = 'open'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='details', tags=[], attrs=None, **kwargs)

    def enable_open(self, ):
        """Enable open.

        enable_open()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.OPEN, '')

    def disable_open(self, ):
        """Disable open.

        disable_open()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.OPEN in self.attrs:
            del self.attrs[self.AttributeNames.OPEN]
        return self

    def is_open(self, ):
        """Check open enabled.

        is_open()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.OPEn in self.attrs



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ditails.py ends here
