# ログ検索

## はじめに
DockerDemo-02 はコンテナのログをSplunkへ転送し目的のログを探すデモンストレーションになります

## 構成図

## 説明
| オプション | 説明 |
| -- | -- |
| --log-driver=splunk-logging-plugin | |
| --log-opt splunk-token=af615c43-4d80-48d8-9463-3fbcf1049c4f | |
| --log-opt splunk-url=https://172.19.0.3:8088 | |
| --log-opt splunk-insecureskipverify=true | |
| --log-opt splunk-index=docker | |