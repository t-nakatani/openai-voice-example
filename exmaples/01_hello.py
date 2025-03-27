import openai
import pygame


def text_to_speech(text, output_file="output.mp3"):
    # テキストを音声に変換
    response = openai.audio.speech.create(
        model="tts-1",  # または "tts-1-hd" でより高品質な音声
        voice="shimmer",  # 利用可能な声: alloy, echo, fable, onyx, nova, shimmer
        input=text,
    )

    # 音声ファイルを保存
    response.stream_to_file(output_file)
    return output_file


def play_audio(file_path):
    # pygameを初期化
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)

    # 音声を再生
    pygame.mixer.music.play()

    # 再生が終わるまで待機
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# メイン処理
if __name__ == "__main__":
    # 「こんにちは」を音声に変換
    text = "こんにちは、今日のニュースをお伝えします。"
    output_file = text_to_speech(text)

    # 音声を再生
    print(f"「{text}」を再生します...")
    play_audio(output_file)
