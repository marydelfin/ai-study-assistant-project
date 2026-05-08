print("=== AI Study Assistant ===")

while True:
    topic = input("\nEnter topic: ")

    print("\nChoose what you want:")
    print("1. Notes")
    print("2. Summary")
    print("3. Quiz")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        prompt = f"Explain {topic} in 3 short notes."
    elif choice == "2":
        prompt = f"Give a 3-line summary of {topic}."
    elif choice == "3":
        prompt = f"Give 3 quiz questions on {topic}."
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
        continue

    print("\n👉 Copy this prompt and paste in ChatGPT:\n")
    print(prompt)

    # Save to file
    with open("output.txt", "a") as file:
        file.write(f"\nTopic: {topic}\n")
        file.write(f"Choice: {choice}\n")
        file.write(prompt + "\n")
        file.write("-" * 30 + "\n")
