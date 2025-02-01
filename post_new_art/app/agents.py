from pydantic_ai.agent import Agent

from app.agents.prompt_organizer import prompt_organizer_agent

# tools: post_art_to_x, publish_nft, allocate_token
orchestration_agent = Agent(
    model="openai:gpt-4o-mini",
    system_prompt="",
)

# tools: get_advices, fine_tune_prompt
# return: content: XPostContent
x_posting_agent = Agent(
    model="openai:gpt-4o-mini",
    system_prompt="",
)
