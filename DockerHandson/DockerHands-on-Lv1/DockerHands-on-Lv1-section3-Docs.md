### wodpress環境の構築(データベース×web)
---
#### wordpressコンテナの作成
- wordpressのimageをダウンロード

` docker pull wordpress `

- wordpressコンテナを作成

` docker run --name wordp -p 8080:80 wordpress  `

- [webアクセス](http://127.0.0.1:8080/)
- 以下の工程を実施
  - wordpressの言語選択ページを進める
  - データベース設定値を入力し次ページ
  - データ接続確立エラーが出力される
    - wordpressにデータベース設定をしていないことが原因


#### networkを作成
- wordpressとmysqlのネットワークを作成

` docker network create wordpress_net `

#### detabaseとmysqlを設定
- mysqlで設定が必要な変数
  - rootアカウントのパスワード
  - 初期データベース名
    - mysqlのイメージ生成時に作成されるデータベース名を指定する
  - 作成するROOTではないユーザを生成
    - ユーザー名とパスワードを指定

| command | 説明 |
| - | - |
| -e | 環境変数を設定 |
| MYSQL_ROOT_PASSWORD | mysql rootのパスワード |
| MYSQL_DATABASE | mysqlデータベース名 |
| MYSQL_USER | MYSQLユーザ名 | 
| MYSQL_PASSWORD | MYSQLのパスワード |

` docker run --name mysqldb -dit --net=wordpress_net -e MYSQL_ROOT_PASSWORD=P@ssw0rd -e MYSQL_DATABASE=wordpressdb -e MYSQL_USER=user01 -e MYSQL_PASSWORD=user01pass mysql --character-set-server=utf8 --collation-server=utf8_general_ci --default_authentication_plugin=mysql_native_password `

#### wordpressの起動
- ネットワークを指定してwordpressを起動
- 起動後言語選択をし、データベースの連携設定を実施(以下の表を参考)

| 項目 | 参考変数値 |
| - | - |
| データベース名 | MYSQL_DATABASE | 
| ユーザー名 | MYSQL_USER | 
| パスワード | MYSQL_PASSWORD | 
| データベースのホスト名 | コンテナ名 |

` docker run --name wordp -dit --net=wordpress_net -p 8080:80 wordpress `