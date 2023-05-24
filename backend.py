import openai


class Chatbot:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=3000,
                temperature=0.2
            ).choices[0].text
            return response
        except openai.error.RateLimitError:
            return "Error: Exceeded API rate limit. Please wait and try again later."

if __name__ == "__main__":
    api_key = "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"  # Replace with your actual OpenAI API key
    chatbot = Chatbot(api_key)
    response = chatbot.get_response("Capital of the Philippines")
    print(response)
