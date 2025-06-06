import pytest
from langchain_core.runnables import RunnableConfig
from langsmith import unit

from agentix import graph


@pytest.mark.asyncio
@unit
async def test_agentix_simple_passthrough() -> None:
    res = await graph.ainvoke(
        {"messages": [("user", "Who is the founder of LangChain?")]},
        RunnableConfig(configurable={"system_prompt": "You are a helpful AI assistant."}),
    )

    assert "harrison" in str(res["messages"][-1].content).lower()
