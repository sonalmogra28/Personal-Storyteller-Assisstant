import openai
# Setting my OpenAI API key here

client = openai.OpenAI(api_key="API KEY HERE")  # Replace with your actual API key
def call_model(prompt: str, max_tokens=1000, temperature=0.7) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].message.content

def generate_story(user_idea: str) -> str:
    storyteller_prompt = (
        f"You are a master children's storyteller. Write a bedtime story for kids aged 5–10 "
        f"based on this idea: '{user_idea}'. Make it imaginative, age-appropriate, and include a gentle moral."
    )
    return call_model(storyteller_prompt)

def judge_story(story: str) -> str:
    judge_prompt = (
        "You are a children's literature expert. Please evaluate the following story for:\n"
        "- Age appropriateness (5–10)\n"
        "- Engagement and creativity\n"
        "- Structure (beginning, middle, end)\n"
        "- Clarity and moral\n"
        "Suggest improvements if needed.\n\n"
        f"Story:\n{story}"
    )
    return call_model(judge_prompt, temperature=0.3)

def improve_story(story: str, feedback: str) -> str:
    improver_prompt = (
        "You are a children's story editor. Improve the following story based on the feedback provided.\n\n"
        f"Story:\n{story}\n\nFeedback:\n{feedback}"
    )
    return call_model(improver_prompt)

def main():
    user_input = input("What kind of story would you like to hear? ")
    story = generate_story(user_input)
    print("\n--- Initial Story ---\n")
    print(story)

    feedback = judge_story(story)
    print("\n--- Judge Feedback ---\n")
    print(feedback)

    if "suggest" in feedback.lower() or "improve" in feedback.lower():
        improved_story = improve_story(story, feedback)
        print("\n--- Improved Story ---\n")
        print(improved_story)
    else:
        print("\nThe story is already great! Enjoy!")

if __name__ == "__main__":
    main()