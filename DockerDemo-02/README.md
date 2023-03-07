# ログ検索

## はじめに
DockerDemo-02 はコンテナのログをSplunkへ転送し目的のログを探すデモンストレーションになります

## 構成図

## 利用する技術要素
- docker plugin
  - Dockerの機能を拡張する。詳しくは[こちら](https://docs.docker.jp/engine/extend/plugins.html)
- splunk
  - ログ解析・管理ツール。ログを集中管理できる。
  - 検索して目的のログを探すことができるよ！

## 説明
| オプション | 説明 |
| -- | -- |
| --log-driver=splunk-logging-plugin |  |
| --log-opt splunk-token=af615c43-4d80-48d8-9463-3fbcf1049c4f | |
| --log-opt splunk-url=https://172.19.0.3:8088 | |
| --log-opt splunk-insecureskipverify=true | |
| --log-opt splunk-index=docker | |

## デモンストレーション
- 