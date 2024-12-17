import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class MistralInteractive:
    def __init__(self, model_name: str = "mistralai/Mistral-7B-Instruct-v0.3"):
        """
        Initialize the model and tokenizer.
        """
        print("\nInitializing Mistral model... Please wait.")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, 
            torch_dtype=torch.float16, 
            device_map="auto"
        )
        print("Model loaded successfully!\n")

    def generate_response(self, prompt: str, max_length: int = 200, temperature: float = 0.7) -> str:
        """
        Generate a response for a given prompt.
        Args:
            prompt (str): The input prompt for the model.
            max_length (int): Maximum length of the generated output.
            temperature (float): Sampling temperature for generation.
        Returns:
            str: The generated response.
        """
        try:
            # Encode the prompt and move tensors to GPU
            inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
            
            # Generate output with adjustable max_length and temperature
            output = self.model.generate(
                **inputs, 
                max_length=max_length, 
                temperature=temperature,
                pad_token_id=self.tokenizer.eos_token_id
            )
            
            # Decode and return the result
            return self.tokenizer.decode(output[0], skip_special_tokens=True)

        except Exception as e:
            return f"Error during generation: {str(e)}"

def main():
    """
    Main interactive function to input prompts and generate model responses.
    """
    mistral = MistralInteractive()
    
    print("Welcome to the Mistral-7B Interactive Text Generator!")
    print("Type 'exit' to quit the program.\n")
    
    while True:
        # Input prompt from the user
        prompt = input("Enter your prompt: ").strip()
        
        if prompt.lower() in ["exit", "quit"]:
            print("Exiting the program. Goodbye!")
            break
        
        # Allow the user to adjust parameters
        try:
            max_length = int(input("Max length of response (default: 200): ") or 200)
            temperature = float(input("Temperature (default: 0.7): ") or 0.7)
        except ValueError:
            print("Invalid input. Using default parameters.")
            max_length = 200
            temperature = 0.7
        
        # Generate the response
        print("\nGenerating response...\n")
        response = mistral.generate_response(prompt, max_length=max_length, temperature=temperature)
        print(f"Response:\n{response}\n{'-'*60}")

if __name__ == "__main__":
    main()
