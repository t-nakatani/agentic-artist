import { useSession, signIn, signOut } from "next-auth/react"
import { Button } from "@/components/ui/button"

export function AuthSection() {
  const { data: session } = useSession()

  if (session) {
    return (
      <div className="w-full">
        <div className="mb-4">
          Signed in as {session.user?.name} ({session.user?.email})
        </div>
        <Button onClick={() => signOut()} className="w-full">
          Sign out
        </Button>
      </div>
    )
  }

  return (
    <div className="w-full">
      <p className="text-sm text-gray-600 mb-2">Connect your X account to see your allocation:</p>
      <Button onClick={() => signIn("twitter")} className="w-full">
        Sign in with X
      </Button>
    </div>
  )
} 