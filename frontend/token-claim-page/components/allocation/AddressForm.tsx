"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"

interface AddressFormProps {
  onSubmit: (address: string) => Promise<void>
  xAccountAddress?: string
  walletAddress?: string | null
}

const AddressForm: React.FC<AddressFormProps> = ({ onSubmit, xAccountAddress, walletAddress }) => {
  const [address, setAddress] = useState("")

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log('フォーム送信:', address)
    if (validateAddress(address)) {
      onSubmit(address)
    }
  }

  const validateAddress = (address: string) => {
    const isValid = address.startsWith("0x") && address.length === 42
    console.log('アドレス検証:', address, isValid)
    return isValid
  }

  return (
    <form onSubmit={handleSubmit} className="flex gap-2">
      {xAccountAddress && (
        <div className="mb-4">
          <p className="text-sm text-gray-600">Your X account address:</p>
          <p className="font-mono">{xAccountAddress}</p>
        </div>
      )}
      <input
        type="text"
        value={address}
        onChange={(e) => setAddress(e.target.value)}
        placeholder="Enter Ethereum address"
        className="flex-1 p-2 border rounded"
      />
      <Button type="submit" disabled={!validateAddress(address)}>
        Check
      </Button>
    </form>
  )
}

export default AddressForm

