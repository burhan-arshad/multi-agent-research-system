from agents import build_news_agent, build_scraper_agent, writer_chain, critic_chain
import re


def extract_urls(text: str) -> list[str]:
    return re.findall(r'https?://[^\s]+', text)


def run_search_pipeline(topic:str)->dict:
    state={}

    # Step 1: Fetch news
    print("\n"+ "-"*20 + " Fetching News " + "-"*20)
    news_agent=build_news_agent()
    news_result=news_agent.invoke({
        "messages" :[("user", f"Fetch recent news about {topic}")]
    })

    state['news_result']=news_result['messages'][-1].content
    print(f"\n\n\nNews result: {state['news_result']}")

    # Step 2: Scrape URLs from news result
    print("\n"+ "-"*20 + " Scraping URLs " + "-"*20)
    urls = extract_urls(state["news_result"])
    reader_agent=build_scraper_agent()
    reader_result=reader_agent.invoke({
        "messages" :[(
            "user",
            f"Scrape these news URLs and return the important article content:\n"
            + "\n".join(urls)
        )]
    })
    state['scraped_content']=reader_result['messages'][-1].content
    print(f"\n\n\nScraped content: {state['scraped_content']}")

    # Step 3: Writer chain
    print("\n"+ "-"*20 + " Drafting Report " + "-"*20)
    combined_research=(f"{state['news_result']}\n\n{state['scraped_content']}")
    state['written_report']=writer_chain.invoke({
        "topic":topic,
        "research":combined_research
    })

    print(f"\n\n\nWritten report: {state['written_report']}")

    # Step 4: Critic chain
    print("\n"+ "-"*20 + " Critiquing Report " + "-"*20)
    state['critique']=critic_chain.invoke({
        "report":state['written_report']
    })
    print(f"\n\n\nCritique: {state['critique']}")

    return state

if __name__=="__main__":
    topic=input("Enter a topic to research: ")
    result=run_search_pipeline(topic)