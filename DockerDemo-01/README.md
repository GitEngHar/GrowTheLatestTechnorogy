# アラート通知デモ

## はじめに

## 構成図
![構成図](https://user-images.githubusercontent.com/119464648/215912438-289c8e2c-98b8-4e29-ad2c-4eb69482f7d4.png)

## デモンストレーション
- 監視システムの立ち上げ ([バックとフォアの動作差異詳細](https://docs.docker.jp/engine/reference/run.html))
  - docker-compose -f docker-compose.yml up -d
  - docker-compose up -d  
- 監視システムの確認
  - prometheus
    - [http://localhost:9090](http://localhost:9090)
  - aleartmanager
    - [http://localhost:9093](http://localhost:9093)
  - wordpress
    - [http://localhost:8000](http://localhost:8000)

- アラート発生
  - docker stop wordpress_1

## 利用したDocker技術要素
- [docker-compose.yml](https://docs.docker.jp/compose/overview.html)
- 
## 今後のやりたいこと
- Screwdriverを用いた自動デプロイ
- スマートにコンテナのメトリクスを取得する方法があれば知りたいですmm
