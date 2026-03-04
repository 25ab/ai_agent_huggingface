from agents.main_agents import agent

def main():
    query = "Explain deep learning in medicine"

    result = agent.run(query)

    print(result)

if __name__ == "__main__":
    main()