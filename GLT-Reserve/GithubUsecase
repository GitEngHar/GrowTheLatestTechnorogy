# 概要
GLTではGithubを利用しコンテンツ制作等を行っていきます

以下に機能イメージがつくよう、要望ごとのGithubの機能を紹介します。

## 制作物の過程を記録したい・バグを改修した記録を残したい
[Issue機能](https://github.com/GitEngHar/GrowTheLatestTechnorogy/issues)を用いて掲示板のように記録を蓄積できます

Issueの例を見ると用途が想像しやすいとおもわれます。([こちら](https://github.com/GitEngHar/GrowTheLatestTechnorogy/issues/1)から確認)

## 制作物をGithubへアップロードしたい
制作物をコミュニティで掲載する前に内容を確認し、バグがないか & 要件を満たせているかなど確認する必要があります

コミュニティで掲載されるためには main というブランチに反映する必要があります(mainブランチは木の幹だと思ってください)

![image](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/6d8210b6-fc57-4979-8c4c-273350368054)

main に 反映する前に反映してもよいか内容を確認する必要があります。そのため、反映したい変更内容を記録している main ではないブランチが必要です(他ブランチは木の枝のようなものです)

内容を確認し問題なければ変更点をmainに合流(marge)させ、ブランチの変更点が main に反映されます。(木の枝が幹に合体されるのは想像しずらいかも)

変更点を確認するためのレビューがPullRequest(通称PR)です
PRの例は[こちら](https://github.com/GitEngHar/GrowTheLatestTechnorogy/pull/21)にあります

## GitHubのリポジトリ(ソースコード等)をLocalに取得したい
リポジトリをCloneすることでローカル環境にソースコード等をコピーできます

![image](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/04488073-768a-4d7a-bda2-d4c094655328)

上画像中の ` https://~省略~ ` をコピーし以下のようにローカルへコピーできます

docker環境でgithubを扱う想定なのでコマンドのInstallは不要です。前述で紹介してある環境ではgitコマンドが初めから利用できます

```
$ git clone https://github.com/GitEngHar/GrowTheLatestTechnorogy.git
```

## 成果物をGithub(webのgit)にアップロードしたい

認証にはTokenを作成する必要があるため、[こちら](https://capybara-notebook.com/github_accesstoken/)を参考に作成してください。

実際には以下のようにUser名とパスワードを聞かれるので、User名は自分のGithubアカウント名を入力し、パスワードにはToken値を入力すると良いです。
```
Username for 'https://github.com': GitEngHar(ユーザ名)
Password for 'https://ユーザー名@github.com': Token値
```
