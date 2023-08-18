# 目的
画像にあるDockerがコンテナを設置するまでの流れを理解する

## 前提条件
[GLT-Reserve](https://github.com/GitEngHar/GrowTheLatestTechnorogy/tree/main/GLT-Reserve)を終えていること

## 実行環境
[Docker Playground](https://labs.play-with-docker.com/)で実施します

## Dockerライフサイクルを学ぶ
### ライフサイクルの全体図
![docker ライフサイクル図](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/cfa408a3-0734-423a-b6e7-7479107c1499)


[Link](https://lucid.app/lucidchart/866ecd6c-b04d-4d22-85b8-05d3eb88be21/edit?invitationId=inv_000ea0a9-a973-4597-82b9-347d42da4e5f&page=0_0#)

### ライフサイクルの説明
![image](https://user-images.githubusercontent.com/119464648/227698270-fb13cfda-f57c-4687-959d-bb35512e15da.png)


### 手を動かして学ぶ

webサーバのコンテナを作成してサイトを表示しよう

#### ①imageファイルを取得する

| コマンド       | 説明                 |
|------------|--------------------|
| docker     | docker機能を利用するコマンド  |
| image pull | imageファイルを取得するコマンド |

`docker pull httpd` を実行してImageファイルを取得する。

```
$ docker pull httpd
latest: Pulling from library/httpd
docker.io/library/httpd:latest
```

#### ②webサーバコンテナを作成し起動する

| コマンド                | 説明                   |
|---------------------|----------------------|
| run                 | imageを指定してコンテナを作成、起動するコマンド |
| -p DockerHostアドレス:ホストポート:コンテナポート | コンテナに接続するアドレスとポート番号を設定   |
| -d | コンテナプロセスが裏側で動作します。設定しないと表側で動作、ターミナルを占有します。   |

` docker run -d -p 8080:80 httpd `を実行して`httpd` imageを使ってコンテナを作成、起動する。

```
$ docker run -d -p 8080:80 httpd
36e334489a262a89372ebb4a9a6bbcf6d449eaeff5780188fcfb8c3fb473e1e7
```


#### ③コンテナの動作を確認する

| コマンド       | 説明                 |
|------------|--------------------|
| ps | コンテナの一覧を表示 |

` docker ps `を実行して作成したコンテナを確認する

```
$  docker ps
CONTAINER ID   IMAGE     COMMAND              CREATED          STATUS          PORTS                    NAMES
36e334489a26   httpd     "httpd-foreground"   11 minutes ago   Up 11 minutes   127.0.0.1:8080->80/tcp   cool_black
```

#### ④起動したwebサーバのコンテナにアクセス！サイトを表示してみる
![image](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/2eecb9ca-a808-447c-9b94-620487b0f608)

1. 「OPEN PORT」のボタンを押下
2.  画面上部に表示されたポップの入力欄に「8080」を入力
3. 「OK」のボタンを押下

成功すると以下のような画面が表示されます

![image](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/35d827dd-c225-49da-bde9-09a117f5c9b0)

