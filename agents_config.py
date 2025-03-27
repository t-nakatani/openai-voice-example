from agents import Agent
from agents.extensions.handoff_prompt import prompt_with_handoff_instructions
from tools import get_weather


def create_agents():
    japanese_agent = Agent(
        name="Japanese",
        handoff_description="A Japanese speaking agent.",
        instructions=prompt_with_handoff_instructions(
            "You're speaking to a human, so be polite and concise. Speak in Japanese.",
        ),
        model="gpt-4o-mini",
    )

    main_agent = Agent(
        name="Assistant",
        instructions=prompt_with_handoff_instructions(
            "You're speaking to a human, so be polite and concise. If the user speaks in Japanese, handoff to the japanese agent.",
        ),
        model="gpt-4o-mini",
        handoffs=[japanese_agent],
        tools=[get_weather],
    )

    return main_agent
