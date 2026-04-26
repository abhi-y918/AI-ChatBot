try:
    from ddgs import DDGS
    print("Successfully imported DDGS from ddgs")
    with DDGS() as ddgs:
        for r in ddgs.text("test", max_results=1):
            print(f"Test search result: {r}")
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
