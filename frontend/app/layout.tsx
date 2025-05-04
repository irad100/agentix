import type { Metadata } from "next";
import {
  ClerkProvider,
  Waitlist,
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
  title: "Agentix Systems",
  description: "Agentix Systems - AI-powered solutions",
};

function AuthWrapper({ children }: { children: React.ReactNode }) {
  return (
    <>
      <SignedIn>{children}</SignedIn>
      <SignedOut>
        <div className="relative">
          {/* Greyed out UI */}
          <div className="opacity-30 pointer-events-none">{children}</div>
          <div className="absolute inset-0 flex items-center justify-center">
            <Waitlist />
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
