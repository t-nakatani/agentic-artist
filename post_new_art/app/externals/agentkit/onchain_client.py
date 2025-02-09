from cdp_langchain.agent_toolkits import CdpToolkit, Wallet
from cdp_langchain.tools import CdpTool
from cdp_langchain.utils import CdpAgentkitWrapper
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

llm = ChatOpenAI(model="gpt-4o-mini")
agentkit = CdpAgentkitWrapper()
cdp_toolkit = CdpToolkit.from_cdp_agentkit_wrapper(agentkit)
tools = cdp_toolkit.get_tools()
from langgraph.prebuilt import create_react_agent

MIT_PROMPT = """

"""


class MintNFTInput(BaseModel):
    """
    Input argument schema for mintNFT action."
    """

    nft_contract_address: str = Field(..., description="NFT contract address e.g. `0x1234`")
    recipient_address: str = Field(..., description="Recipient address e.g. `0x1234`")
    token_uri: str = Field(..., description="Token URI e.g. `https://ipfs.io/1234`")


def mintNFT(wallet: Wallet, nft_contract_address: str, recipient_address: str, token_uri: str):
    """send a transaction to mint an NFT
    args:
        wallet: Wallet: Wallet object
        nft_contract_address: str: NFT contract address e.g. `0x1234`
        recipient_address: str: Recipient address e.g. `0x1234`
        token_uri: str: Token URI e.g. `https://ipfs.io/1234`
    """
    ## cdpのwalletを使う必要は特にない。


minNFTTool = CdpTool(
    name="mintNFT",
    description=MIT_PROMPT,
    cdp_agentkit_wrapper=agentkit,
    args_schema=MintNFTInput,
    func=mintNFT,
)
