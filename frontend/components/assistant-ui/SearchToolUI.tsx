"use client";
import { makeAssistantToolUI } from "@assistant-ui/react";
import { GlobeIcon } from "@radix-ui/react-icons"; // Assuming you have radix-ui installed

// Define the expected arguments for the search tool
type SearchArgs = {
    query: string;
};

// Define the expected structure of the search results from Tavily
// Adjust this based on the actual structure returned by your backend search function
type SearchResultItem = {
    title: string;
    content: string; // Tavily often uses 'content' for description
    url: string;
};

type SearchResult = {
    // Assuming the backend returns the results directly as an array
    // or wraps them in a key like 'results'. Adjust if necessary.
    // For now, let's assume it's directly an array based on the python Optional[dict[str, Any]] which langchain_tavily.TavilySearch likely returns as list of dicts
    results: SearchResultItem[];
};


export const SearchToolUI = makeAssistantToolUI<SearchArgs, SearchResult>({
    toolName: "search", // Matches the python function name
    render: ({ args, status, result }) => {
        const isLoading = status.type === "running";

        // Attempt to parse the result if it's a string and status is complete
        let parsedResult: SearchResult | undefined = undefined;
        if (status.type === 'complete' && typeof result === 'string') {
            try {
                // Assuming the string contains the full object including the 'results' key
                const rawParsed = JSON.parse(result);
                // Validate if the parsed object has the expected 'results' array
                if (rawParsed && Array.isArray(rawParsed.results)) {
                    parsedResult = rawParsed as SearchResult;
                }
            } catch (error) {
                console.error("[SearchToolUI] Failed to parse result string:", error);
                // Handle error, maybe display an error message in the UI
            }
        } else if (status.type === 'complete' && typeof result === 'object' && result !== null) {
            // If it's already an object (ideal case), use it directly
            // Type guard to check for the expected structure
            if ('results' in result && Array.isArray(result.results)) {
                parsedResult = result as SearchResult;
            }
        }

        // Use parsedResult for rendering
        const displayResults = !isLoading ? parsedResult?.results : undefined;

        return (
            <div className="rounded-md border bg-muted p-4 space-y-3 my-2">
                <div className="flex items-center gap-2 text-sm font-medium">
                    <GlobeIcon className="h-4 w-4 animate-spin" /> {/* Add spin animation while loading */}
                    <span>
                        Searching the web for:{" "}
                        <span className="font-semibold text-blue-600">{args.query}</span>
                        {isLoading && "..."}
                    </span>
                </div>
                {!isLoading && parsedResult && (
                    <div className="space-y-2 pl-6">
                        {displayResults?.map((item, index) => (
                            <div key={index} className="text-sm">
                                <a
                                    href={item.url}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="text-blue-700 hover:underline font-medium"
                                >
                                    {item.title}
                                </a>
                                <p className="text-muted-foreground text-xs mt-0.5">
                                    {item.content}
                                </p>
                            </div>
                        ))}
                        {(!displayResults || displayResults.length === 0) && (
                            <p className="text-muted-foreground text-xs mt-0.5">No results found.</p>
                        )}
                    </div>
                )}
                {!isLoading && !parsedResult && status.type === 'complete' && (
                    // Show an error if parsing failed or the structure was wrong
                    <div className="pl-6 text-sm text-red-600">
                        Failed to display search results.
                    </div>
                )}
            </div>
        );
    },
});

// Default export for easier dynamic import if needed, or named export works too
export default SearchToolUI; 