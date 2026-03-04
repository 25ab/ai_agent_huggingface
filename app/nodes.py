def planner_node(state, llm):
    query = state["query"]

    prompt = f"""
    You are research planner.

    Query:
    {query}

    Generate research plan.
    """

    state["plan"] = llm.invoke(prompt)

    return state


def research_node(state, agent):
    query = state["query"]

    state["research"] = agent.run(query)

    return state


def reflection_node(state, llm):
    question = state["query"]
    answer = state["research"]

    prompt = f"""
    Critic agent.

    Question:
    {question}

    Answer:
    {answer}

    Return JSON:
    score and suggestion
    """

    state["reflection"] = llm.invoke(prompt)

    return state