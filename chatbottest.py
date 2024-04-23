from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Define a function to generate response using GPT-2
def generate_response(user_input):
    # Tokenize user input
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    # Generate response
    output = model.generate(input_ids, 
                            max_length=50, 
                            num_return_sequences=1, 
                            no_repeat_ngram_size=2,
                            pad_token_id=tokenizer.eos_token_id,
                            attention_mask=torch.ones(input_ids.shape, dtype=torch.long))
    # Decode response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():
    print("Welcome to the Chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = generate_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
