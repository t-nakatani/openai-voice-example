import asyncio

from agents.voice import (
    AudioInput,
    SingleAgentVoiceWorkflow,
    VoicePipeline,
)

from agents_config import create_agents
from audio_utils import AudioPlayer, create_audio_buffer


async def main():
    # エージェントの作成
    agent = create_agents()

    # 音声パイプラインの設定
    pipeline = VoicePipeline(workflow=SingleAgentVoiceWorkflow(agent))

    # オーディオバッファの作成
    buffer = create_audio_buffer()
    audio_input = AudioInput(buffer=buffer)

    # パイプラインの実行
    result = await pipeline.run(audio_input)

    # オーディオプレーヤーの作成
    player = AudioPlayer()

    # 音声ストリームの再生
    async for event in result.stream():
        if event.type == "voice_stream_event_audio":
            player.write(event.data)


if __name__ == "__main__":
    asyncio.run(main())
