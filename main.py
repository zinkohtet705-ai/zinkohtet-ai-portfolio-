from assistant.core import respond

def main() -> None:
    print("Zin Ko Htet — Personal AI Assistant")
    print("Local starter only. Type 'exit' to quit.")
    while True:
        message = input("\nYou: ").strip()
        if message.lower() in {"exit", "quit"}:
            print("Assistant: Goodbye.")
            break
        if message:
            print(f"Assistant: {respond(message)}")

if __name__ == "__main__":
    main()
