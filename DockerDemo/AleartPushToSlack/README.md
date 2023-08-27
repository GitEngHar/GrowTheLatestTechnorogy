# アラート通知デモ

## はじめに
DockerDemo-01 はwordpressが動作しているコンテナのメトリクスを監視し、Slackにアラートを通知するデモになります。
dockerで指定された構成を組むにあたっての基本を学ぶことができます。

## 構成図
![構成図](https://user-images.githubusercontent.com/119464648/215913640-13fcf3eb-1cd3-4ad6-9a8a-e7eef123b9b4.png)

## デモンストレーション
- 監視システムの立ち上げ ([バックとフォアの動作差異詳細](https://docs.docker.jp/engine/reference/run.html))
  - docker-compose up -d  
- wordpresコンテナでexporterを起動

```
$ docker exec -it wordpress bash  

$ bash -c "tar xvfz /root/node_exporter-1.5.0.linux-amd64.tar.gz &&
./node_exporter-1.5.0.linux-amd64/node_exporter"
```

- 監視システムの確認
  - prometheus
    - [http://localhost:9090](http://localhost:9090)
  - aleartmanager
    - [http://localhost:9093](http://localhost:9093)
  - wordpress
    - [http://localhost:8000](http://localhost:8000)

- アラート発生
  - docker stop wordpress

## 参考リンク
- [docker-compose.ymlについて](https://docs.docker.jp/compose/overview.html)
- [SlackWebhook作成方法](https://qiita.com/vmmhypervisor/items/18c99624a84df8b31008)
- [Prometheusでアプリケーションを監視してみよう](https://iij.github.io/bootcamp/cicd_infra/prometheus/#_0-1-%E6%83%B3%E5%AE%9A%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E5%8F%97%E8%AC%9B%E8%80%85)
- [DockerでPrometheus, Grafana, Alertmanagerを動かす](https://qiita.com/samskeyti/items/fbe8b78e47a5e4d6842a)

## 今後のやりたいこと
- Screwdriverを用いた自動デプロイ
- スマートにコンテナのメトリクスを取得する方法があれば知りたいですmm
