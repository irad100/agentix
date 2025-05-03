import { clerkMiddleware, createRouteMatcher } from "@clerk/nextjs/server";

// Match only the API route(s)
const isApiRoute = createRouteMatcher(["/api(.*)"]);

export default clerkMiddleware(async (auth, req) => {
  const authObject = await auth();
  // Protect the API route
  if (isApiRoute(req)) {
    // Require specific permission to access chat API
    await auth.protect(() => {
      return authObject.orgSlug === "irad";
    });
  }
});

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    "/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)",
    // Always run for API routes
    "/(api|trpc)(.*)",
  ],
};
