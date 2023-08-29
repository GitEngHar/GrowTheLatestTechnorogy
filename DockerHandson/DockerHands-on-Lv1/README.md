# DockerHands-on-Lv1の目的

あなたの成果物 を考えひな形を制作し、ひな形を更新します。

## 何を作るのか

DockerHands-onでは自己紹介ページの制作をします

## 実行環境

[Docker Playground](https://labs.play-with-docker.com/)で実施します

## 進め方

### ①どんな自己紹介ページを制作するか考えよう

あなたがエンジニアとして他の人に紹介するときの要素を盛り込んだ自己紹介ページを作成してみましょう

そのため、以下を考える必要があります

1. 誰に見せるのか
1. どんな情報を盛り込むのか
1. どんな見た目のサイトになるのか

内容を決めたらサイトの見た目を html で作成しましょう(例ではGLTのQ&Aを制作しています。項目と答えがある形式であれば何でも良いです)

#### 作成例 GLT Q&Aページ
![image](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/d870dc3d-7e59-4eb6-bd0e-cfd436ed826b)

<details>
<summary> Q&Aのhtml </summary>

```
<!doctype html>
  <html  lang="en">
  <head>
    <title>GltDockerHandsOn</title>
  </head>
  <style type="text/css">
    <!--
    #QandA-1 {
      width: 100%;
      font-family: メイリオ;
      font-size: 14px; /*全体のフォントサイズ*/
    }
    #QandA-1 h2 {
    
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

### ②webサーバの構築

作成途中...

DockerHands-on-Lv0で実施した内容と同じです

### ③ひな形の作成

作成途中..
