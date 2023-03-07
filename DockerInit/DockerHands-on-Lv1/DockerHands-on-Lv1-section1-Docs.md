本資料は[docker実行環境](https://github.com/GitEngHar/GrowTheLatestTechnorogy/blob/main/docker-start.md)がセットアップされていることを前提とした資料になります。

### webサーバの構築
#### コンテナを作成する流れ
1. コンテナの元になるファイル(image)をダウンロード
1. imageを使ってコンテナを作成
1. 動作テスト

#### imageの取得

```
docker image pull httpd
```

#### コンテナの起動
| command | 説明 |
| - | - |
| docker run IMAGENAME | 新しいコンテナでコマンドを実行。イメージ名。 | 
| -d | バックグラウンドで動作 | 
| -it | 標準出力(ターミナル)に実行結果を表示 |
| -p | ホストからコンテナ:コンテナのlistenポート | 
| --name| コンテナ名を指定 |

```
docker run --name web-test -d -p 8080:80 httpd
```

#### 動作確認
- 動作コンテナ確認
  - 実行結果に対象のコンテナがあれば作成完了 
```
docker ps

CONTAINER ID   IMAGE     COMMAND              CREATED          STATUS          PORTS                  NAMES
99f64763113e   httpd     "httpd-foreground"   45 minutes ago   Up 45 minutes   0.0.0.0:8080->80/tcp   web-test
```
- [webアクセス](http://127.0.0.1:8080/)