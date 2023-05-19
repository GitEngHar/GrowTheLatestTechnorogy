### 目的
画像にあるDockerがコンテナを設置するまでの流れを理解する

### 内容
取り掛かる前にDockerセットアップ☞[docker実行環境](https://github.com/GitEngHar/GrowTheLatestTechnorogy/blob/main/docker-start.md)

#### Docker Appに接続まで
![docker ライフサイクル図 (2)](https://github.com/GitEngHar/GrowTheLatestTechnorogy/assets/119464648/663c31cc-01a3-48ed-85b6-aa55507815d2)


[Link](https://lucid.app/lucidchart/866ecd6c-b04d-4d22-85b8-05d3eb88be21/edit?invitationId=inv_000ea0a9-a973-4597-82b9-347d42da4e5f&page=0_0#)

#### ライフサイクルの説明
![image](https://user-images.githubusercontent.com/119464648/227698270-fb13cfda-f57c-4687-959d-bb35512e15da.png)


### やってみよう

webサーバのコンテナを作成して動作確認をする

imageファイルを取得してコンテナを作成しよう


1. imageファイルを取得する

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

2. webサーバコンテナを作成し起動する

| コマンド                | 説明                   |
|---------------------|----------------------|
| run                 | imageを指定してコンテナを作成、起動するコマンド |
| -p DockerHostアドレス:ホストポート:コンテナポート | コンテナに接続するアドレスとポート番号を設定   |
| -d | コンテナプロセスが裏側で動作します。設定しないと表側で動作、ターミナルを占有します。   |

` docker run -d -p 127.0.0.1:8080:80 httpd `を実行してコンテナを作成して起動する。

```
$ docker run -d -p 127.0.0.1:8080:80 httpd
36e334489a262a89372ebb4a9a6bbcf6d449eaeff5780188fcfb8c3fb473e1e7
```


3. コンテナの動作を確認する

| コマンド       | 説明                 |
|------------|--------------------|
| ps | コンテナの一覧を表示 |

` docker ps `を実行して作成したコンテナを確認する

```
$  docker ps
CONTAINER ID   IMAGE     COMMAND              CREATED          STATUS          PORTS                    NAMES
36e334489a26   httpd     "httpd-foreground"   11 minutes ago   Up 11 minutes   127.0.0.1:8080->80/tcp   cool_black
```

webコンテナにアクセスする
http://127.0.0.1:8080
