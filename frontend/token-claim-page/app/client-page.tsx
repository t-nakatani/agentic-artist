"use client"

import { useState, useCallback, useEffect } from "react"
import { useSession } from "next-auth/react"
import AddressForm from "@/components/allocation/AddressForm"
import AllocationResult from "@/components/allocation/AllocationResult"
import { Button } from "@/components/ui/button"
import { checkAllocationForAddress } from "@/lib/allocation"
import { AuthSection } from "@/components/AuthSection"
import { ANIMATION_STYLES } from "@/lib/constants"
import { AnimatedBackground } from "@/components/background"
import { useWallet } from '../hooks/useWallet'
import { mintToken } from "@/lib/mint"

const EXAMPLE_LINK = 'https://testnets.opensea.io/collection/oniichan-5'
const BANNER_IMAGES = [
  { src: '/images/example_1.png', href: EXAMPLE_LINK },
  { src: '/images/example_2.png', href: EXAMPLE_LINK },
  { src: '/images/example_3.png', href: EXAMPLE_LINK },
  { src: '/images/example_4.png', href: EXAMPLE_LINK },
  { src: '/images/example_5.png', href: EXAMPLE_LINK },
  { src: '/images/example_1.png', href: EXAMPLE_LINK },
  { src: '/images/example_2.png', href: EXAMPLE_LINK },
  { src: '/images/example_3.png', href: EXAMPLE_LINK },
  { src: '/images/example_4.png', href: EXAMPLE_LINK },
  { src: '/images/example_5.png', href: EXAMPLE_LINK },
]

export default function ClientPage() {
  const { data: session } = useSession()
  const [allocation, setAllocation] = useState<string | null>(null)
  const [xAccountAddress, setXAccountAddress] = useState<string | undefined>(undefined)
  const { account, connectWallet, disconnectWallet, isConnected } = useWallet()
  const [address, setAddress] = useState('')

  const checkAllocation = useCallback(async (address: string) => {
    try {
      const result = await checkAllocationForAddress(address)
      setAllocation(result)
    } catch (error) {
      console.error('アロケーションチェックエラー:', error)
      setAllocation(null)
    }
  }, [])

  const checkXAccountAllocation = useCallback(async () => {
    if (xAccountAddress) {
      await checkAllocation(xAccountAddress)
    }
  }, [xAccountAddress, checkAllocation])

  // Xアカウントのアドレスを取得するダミー関数
  const fetchXAccountAddress = useCallback(async () => {
    const dummyAddress = `0x${Array(40)
      .fill(0)
      .map(() => Math.floor(Math.random() * 16).toString(16))
      .join("")}`
    setXAccountAddress(dummyAddress)
  }, [])

  useEffect(() => {
    if (session) {
      fetchXAccountAddress()
    } else {
      setXAccountAddress(undefined)
    }
  }, [session, fetchXAccountAddress])

  // ウォレット接続時に自動的にアロケーションをチェック
  useEffect(() => {
    if (account) {
      checkAllocation(account)
    }
  }, [account, checkAllocation])

  const handleMint = useCallback(async () => {
    try {
      if (!account) {
        console.error('ウォレットが接続されていません')
        return
      }
      await mintToken()
      console.log('Mint successful')
    } catch (error) {
      console.error('Mintエラー:', error)
    }
  }, [account])

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4 relative bg-black/95">
      <style>{ANIMATION_STYLES}</style>
      
      <AnimatedBackground images={BANNER_IMAGES} />
      
      <div className="relative z-10 flex flex-col items-center justify-center w-full max-w-3xl px-4">
        <div className="w-full bg-background/95 backdrop-blur-md rounded-xl p-8 md:p-10 shadow-2xl border border-border">
          <div className="flex flex-col items-center justify-center space-y-6">
            <h1 className="text-3xl md:text-4xl font-bold text-foreground">Token Allocation Checker</h1>
            
            <div className="w-full max-w-2xl">
              <AllocationResult allocation={allocation} />
            </div>
            
            <div className="w-full max-w-2xl">
              {!isConnected ? (
                <AddressForm 
                  onSubmit={checkAllocation} 
                  xAccountAddress={xAccountAddress}
                  walletAddress={account}
                />
              ) : (
                <div className="w-full">
                  <button
                    onClick={handleMint}
                    className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                  >
                    Mint
                  </button>
                </div>
              )}
            </div>
            
            {xAccountAddress && (
              <div className="w-full max-w-2xl">
                <Button onClick={checkXAccountAllocation} className="w-full">
                  Check X Account Allocation
                </Button>
              </div>
            )}
            
            <div className="w-full max-w-2xl mt-6">
              <AuthSection />
            </div>
          </div>
        </div>
      </div>
      
      <div className="fixed top-4 right-4">
        {account ? (
          <button
            onClick={disconnectWallet}
            className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg shadow-lg transition-colors flex items-center space-x-2"
          >
            <span>disconnect</span>
            <span>{`${account.slice(0, 6)}...${account.slice(-4)}`}</span>
          </button>
        ) : (
          <button
            onClick={connectWallet}
            className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg shadow-lg transition-colors"
          >
            connect wallet
          </button>
        )}
      </div>
    </div>
  )
} 