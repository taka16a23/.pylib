#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""video -- video tag

"""
from .html_tag import HtmlTag


class Video(HtmlTag):
    """Video

    Video is a HtmlTag.
    Responsibility:

    HTML の映像要素 (<video>) は、文書中に映像再生に対応する
    メディアプレイヤーを埋め込みます。
    <video> を音声コンテンツのために使用することもできますが、
    <audio> 要素の方がユーザーに取って使い勝手が良いかもしれません。

    上記の例は <video> 要素のシンプルな使い方を示しています。
    <img> 要素の方法と同様に、 src 属性の中に表示したいメディアへのパスを含めます。
    他の属性を含めて、映像の幅や高さ、自動再生やループをするかどうか、
    ブラウザーの標準の映像コントロールを表示するかなどの情報を指定することができます。

    開始・終了タグである <video></video> タグの間の内容は、
    この要素に対応していないブラウザーで代替として表示されます。

    属性
    この要素にはグローバル属性があります。

    メモ: 自動的に音声 (あるいは音声トラックを含む映像) を再生するサイトはユーザーにとって不快な体験になる可能性がありますので、可能な限り避けるべきです。自動再生機能が必須である場合は、オプトイン (ユーザーが明示的に有効化することを求める) にするべきです。ただし、ユーザーの制御下で後からソースを設定するメディア要素を作成するときは、この方法が役に立つでしょう。正しい自動再生の使い方についての追加情報は autoplay ガイドを参照してください。
    映像の自動再生を無効にするために autoplay="false" を指定しても機能しません。 <video> タグにこの属性があれば、映像が自動的に再生されます。自動再生を無効にするには、属性を完全に取り除くことが必要です。

    一部のブラウザー (Chrome 70.0 など) では、 muted 属性がないと autoplay は動作しません。

    autoplay
    論理型の属性です。この属性が指定された場合、データの読み込みが完了し、
    再生可能な状態になった時点で即座にコンテンツの再生が始まります。

    autoPictureInPicture
    論理属性で、 true であれば、ユーザーがこの文書と他の文書や
    アプリケーションとの間を行き来したときに、自動的にピクチャインピクチャモードに
    切り替わるようにすることを示します。

    buffered
    メディアがどれだけの時間分バッファリングされたかを判断するために、
    読み取ることが可能な属性です。この属性は TimeRanges オブジェクトを持ちます。

    controls
    この属性が指定された場合、再生、音量、シーク、
    ポーズの各機能を制御するコントロールを表示します。

    controlslist
    controlslist 属性が指定されていると、
    ブラウザー自身のコントロールのセットを表示する場合
    (例えば controls 属性が設定されている場合)、
    メディア要素に表示するコントロールを選択するのを補助します。
    指定できる値は nodownload, nofullscreen, noremoteplayback です。

    disablePictureInPicture 属性を使用すると、
    ピクチャインピクチャモード (およびコントロール) を無効にすることができます。

    crossorigin
    この列挙型の属性は、関連画像を取得する際に CORS を使用するかを示します。
    CORS が有効なリソース は、汚染されることなく <canvas> 要素で再利用できます。
    次の値が使用できます:

    anonymous
    資格情報を伴わずにオリジン間リクエストを実行します。
    すなわち、Cookie や X.509 証明書がない Origin: HTTP ヘッダーを送信する、
    あるいは HTTP ベーシック認証を行いません。
    サーバーが元のサイトに信用情報を付与しない場合
    (Access-Control-Allow-Origin: HTTP ヘッダーの設定なし)、
    画像が汚染され、その使用も制限されます。

    use-credentials
    クレデンシャルを伴ってオリジン間要求を実行します。
    すなわち、Cookie や X.509 証明書を伴う Origin: HTTP ヘッダーを送信する、
    あるいは HTTP ベーシック認証を行います。
    サーバーが元のサイトに信用情報を付与しない場合
    (Access-Control-Allow-Credentials: HTTP ヘッダーに関わらず)、
    画像が汚染され、その使用も制限されます。
    この属性が提供されない場合、リソースは CORS 要求なしで取得され
    (Origin: HTTP ヘッダーを送信せずに取得)、<canvas>
    要素での汚染されない使用が妨げられます。
    これが無効な場合、列挙型のキーワードに anonymous が
    指定されたものとして扱われます。追加の情報は CORS 設定属性 を参照してください。

    currentTime
    currentTime を読み込むと、秒単位で指定されたメディアの現在の再生位置を
    示す倍精度の浮動小数点値を返します。
    メディアがまだ再生を開始していない場合は、再生を開始する時間オフセットを返します。
    currentTime を設定すると、現在の再生位置を指定された時間に設定し、
    メディアがすでに読み込まれている場合には、その位置までメディアをシークします。

    メディアがストリーミングされている場合、そのデータがメディアバッファ上で
    期限切れになっていると、ユーザエージェントがリソースの一部を取得できない
    可能性があります。メディアによっては、0秒から開始しないメディアのタイムラインが
    ある場合もあり、 currentTime をそれ以前の時間に設定すると失敗します。
    メディアタイムラインの参照フレームの開始点を決定するには、
    getStartDate() メソッドを使用することができます。

    disablePictureInPicture
    ブラウザーにピクチャインピクチャのコンテキストメニューを
    表示させないようにしたり、場合によっては自動的にピクチャインピクチャを
    要求しないようにします。

    disableRemotePlayback
    論理属性で、有線 (HDMI, DVI など) や無線 (Miracast, Chromecast,
    DLNA, AirPlay など) を使用して接続された端末のリモート
    再生機能を無効にするために使用されます。
    Safari では、代替として x-webkit-airplay="deny" を使用することができます。

    duration 読取専用
    倍精度浮動小数点値で、メディアのタイムライン上でのメディアの再生時間 (全長)
    を秒単位で示します。
    要素にメディアが存在しない場合、またはメディアが有効でない場合は
    NaN が返されます。
    メディアの終了時刻が不明な場合
    (持続時間不明のライブストリーム、ウェブラジオ、 WebRTC からのメディア受信など)、
    この値は +Infinity になります。

    height
    映像の表示領域の高さを、 CSS ピクセル値で指定します。
    (絶対値に限ります。パーセント値は不可。)

    intrinsicsize
    この属性はブラウザーに、画像の固有の寸法を無視し、
    この属性で指定された寸法であると見せかけるよう指示します。
    特に、画像がこれらの次元のラスターであって、
    画像の naturalWidth/naturalHeight はこの属性で指定された値が返されます。
    説明と例

    loop
    論理型の属性です。
    指定された場合、ブラウザーは映像の末尾に達すると、自動的に先頭に戻ります。

    muted
    論理型の属性で、映像に含まれる音声の既定の設定を示します。
    この属性を設定すると、初期状態が消音になります。
    既定値は false であり、映像再生時に音声も再生することを表します。

    playsinline
    論理属性で、映像を「インライン」で再生する、
    すなわち要素の再生領域内で再生するかを指定します。
    この属性がないことが、映像を常に全画面で再生するという
    意味ではないことに注意してください。

    poster
    映像のダウンロード中に表示される画像の URL です。
    この属性が指定されない場合、最初のフレームが利用可能になるまで何も表示されず、
    その後、最初のフレームをポスターフレームとして表示します。

    preload
    列挙型の属性で、映像が再生される前に、
    どのコンテンツを読み込むとユーザーに最高の使い勝手を
    もたらすかについての作者の考えを、
    ブラウザーに対するヒントとしてを提供するためのものです。
    以下の値のうちひとつを持つことができます。
    none: 映像を事前に読み込むべきではないことを示します。
    metadata: 映像のメタデータ (例えば、長さ) を読み込みます。
    auto: ユーザーが映像ファイルを使用しないと思われる場合でも、
    ファイル全体をダウンロードしてよいことを示します。
    空文字列: これは auto 値と同義です。
    既定値はブラウザーごとに異なります。仕様書では metadata を設定するよう助言しています。

    注:
    autoplay 属性は preload より優先します。
    autoplay を指定すると、言うまでもなくブラウザーは映像を
    再生するためにダウンロードを始めなければなりません。
    仕様書は、ブラウザーがこの属性の値に従うことを強制していません。
    これは単なるヒントです。
    src
    埋め込む映像コンテンツへの URL を指定します。
    この属性は省略可能です。
    埋め込む映像の指定には、video 要素のブロック内で <source> を
    使用することもできます。
    width
    映像の表示領域の幅を、 CSS ピクセル値で指定します。
    (絶対値に限ります。パーセント値は不可)。
    イベント
    イベント名	発生する時
    audioprocess	ScriptProcessorNode の入力バッファが処理可能になった。
    canplay	ブラウザーがメディアを再生できるようになったものの、追加のバッファリングのために停止することなくメディアの最後まで再生するには、充分なデータが読み込まれていないとみられる。
    canplaythrough	ブラウザーがコンテンツのバッファリングのために停止することなく最後までメディアを再生することができるとみられる。
    complete	OfflineAudioContext のレンダリングが終了した。
    durationchange	duration 属性が更新された。
    emptied	メディアが空になった。例えば、このイベントはメディアがすでに読み込まれた (または部分的に読み込まれた) 状態で、再読み込みのために load() メソッドが呼び出された場合など。
    ended	メディアの末尾に達したために再生が停止した。
    loadeddata	メディアの最初のフレームが読み込み終わった。
    loadedmetadata	メタデータを読み込んだ。
    pause	再生が一時停止した。
    play	再生が始まった。
    playing	データがなくなったために一時停止または遅延した後で、再生の再開の準備ができた。
    progress	ブラウザーがリソースを読み込んでいる間に定期的に発生します。
    ratechange	再生レートが変更された。
    seeked	シーク操作が完了した。
    seeking	シーク捜査が始まった。
    stalled	ユーザーエージェントがメディアを読み込もうとしているが、データが予期せずに入ってこない。
    suspend	メディアデータの読み込みが停止した。
    timeupdate	currentTime 属性で示されている時刻が更新された。
    volumechange	音量が変更された。
    waiting	一時的なデータの不足により、再生が停止した。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        AUTOPLAY = 'autoplay'
        AUTOPICTUREINPICTURE = 'autoPictureInPicture'
        BUFFERED = 'buffered'
        CONTROLS = 'controls'
        CROSSORIGIN = 'crossorigin'
        ANONYMOUS = 'anonymous'
        USE_credentials = 'use-credentials'
        CURRENTTIME = 'currentTime'
        DISABLEPICTUREINPICTURE = 'disablePictureInPicture'
        DURATION = 'duration'
        HEIGHT = 'height'
        INTRINSICSIZE = 'intrinsicsize'
        LOOP = 'loop'
        MUTED = 'muted'
        PLAYSINLINE = 'playsinline'
        POSTER = 'poster'
        PRELOAD = 'preload'
        SRC = 'src'

    class AutoPictureInPicture(object):
        """AutoPictureInPicture

        AutoPictureInPicture is a object.
        Responsibility:
        """
        TRUE = 'true'
        FALSE = 'false'

    class ControlsList(object):
        """ControlsList

        ControlsList is a object.
        Responsibility:
        """
        NODOWNLOAD = 'nodownload'
        NOFULLSCREEN = 'nofullscreen'
        NOREMOTEPLAYBACK = 'noremoteplayback'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='video', tags=[], attrs=None, **kwargs)

    def enable_autoplay(self, ):
        """Enable autoplay.

        enable_autoplay()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.AUTOPLAY, None)

    def disable_autoplay(self, ):
        """Disable autoplay.

        disable_autoplay()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.AUTOPLAY in self.attrs:
            del self.attrs[self.AttributeNames.AUTOPLAY]
        return self

    def is_autoplay(self, ):
        """Check autoplay enabled.

        is_autoplay()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.AUTOPLAY in self.attrs

    def set_autopictureinpicture(self, value):
        """Set autopictureinpicture attribute value.

        set_autopictureinpicture(value)

        @Arguments:
        - `value`: autopictureinpicture value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.AUTOPICTUREINPICTURE, value)

    def get_autopictureinpicture(self, ):
        """Get autopictureinpicture attribute value.

        get_autopictureinpicture()

        @Return: autopictureinpicture attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.AUTOPICTUREINPICTURE, None)

    def remove_autopictureinpicture(self, ):
        """Remove autopictureinpicture attribute.

        remove_autopictureinpicture()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.AUTOPICTUREINPICTURE in self.attrs:
            del self.attrs[self.AttributeNames.AUTOPICTUREINPICTURE]
        return self

    def set_buffered(self, value):
        """Set buffered attribute value.

        set_buffered(value)

        @Arguments:
        - `value`: buffered value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.BUFFERED, value)

    def get_buffered(self, ):
        """Get buffered attribute value.

        get_buffered()

        @Return: buffered attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.BUFFERED, None)

    def remove_buffered(self, ):
        """Remove buffered attribute.

        remove_buffered()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.BUFFERED in self.attrs:
            del self.attrs[self.AttributeNames.BUFFERED]
        return self

    def get_controls(self, ):
        """Get controls attribute value.

        get_controls()

        @Return: controls attribute value

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CONTROLS, None)

    def enable_controls(self, ):
        """Enable controls attribute value to On.

        enable_controls()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.CONTROLS, None)

    def remove_controlslist(self, ):
        """Remove controlslist attribute.

        remove_controlslist()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CONTROLSLIST in self.attrs:
            del self.attrs[self.AttributeNames.CONTROLSLIST]
        return self

    def set_controlslist(self, value):
        """Set controlslist attribute value.

        set_controlslist(value)

        @Arguments:
        - `value`: controlslist attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.CONTROLSLIST, value)

    def get_controlslist(self, ):
        """Get controlslist attribute value.

        get_controlslist()

        @Return: controlslist attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CONTROLSLIST, None)

    def set_disablePictureInPicture(self, ):
        """Set disablePictureInPicture.

        set_disablePictureInPicture()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DISABLEPICTUREINPICTURE, None)

    def remove_disablePictureInPicture(self, ):
        """Remove disablePictureInPicture.

        disable_disablePictureInPicture()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DISABLEPICTUREINPICTURE in self.attrs:
            del self.attrs[self.AttributeNames.DISABLEPICTUREINPICTURE]
        return self

    def is_disablePictureInPicture(self, ):
        """Check disablePictureInPicture.

        is_disablePictureInPicture()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.DISABLEPICTUREINPICTURE in self.attrs

    def set_crossorigin(self, value):
        """Set crossorigin attribute value.

        set_crossorigin(value)

        @Arguments:
        - `value`: crossorigin attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORM, value)

    def get_crossorigin(self, ):
        """Get crossorigin attribute value.

        get_crossorigin()

        @Return: crossorigin attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CROSSORIGIN, None)

    def remove_crossorigin(self, ):
        """Remove crossorigin attribute.

        remove_crossorigin()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CROSSORIGIN in self.attrs:
            del self.attrs[self.AttributeNames.CROSSORIGIN]
        return self

    def set_currenttime(self, value):
        """Set currenttime attribute value.

        set_currenttime(value)

        @Arguments:
        - `value`: current time attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.CURRENTTIME, value)

    def get_currenttime(self, ):
        """Get currenttime attribute value.

        get_currenttime()

        @Return: currenttime attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CURRENTTIME, None)

    def remove_currenttime(self, ):
        """Remove currenttime attribute.

        remove_currenttime()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CURRENTTIME in self.attrs:
            del self.attrs[self.AttributeNames.CURRENTTIME]
        return self

    def set_src(self, value):
        """Set src attribute value.

        set_src(value)

        @Arguments:
        - `value`: src attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.SRC, value)

    def get_src(self, ):
        """Get src attribute value.

        get_src()

        @Return: src attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.SRC, None)

    def remove_src(self, ):
        """Remove src attribute.

        remove_src()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.SRC in self.attrs:
            del self.attrs[self.AttributeNames.SRC]
        return self

    def set_height(self, value):
        """Set height attribute value.

        set_height(value)

        @Arguments:
        - `value`: height attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.HEIGHT, value)

    def get_height(self, ):
        """Get height attribute value.

        get_height()

        @Return: height attribute value.

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

    def set_loop(self, value):
        """Set loop attribute value.

        set_loop(value)

        @Arguments:
        - `value`: loop value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.LOOP, value)

    def get_loop(self, ):
        """Get loop attribute value.

        get_loop()

        @Return: loop attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.LOOP, None)

    def remove_loop(self, ):
        """Remove loop attribute.

        remove_loop()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.LOOP in self.attrs:
            del self.attrs[self.AttributeNames.LOOP]
        return self

    def set_muted(self, value):
        """Set muted attribute value.

        set_muted(value)

        @Arguments:
        - `value`: muted value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.MUTED, value)

    def get_muted(self, ):
        """Get muted attribute value.

        get_muted()

        @Return: muted attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MUTED, None)

    def remove_muted(self, ):
        """Remove muted attribute.

        remove_muted()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MUTED in self.attrs:
            del self.attrs[self.AttributeNames.MUTED]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# video.py ends here
