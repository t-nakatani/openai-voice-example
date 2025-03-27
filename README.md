# OpenAI Voice アシスタントサンプル

このプロジェクトは、OpenAI の音声API を使用した簡単な音声アシスタントの実装例です。

## 機能

- 音声入力によるアシスタントとの対話
- 天気情報の取得機能
- 日本語サポート（日本語で話しかけると自動的に日本語エージェントにハンドオフ）

## ファイル構成

- `main.py` - メインエントリーポイント
- `agents_config.py` - エージェントの設定と初期化
- `tools.py` - 関数ツールの定義
- `audio_utils.py` - オーディオ処理ユーティリティ
- `requirements.txt` - 依存関係リスト

## セットアップ

1. 必要なライブラリをインストールします：

```bash
pip install -r requirements.txt
```

2. プログラムを実行します：

```bash
python main.py
```

## 注意事項

- このプログラムを実行するには、OpenAIアカウントとAPIキーが必要です。
- 環境変数 `OPENAI_API_KEY` に適切なAPIキーを設定する必要があります。
