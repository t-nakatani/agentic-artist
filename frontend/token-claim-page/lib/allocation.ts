import { ethers } from "ethers"
import { AllocationStorageHandler } from "./contract-handlers/allocationStorageHandler"

export const checkAllocationForAddress = async (address: string): Promise<string> => {
  console.log('アロケーション確認中:', address)
  
  // TODO: 本番環境ではprocess.env.NEXT_PUBLIC_RPC_URLを使用
  const provider = new ethers.JsonRpcProvider("https://base-sepolia.gateway.tenderly.co")
  
  const allocationStorage = new AllocationStorageHandler(provider)
  
  try {
    const allocation = await allocationStorage.getAllocation(address)
    const result = Number(allocation).toFixed(1) + ' AGNT'
    console.log('アロケーション結果:', result)
    return result
  } catch (error) {
    console.error('アロケーション確認エラー:', error)
    throw error
  }
}
