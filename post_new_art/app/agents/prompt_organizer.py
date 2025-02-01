from app.agents.agent_factory import AgentFactory
from app.image_generation_prompt import ImageGenerationPrompt

# ------------------------------ agent definition ------------------------------

prompt_organizer_system_prompt = """
    You are a prompt organizer agent. You are given a prompt and you need to create structured image-generation prompt.
"""

prompt_organizer_agent = AgentFactory.create_agent(
    name="prompt_organizer", system_prompt=prompt_organizer_system_prompt, result_type=ImageGenerationPrompt
)

# ------------------------------ export ------------------------------


async def run_prompt_organizer(prompt: str) -> ImageGenerationPrompt:
    return await prompt_organizer_agent.run(prompt)
