from app.agents.agent_factory import AgentFactory
from app.agents.persona.prompt_organizer import PromptOrganizer


def test_prompt_organizer_agent():
    prompt_organizer = PromptOrganizer()
    prompt_organizer_agent = AgentFactory.create_agent(prompt_organizer)
    sentense = [
        "Visualize a surreal blue canvas adorned with translucent clouds.",
        "The varying shades of blue merge into a rhythmic, enchanting display, evoking a sense of mystery and wonder.",
    ]

    result = prompt_organizer_agent.run_sync(" ".join(sentense))

    assert isinstance(result.data, prompt_organizer.result_type)
