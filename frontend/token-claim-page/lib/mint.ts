import { ethers } from "ethers"
import { TokenMintHandler } from "./contract-handlers/tokenMintHandler"

export async function mintToken(): Promise<void> {
  const provider = new ethers.BrowserProvider(window.ethereum as any)
  const signer = await provider.getSigner()
  
  const tokenMint = new TokenMintHandler(signer)
  await tokenMint.mint()
  
  // 処理時間をシミュレート
  await new Promise(resolve => setTimeout(resolve, 1000))
}
