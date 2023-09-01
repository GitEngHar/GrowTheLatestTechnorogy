# PC上で自己紹介ページを制作してみよう

あなたがエンジニアとして他の人に紹介するときの自己紹介ページを作成してみましょう  
まずは、以下の要素を考えてみましょう (ページ制作は本筋ではないので簡素なもので大丈夫です)

1. 誰に見せるのか
1. どんな情報を盛り込むのか

自己紹介ページは以下を参考にしてみてください

- [【HTML初心者入門】メモ帳でホームページを作成する方法！ - WEBCAMP MEDIA](https://web-camp.io/magazine/archives/7725)

※ 注意点 `<meta charset="UTF-8">` を設定しない場合webページが文字化けするので気を付けてください

- [参考](https://web-camp.io/magazine/archives/96334)

## 作成例 GLT Q&Aページ

![image](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/9a737438-4cfc-4669-b41c-f195f5f7d248)

<details>

<summary> Q&Aのhtml </summary>

```html
<!doctype html>
  <html  lang="ja">
  <head>
    <meta charset="UTF-8">
    <title>GltDockerHandsOn</title>
  </head>
  <style type="text/css">
    <!--
    #QandA-1 {
      width: 100%;
      font-family: メイリオ;
      font-size: 14px; /*全体のフォントサイズ*/
    }
    #QandA-1 dt {
      background: #444; /* 「Q」タイトルの背景色 */
      color: #fff; /* 「Q」タイトルの文字色 */
      padding: 8px;
      border-radius: 2px;
    }
    #QandA-1 dt:before {
      content: "Q.";
      font-weight: bold;
      margin-right: 8px;
    }
    #QandA-1 dd {
      margin: 24px 16px 40px 32px;
      line-height: 140%;
      text-indent: -24px;
    }
    #QandA-1 dd:before {
      content: "A.";
      font-weight: bold;
      margin-right: 8px;
    }
    -->
  </style>
  <body>
    <h1>GLTの Q&A</h1>
    <div id="QandA-1">
      <dl>
        <dt>GLTは何をするの?</dt>
        <dd>技術を楽しむコンテンツを体験します<br>開発者としてコンテンツの制作や魅力あふれるデモンストレーションを作成いただけると嬉しいです</dd>
        <dt>GLTは何の略称??</dt>
        <dd>Grow the Latest Technology</dd>
        <dt>GLTは誰でも参加できるの??</dt>
        <dd>どなたでも参加可能です<br></dd>
      </dl>    
    </div>
    <footer></footer>    
  </body>
</html>
```
  
</details>
