from app.agents.agent_persona import AgentPersona
from app.image_generation_prompt import ImageGenerationPrompt


class PromptOrganizer(AgentPersona):
    """
    PromptOrganizer agent
    """

    role = """
    You are a prompt organizer agent. You are given a prompt and you need to create structured image-generation prompt.
    """

    result_type = ImageGenerationPrompt
