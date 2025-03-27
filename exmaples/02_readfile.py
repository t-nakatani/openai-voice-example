import openai
import pygame


def read_text_from_file(file_path):
    """ファイルからテキストを読み取る"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def text_to_speech(text, output_file="output.mp3"):
    """テキストを音声に変換"""
    response = openai.audio.speech.create(
        model="tts-1",  # または "tts-1-hd" でより高品質な音声
        voice="nova",  # 日本語によく合う声を選択
        input=text,
    )

    # 音声ファイルを保存
    response.stream_to_file(output_file)
    return output_file


def play_audio(file_path):
    """音声ファイルを再生"""
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)

    print("音声再生中...")
    pygame.mixer.music.play()

    # 再生が終わるまで待機
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# メイン処理
if __name__ == "__main__":
    # 読み取るファイルのパス
    input_file = "data/react-state-management.md"  # 適宜変更してください

    try:
        # ファイルからテキストを読み取る
        text = read_text_from_file(input_file)
        print(f"ファイル '{input_file}' からテキストを読み込みました")

        # テキストを音声に変換
        output_file = text_to_speech(text)
        print(f"テキストを音声に変換しました: {output_file}")

        # 音声を再生
        play_audio(output_file)

    except FileNotFoundError:
        print(f"エラー: ファイル '{input_file}' が見つかりません")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
