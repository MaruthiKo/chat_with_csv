import pandas as pd
import dotenv
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

def main(query, df):
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        max_iterations=5,
    )
    response = agent.invoke(query)
    return response["output"]



if __name__ == "__main__":
    query = input("Enter your query: ")
    df = pd.read_csv("customer_survey.csv")
    print(main(query, df))
