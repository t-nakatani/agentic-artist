"use client"

import { Inter } from "next/font/google"
import "./globals.css"
import { SessionProvider } from "next-auth/react"
import type { ReactNode } from "react"
import AuthProvider from "./providers/AuthProvider"

const inter = Inter({ subsets: ["latin"] })

export default function RootLayout({
  children,
}: {
  children: ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <AuthProvider>{children}</AuthProvider>
      </body>
    </html>
  )
}



import './globals.css'