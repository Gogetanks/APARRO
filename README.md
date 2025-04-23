# APARRO
APARRO is Automatic Processing of Audio Recordings for Restaurant Orders, so basically an AI assistant which will take your order.

A restaurant assistant that utilizes advanced speech recognition and large
language models to process restaurant orders orally.

- A Python-based voice recorder collects audio from customers.
- OpenAI's Whisper model is used to convert speech to text.
- Mistral's LLM splits the order into menu items.
- The order is displayed back to the customer, with unavailable items clearly
mentioned

## Technologies:
- **Faster Whisper:** A faster version of the Whisper model from OpenAI used for listening to orders.
- **Mistral AI 7B:** A large language model employed for analyzing text and identifying food items.
- **thefuzz library:** Used for fuzzy matching items in orders with items in the menu.

