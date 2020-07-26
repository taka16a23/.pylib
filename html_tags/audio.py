#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""audio -- audio tag

"""
from .html_tag import HtmlTag


class Audio(HtmlTag):
    """Audio

    Audio is a HtmlTag.
    Responsibility:

    HTML の <audio> 要素は、文書内に音声コンテンツを埋め込むために使用します。
    この要素は、1つまたは複数の音源を含むことができます。
    音源は src 属性または <source> 要素を使用して表し、ブラウザーがもっとも適切な音源を選択します。
    また、 MediaStream を使用してストリーミングメディアを指し示すこともできます。

    上記の例は、 <audio> 要素の単純な使用方法を示しています。
    <img> 要素と同様の方法で、埋め込みたいメディアへのパスを src 属性に設定します。
    他にも自動再生や繰り返しを行うかどうか、ブラウザーの既定のオーディオコントロールを表示したいかどうか、
    などの情報を指定する属性を含めることができます。

    開始および終了タグ <audio></audio> の中のコンテンツは、
    この要素に対応してないブラウザーで代替として表示されます。

    属性
    この要素にはグローバル属性があります。

    autoplay
    論理属性。
    指定された場合、音声ファイル全体のダウンロードの完了を待たずに、
    再生可能な状態になった時点で即座にコンテンツの再生が始まります。
    メモ: 自動的に音声 (あるいは音声トラックを含む動画) を
    再生するサイトはユーザーにとって不快な体験になる可能性がありますので、
    可能な限り避けるべきです。自動再生機能が必須である場合は、
    オプトイン (ユーザーが明示的に有効化することを求める) にするべきです。
    ただし、ユーザーの制御下で後からソースを設定するメディア要素を作成するときは、
    この方法が役に立つでしょう。
    自動再生ガイドには autoplay の正しい使い方についての追加情報があります。

    controls
    この属性が指定された場合、ブラウザーは再生・一時停止、音量、
    シークの各機能を制御するコントロールを表示します。
    <audio controls>

    crossorigin
    この列挙型の属性は、関連する音声ファイルを取得する際に CORS を使用するかを示します。
    CORS が有効なリソース は、汚染されることなく <canvas> 要素で再利用できます。
    次の値が使用できます:
        anonymous
        資格情報を伴わずにオリジン間リクエストを実行します。すなわち、 Cookie や X.509 証明書がない Origin: HTTP ヘッダーを送信する、あるいは HTTP ベーシック認証を行いません。サーバーが元のサイトに信用情報を付与しない場合 (Access-Control-Allow-Origin: HTTP ヘッダーの設定なし)、画像が汚染され、その使用も制限されます。
        use-credentials
        資格情報を伴ってオリジン間リクエストを実行します。
        すなわち、Cookie や X.509 証明書を伴う Origin: HTTP ヘッダーを送信する、
        あるいは HTTP ベーシック認証を行います。
        サーバーが元のサイトに信用情報を付与しない場合
        (Access-Control-Allow-Credentials: HTTP ヘッダーに関わらず)、
        画像が汚染され、その使用も制限されます。
        この属性が存在しない場合、リソースは CORS リクエストなしで (すなわち、 Origin: HTTP ヘッダーなしで) 取得され、 <canvas> 要素での汚染されない使用が妨げられます。これが無効な場合、列挙型のキーワードに anonymous が指定されたものとして扱われます。追加の情報は CORS 設定属性 を参照してください。

    currentTime
    currentTime を読み取ると、倍精度浮動小数点値で、
    現在の音声の再生位置を秒単位で示す値を返します。
    音声のメタデータが利用できない場合—この場合はメディアの開始時刻や長さを知ることが
    できなくなるので— currentTime は再生が始まる時刻を示したり、
    変更したりすることができます。そうでない場合は、 currentTime を設定すると
    現在の再生位置を指定された時刻に設定し、メディアが現在読み込まれていれば、
    その位置にシークします。
    音声がストリーミングである場合は、 ユーザーエージェント は
    データがメディアバッファーからあふれた場合に一部を受け取ることができません。
    他にも音声が0秒から始まらないメディアタイムラインを持っている場合もあり、
    currentTime をそれより前の時刻に設定すると失敗します。
    例えば、音声のメディアタイムラインが12時間目に始まる場合、 currentTime を
    3600 に設定すると、現在の再生位置をメディアの開始位置の前に設定しようとするので、失敗します。
    getStartDate() メソッドは、メディアのタイムラインの参照フレームの開始点を特定するのに
    使用することができます。

    disableRemotePlayback
    論理属性で、有線 (HDMI, DVI, など) や無線技術 (Mirachast, Chromecast, DLNA,
    AirPlay, など) で接続された機器のリモート再生機能を無効にするために使用します。
    詳しくはこの提案中の仕様書をご覧ください。
    Safari では、代替として x-webkit-airplay="deny" を使用することができます。

    duration 読取専用
    倍精度浮動小数点値で、メディアのタイムライン上の音声の長さ (合計の長さ) を秒単位で示します。
    要素上にメディアがない場合や、メディアが有効でない場合は、返値は NaN になります。
    メディアの終わりが分からない場合 (長さの分からないライブストリーミング、ウェブラジオ、
    WebRTC から来たメディアなど)、この値は +Infinity になります。

    loop
    論理型の属性です。指定された場合、音声プレイヤーは音声の末尾に達すると、
    自動的に先頭に戻ります。

    muted
    論理型の属性で、音声の既定の設定を示します。
    この属性を設定すると、初期状態が消音になります。
    既定値は false です。

    preload
    列挙型の属性で、ユーザーに取って最良の結果をもたらすと作者が考えていることのヒントを
    ブラウザーに伝えるためのものです。以下の値のうちひとつを持つことができます。

      none: 音声を事前に読み込むべきではないことを示します。
      metadata: 音声のメタデータ (例えば、長さ) を読み込みます。
      auto: ユーザーが音声ファイルを使用しないと思われる場合でも、
             ファイル全体をダウンロードしてよいことを示します。
      空文字列: これは auto 値と同義です。
      既定値はブラウザーによって異なります。仕様書では metadata にするよう助言しています。

      使用上のメモ:
      autoplay 属性は preload より優先します。autoplay を指定すると、
               言うまでもなくブラウザーは音声を再生するためにダウンロードを
               始めなければなりません。
      仕様書は、ブラウザーがこの属性の値に従うことを強制していません。
      これは単なるヒントです。

    src
    埋め込む音声コンテンツの URL を指定します。
    なお、この属性は HTTP access controls に従います。
    この属性を省略し、audio 要素の子要素として配置した <source> 要素と
    その src 属性を用いて指定することも可能であり、その場合、これを複数設置することで、
    異なるタイプの複数の代替コンテンツを配置することが可能となります。

    イベント:
    audioprocess ScriptProcessorNode の入力バッファが処理可能になった。
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
    ratechange	再生レートが変更された。
    seeked	シーク操作が完了した。
    seeking	シーク操作が始まった。
    stalled	ユーザーエージェントがメディアを読み込もうとしているが、データが予期せずに入ってこない。
    suspend	メディアデータの読み込みが停止した。
    timeupdate	currentTime 属性で示されている時刻が更新された。
    volumechange	音量が変更された。
    waiting	一時的なデータの不足により、再生が停止した。

    使用上のメモ:
    ブラウザーはすべてが同じファイル形式および音声形式に対応しているわけではありません。
    内部に含められた <source> 要素で複数のソースを提供することができ、
    ブラウザーは理解できる最初のものを使用します。

    <audio controls>
      <source src="myAudio.mp3" type="audio/mpeg">
      <source src="myAudio.ogg" type="audio/ogg">
        <p>Your browser doesn't support HTML5 audio. Here is
         a <a href="myAudio.mp4">link to the audio</a> instead.</p>
    </audio>

    他の使用上のメモ:

    controls 属性を指定しない場合、音声プレイヤーはブラウザーの既定のコントロールを含めません。
    JavaScript と HTMLMediaElement API を使用して、
    独自のカスタムコントロールを作成することができます。
    音声コンテンツを詳細に制御できるように、 HTMLMediaElement はさまざまなイベントを発行します。
    これは音声の読み込みプロセスを監視する方法も提供するので、エラーを監視したり、
    再生や捜査を始めることができるようになったことを検出したりすることができます。
    Web Audio API を使用すると、既存の音声ファイルのストリーミングではなく、
    JavaScript コードから音声ストリームを直接生成および操作することもできます。
    <audio> 要素は <video> 要素と同じような方法で字幕を持つことができません。
    Ian Devlin による WebVTT and Audio で、役立つ情報や作業があります。
    HTML の <audio> 要素の使用に関する良い情報源として、
    映像および音声コンテンツの初心者向けチュートリアルがあります。

    CSS でのスタイル付け
    <audio> 要素は既定では固有の視覚的な出力を持ちませんが、 controls 属性が指定されると、ブラウザーの標準のコントロールが表示されます。

    既定のコントロールは display の値に既定で inline を持っており、テキストブロックなどの中に置いておきたい場合でない限り、配置やレイアウトを制御しやすくするために、値を block に設定することは、多くの場合は良い考えです。

    既定のコントロールは、ブロックを単位としてて影響するプロパティでスタイル付けすることができるので、 border や border-radius, padding, margin 等を指定することができます。しかし、音声プレイヤー内の個別のコンポーネントはスタイル付けすることができず (例えば、ボタンの寸法やアイコンの変更、フォントの変更など)、またコントロールはブラウザーごとに異なります。

    ブラウザー間で一貫したルック＆フィールを実現するには、カスタムコントロールを作成する必要があるでしょう。これは好きな方法でマークアップおよびスタイル付けをすることができ、 JavaScript と HTMLMediaElement API を使用することで、これらの機能を結合することができます。

    動画プレイヤーのスタイル付けの基本は、便利なスタイル付けテクニックをいくつか紹介しています。これは <video> の文脈で書かれたものですが、多くは <audio> にも同様に適用されます。

    トラックの追加と削除の検出
    addtrack および removetrack イベントを用いると、 <audio> 要素でトラックが追加されたり削除されたりしたことを検出することができます。しかし、これらのイベントは <audio> 要素自身に直接送信されるわけではありません。代わりに、 <audio> の HTMLMediaElement 内にある、要素に追加されたトラックの種類に対応するトラックリストオブジェクトに送信されます。

    HTMLMediaElement.audioTracks
    メディア要素のオーディオトラックのすべてを含む AudioTrackList です。 addtrack のリスナーをこのオブジェクトに追加すると、新しいオーディオトラックが要素に追加された時に通知を受け取ることができます。
    HTMLMediaElement.videoTracks
    この VideoTrackList オブジェクトに addtrack リスナーを追加することで、要素に動画トラックが追加されたときに通知を受け取ることができます。
    HTMLMediaElement.textTracks
    この TextTrackList オブジェクトに addtrack リスナーを追加することで、要素にテキストトラックが追加されたときに通知を受け取るkとができます。
    メモ: <audio> 要素であっても、動画やテキストトラックリストを持っており、インターフェイスの実装の使用が奇妙に見えますが、実際に動画を表示するために使用することができます。

    例えば、次のようなコードで <audio> 要素で音声トラックが追加されたり削除されたりしたときを検出することができます。

    var elem = document.querySelector("audio");

    elem.audioTrackList.onaddtrack = function(event) {
      trackEditor.addTrack(event.track);
    };

    elem.audioTrackList.onremovetrack = function(event) {
      trackEditor.removeTrack(event.track);
    };
    このコードは音声トラックが要素で追加および削除されることを監視し、トラックエディターの論理関数を呼び出すことで、エディターにおける利用できるトラックの一覧でトラックを登録や削除を行います。

    addtrack および removetrack イベントを監視するには、 addEventListener() を使用することもできます。

    基本的な使用法
    以下の例は <audio> 要素で OGG ファイルを再生する単純な例を示しています。ページで許可されていれば、 autoplay 属性によって自動再生され、代替コンテンツも含んでいます。

    <!-- シンプルな音声再生 -->
    <audio src="AudioTest.ogg" autoplay>
    あなたのブラウザーは <code>audio</code> 要素に対応していません。
    </audio>
    いつ自動再生が動作するのか、自動再生を使用する許可の取得方法、いつどのように自動再生を使用するのが適切であるのかについては、自動再生ガイドをご覧ください。

    <source> 要素を伴う <audio> 要素
    この例では、埋め込まれる音声トラックを、 <audio> 要素の直接の src 属性ではなく、内部の <source> 要素のものを使用して指定しています。これは type 属性の中でファイルの MIME タイプを含めることで、ブラウザーがそのファイルを再生できるかどうかを知ることができ、そのファイル再生できないときに時間を浪費しません。

    <audio controls>
      <source src="foo.wav" type="audio/wav">
    あなたのブラウザーは <code>audio</code> 要素に対応していません。
    </audio>
    複数の <source> 要素を持つ <audio>
    この例は複数の <source> 要素を含んでいます。ブラウザーは最初の source 要素 (Opus) を読み込もうとします。再生することができれば、2番目 (vorbis) と3番目 (mp3) の読み込みは行われません。

    <audio controls>
    <source src="foo.opus" type="audio/ogg; codecs=opus"/>
    <source src="foo.ogg" type="audio/ogg; codecs=vorbis"/>
    <source src="foo.mp3" type="audio/mpeg"/>
    </audio>
    アクセシビリティの考慮事項
    台詞のある音声には、実際にコンテンツを説明する字幕と文字化情報transcriptを提供するべきです。 WebVTT を使用して字幕を指定すると、聴力を失った人が、音声の再生時に音声の内容を理解する事ができるようになるのに対し、文字化情報を使用すると、録音されたコンテンツを理解するのに時間が掛かる人が、自分に合ったペースと書式で録音の内容を確認できるようになります。

    自動字幕サービスが使用されている場合は、生成されたコンテンツが元の音声を正しく表現しているかを確認することが重要です。

    <audio> 要素は直接 WebVTT に対応していません。機能を提供するライブラリまたはフレームワークを探すか、字幕を表示するコードを自分自身で書くかする必要があります。一つの選択肢として、 <video> 要素が WebVTT に対応しているので、これで音声を再生するというものもあります。

    字幕や文字化情報では、話されるセリフに加えて、重要な情報を伝える音楽や音響効果も識別できるようにしてください。これには感情や口調も含みます。例えば、以下の WebVTT では、角括弧を使用して口調や感情を閲覧者に示しています。これによって音楽、物音、効果音などの雰囲気を確立するのに役立ちます。

    1
    00:00:00 --> 00:00:45
    [エネルギチックなテクノ音楽]

    2
    00:00:46 --> 00:00:51
    タイムキーパーのポッドキャストのようこそ！このエピソードでは、私たちはどちらのスイス時計が腕時計かを議論します？

    16
    00:00:52 --> 00:01:02
    [笑い] ごめん！言いたかったのは、どの腕時計がスイスの腕時計か？です。
    また、 <audio> 要素に対応していないブラウザーを使用している閲覧者向けのフォールバックとしていくらかのコンテンツ (直接ダウンロードするリンクなど) を提供するのは良い習慣です。

    <audio controls>
    <source src="myAudio.mp3" type="audio/mpeg">
    <source src="myAudio.ogg" type="audio/ogg">
    <p>
    Your browser doesn't support HTML5 audio.
    Here is a <a href="myAudio.mp4">link to download the audio</a> instead.
    </p>
    </audio>

    技術的概要
    コンテンツカテゴリ	フローコンテンツ、記述コンテンツ、埋め込みコンテンツ。 controls 属性を持つ場合は、対話型コンテンツと知覚可能コンテンツ。
    許可されている内容	要素が src 属性を持つ場合: 0個以上の <track> 要素とそれに続く、メディア要素を含まない透過的コンテンツ。すなわち <audio> 要素や <video> を子要素として配置してはなりません。
    その他の場合: 0個以上の <source> 要素、0個以上の <track> 要素、メディア要素を含まない透過的コンテンツ。すなわち <audio> 要素や <video> を子要素として配置してはなりません。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	埋め込みコンテンツを受け入れるすべての要素。
    暗黙の ARIA ロール	対応するロールなし
    許可されている ARIA ロール	application
    DOM インターフェイス	HTMLAudioElement
    """
    class AttributeNames(HtmlTag.AttributeNames):
        """AttributeNames

        AttributeNames is a HtmlTag.AttributeNames.
        Responsibility:
        """
        AUTOPLAY = 'autoplay'
        CONTROLS = 'controls'
        CROSSORIGIN = 'crossorigin'
        CURRENTTIME = 'currentTime'
        DISABLEREMOTEPLAYBACK = 'disableRemotePlayback'
        DURATION = 'duration'
        LOOP = 'loop'
        MUTED = 'muted'
        PRELOAD = 'preload'
        SRC = 'src'

    class CrossOrigin(object):
        """CrossOrigin

        CrossOrigin is a object.
        Responsibility:
        """
        ANONYMOUS = 'anonymous'
        USE_CREDENTIALS = 'use-credentials'

    class Muted(object):
        """Muted

        Muted is a object.
        Responsibility:
        """
        TRUE = 'true'
        FALSE = 'false'

    class Preload(object):
        """Preload

        Preload is a object.
        Responsibility:
        """
        NONE = 'none'
        METADATA = 'metadata'
        AUTO = 'auto'
        BLANK = ''

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='audio', tags=[], attrs=None, **kwargs)

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

    def enable_controls(self, ):
        """Enable controls.

        enable_controls()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.CONTROLS, None)

    def disable_controls(self, ):
        """Disable controls.

        disable_controls()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CONTROLS in self.attrs:
            del self.attrs[self.AttributeNames.CONTROLS]
        return self

    def is_controls(self, ):
        """Check controls enabled.

        is_controls()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.CONTROLS in self.attrs

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

    def disable_remote_playback(self, ):
        """Disable remote playback attribute .

        disable_remove_playback()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DISABLEREMOTEPLAYBACK, None)

    def enable_remote_playback(self, ):
        """Enable remote playback.

        enable_remote_playback()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DISABLEREMOTEPLAYBACK in self.attrs:
            del self.attrs[self.AttributeNames.DISABLEREMOTEPLAYBACK]
        return self

    def is_disable_remote_playback(self, ):
        """Check disabled remote playback.

        is_disable_remote_playback()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.DISABLEREMOTEPLAYBACK in self.attrs

    def set_duration(self, value):
        """Set duration attribute value.

        set_duration(value)

        @Arguments:
        - `value`: duration value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DURATION, value)

    def get_duration(self, ):
        """Get duration attribute value.

        get_duration()

        @Return: duration attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.DURATION, None)

    def remove_duration(self, ):
        """Remove duration attribute.

        remove_duration()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DURATION in self.attrs:
            del self.attrs[self.AttributeNames.DURATION]
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

    def set_preload(self, value):
        """Set preload attribute value.

        set_preload(value)

        @Arguments:
        - `value`: preload attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.PRELOAD, value)

    def get_preload(self, ):
        """Get preload attribute value.

        get_preload()

        @Return: preload attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.PRELOAD, None)

    def remove_preload(self, ):
        """Remove preload attribute.

        remove_preload()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.PRELOAD in self.attrs:
            del self.attrs[self.AttributeNames.PRELOAD]
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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# audio.py ends here
