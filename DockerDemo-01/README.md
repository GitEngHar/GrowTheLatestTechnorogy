# アラート通知デモ

## はじめに

## 構成図

## デモンストレーション
- 監視システムの立ち上げ ([バックとフォアの動作差異詳細](https://docs.docker.jp/engine/reference/run.html))
  - docker-compose up -d
  - docker-compose -f docker-compose.yml up -d
- 監視システムの確認
  - prometheus
    - [http://localhost:9090](http://localhost:9090)
  - aleartmanager
    - [http://localhost:9093](http://localhost:9093)
  - wordpress
    - [http://localhost:8080](http://localhost:8000)
   - cadvisor 
    - [http://localhost:8080](http://localhost:8080)
- アラート発生
  - docker stop wordpress_1

## 利用したDocker技術要素

## +αでやりたいと思ったこと
- Screwdriverを用いた自動デプロイ
