import type { Metadata } from "next";
import {
  ClerkProvider,
  SignInButton,
  SignUpButton,
  SignedIn,
  SignedOut,
  UserButton,
} from "@clerk/nextjs";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Agentix Chat",
  description: "Agentix Chat - Your AI Assistant",
};

function AuthWrapper({ children }: { children: React.ReactNode }) {
  return (
    <>
      <SignedIn>{children}</SignedIn>
      <SignedOut>
        <div className="relative">
          {/* Greyed out UI */}
          <div className="opacity-30 pointer-events-none">{children}</div>

          {/* Overlay with sign in/up buttons */}
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="bg-white/90 dark:bg-slate-900/90 p-8 rounded-lg shadow-lg text-center">
              <h2 className="text-xl font-bold mb-4">
                Sign in to use the chat
              </h2>
              <p className="mb-6">
                Please sign in or create an account to start chatting with the
                assistant.
              </p>
              <div className="flex flex-col gap-3">
                <SignInButton mode="modal">
                  <button className="w-full px-4 py-2 rounded-md bg-gray-200 hover:bg-gray-300 transition-colors">
                    Sign in
                  </button>
                </SignInButton>
                <SignUpButton mode="modal">
                  <button className="w-full px-4 py-2 rounded-md bg-blue-500 text-white hover:bg-blue-600 transition-colors">
                    Sign up
                  </button>
                </SignUpButton>
              </div>
            </div>
          </div>
        </div>
      </SignedOut>
    </>
  );
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <ClerkProvider afterSignOutUrl="/">
      <html lang="en">
        <body
          className={`${geistSans.variable} ${geistMono.variable} antialiased`}
        >
          <nav className="fixed top-0 right-0 p-4 z-50">
            <SignedIn>
              <UserButton />
            </SignedIn>
          </nav>
          <AuthWrapper>{children}</AuthWrapper>
        </body>
      </html>
    </ClerkProvider>
  );
}
