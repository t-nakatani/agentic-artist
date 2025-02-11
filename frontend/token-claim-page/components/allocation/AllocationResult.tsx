"use client"

interface AllocationResultProps {
  allocation: string | null
}

export default function AllocationResult({ allocation }: AllocationResultProps) {
  return (
    <div className="mt-4 p-4 border rounded-lg bg-gray-50 flex flex-col items-center">
      <h2 className="text-lg font-semibold mb-2">Your Current Allocation</h2>
      {allocation ? (
        <div className="flex flex-col items-center">
          <p className="text-3xl font-mono font-bold text-blue-600">{allocation}</p>
        </div>
      ) : (
        <p className="text-gray-500">...loading...</p>
      )}
    </div>
  )
}

