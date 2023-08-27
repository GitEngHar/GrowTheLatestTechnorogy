#### マウント(共有ボリューム 永続化)
##### コンテナで設定されているDocumentルート先を調べる
- docker exec -it web-test bash
- cat /usr/local/apache2/conf/httpd.conf | grep -e Document
  - > /usr/local/apache2/htdocs
- exit
- コンテナを削除( 次のセクションで新しいコンテナを作成するため )
  - ` docker rm web-test `


##### Documentルート設定ディレクトリをマウントしindex.htmlの設置
- dockerのディレクトリをマウントして共有ディレクトリを持つ
  - local環境(windows,mac)のdocker実行ディレクトリにsource_dirを作成

` docker run -d -it --name web-test -p 8080:80 --mount type=bind,source=${pwd}\source_dir,target=調べたDocumentルート先 httpd `

- source_dirにindex.htmlを作成(中身を適当に書く)
- [webアクセス](http://127.0.0.1:8080/)
index.htmlの中身が表示されれば成功