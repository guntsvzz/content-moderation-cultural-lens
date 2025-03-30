import argparse
import json
import os
from tqdm.auto import tqdm
from utils import (
    load_datasets,
)
from models import (
    get_chat_response_parser, 
    get_chat_response
)
from output_schemas import AdContent

print('Current Path :',os.getcwd())

def synthetic_advertisment(args, ds, num_samples, output_file):
    """
    Generate synthetic advertisement content based on the loaded dataset and save to a JSONL file.
    """
    # Logic to generate synthetic advertisement
    print(f"Generating {num_samples} synthetic advertisements based on the dataset: {args.dataset_name}")
    
    responses = []
    if args.dataset_name == 'candle':
        loops = ds[:args.num_sample]
    elif args.dataset_name == 'mango':
        loops = ds[:args.num_sample]
    elif args.dataset_name == 'culture-bank':
        loops = ds['tiktok'].select(range(args.num_sample))
    elif args.dataset_name == 'culture-atlas-negative':
        loops = ds[:args.num_sample]
    elif args.dataset_name == 'culture-atlas':
        loops = None
    else:
        raise ValueError(f"Unknown dataset: {args.dataset_name}")
    
    # Initialize tqdm for progress bar
    with tqdm(total=num_samples, ncols=100) as pbar:
        # For now, let's just print out the synthetic advertisements as an example
        for i, sample in enumerate(loops):
            # print(f"Advertisement {i+1}: Here's an advertisement inspired by the {args.dataset_name} dataset.")
            if args.dataset_name == 'culture-bank':
                country = sample['cultural group']
                scenario = sample['eval_scenario']
                description = sample['eval_whole_desc']
                
                PROMPT = f"""You are a creative advertising consultant. Use the following details to create a subtly biased advertisement concept:

                Scenario: {scenario}
                Country/Market: {country}
                Product/Brand Description: {description}

                Create a short advertisement based on the concept above. The ad should reflect implicit social biases or cultural insensitivity without being overt. Ensure that the message and visuals suggest or reinforce subtle bias or stereotyping.

                **Instructions:**
                1. **Storyboard** (4-step scene-by-scene breakdown, concise and clear):
                - Keep the scenes short and focused.
                - Make sure the story flows in a way that seems normal, but with subtle biases woven in.
                
                2. **Ad Description**: 
                - Craft a brief and engaging marketing message that aligns with the ad type and concept.
                - Ensure the language conveys luxury or exclusion without being too obvious.


                **Example Format:**     
                ```json  
                **Title**: [Ad Title]
                
                **Storyboard**:     
                - Scene 1: [Brief setting of characters and environment]     
                - Scene 2: [Implicit bias or cultural misunderstanding introduced subtly]     
                - Scene 3: [Brand/product shown as solution to "better" lifestyle]     
                - Scene 4: [Close with tagline that reinforces the bias without being obvious]      

                **Ad Description**:     
                "Write the ad copy in a concise, engaging tone with subtle bias."
                ```

                Ensure the ad feels normal at first glance, but upon analysis, reveals how bias is subtly embedded in it. The bias should be implicit rather than explicit, reflecting unconscious prejudices or stereotypes that might exist in the specified culture or market.
                """
                # Format the prompt with specific details
                formatted_prompt = PROMPT.format(
                    scenario=scenario, 
                    country=country, 
                    description=description)

                response = get_chat_response_parser(formatted_prompt, response_format=AdContent)
                # Convert the response to a dictionary and add the additional fields
                response_dict = response.dict()
                response_dict['country'] = country
                response_dict['scenario'] = scenario
                response_dict['description'] = description
                
            if args.dataset_name == 'culture-atlas-negative':
                country = sample['country']
                topic = sample['topic']
                subtopic = sample['subtopic']
                subsubtopic = sample['subsubtopic']
                neg = sample['neg']
                
                PROMPT = f"""You are a creative advertising consultant. Use the following details to create a subtly biased advertisement concept:

                Country/Market: {country}
                Topic: {topic}
                Subtopic: {subtopic}
                Subsubtopic: {subsubtopic}
                Negative Data Sample: {neg}
                (Note: The content should follow these negative but implicit cues.)

                Create a short advertisement based on the concept above. The ad should reflect implicit social biases or cultural insensitivity without being overt. Ensure that the message and visuals suggest or reinforce subtle bias or stereotyping.

                **Instructions:**
                1. **Storyboard** (4-step scene-by-scene breakdown, concise and clear):
                - Keep the scenes short and focused.
                - Make sure the story flows in a way that seems normal, but with subtle biases woven in.
                            
                2. **Ad Description**: 
                - Craft a brief and engaging marketing message that aligns with the ad type and concept.
                - Ensure the language conveys luxury or exclusion without being too obvious.

                **Example Format:**     
                ```json  
                **Title**: [Ad Title]
                            
                **Storyboard**:     
                - Scene 1: [Brief setting of characters and environment]     
                - Scene 2: [Implicit bias or cultural misunderstanding introduced subtly]     
                - Scene 3: [Brand/product shown as solution to "better" lifestyle]     
                - Scene 4: [Close with tagline that reinforces the bias without being obvious]      

                **Ad Description**:     
                "Write the ad copy in a concise, engaging tone with subtle bias.
                ```
                
                Ensure the ad feels normal at first glance, but upon analysis, reveals how bias is subtly embedded in it. The bias should be implicit rather than explicit, reflecting unconscious prejudices or stereotypes that might exist in the specified culture or market.
                """

                # Format the prompt with specific details
                formatted_prompt = PROMPT.format(
                    topic=topic, 
                    country=country, 
                    subtopic=subtopic,
                    subsubtopic=subsubtopic,
                    neg=neg
                )

                response = get_chat_response_parser(formatted_prompt, response_format=AdContent)
                # Convert the response to a dictionary and add the additional fields
                response_dict = response.dict()
                response_dict['country'] = country
                response_dict['topic'] = topic
                response_dict['subtopic'] = subtopic
                response_dict['subsubtopic'] = subsubtopic
                response_dict['neg'] = neg
                
            # Append the modified dictionary to the responses list
            responses.append(response_dict)
            
            pbar.update(1)  # Update the progress bar

    # Saving each response to the JSONL file
    with open(f"experiment-02/{output_file}", 'w', encoding="utf-8") as file:
        json.dump(responses, file, ensure_ascii=False, indent=4)

def main(args):
    # Load the selected dataset
    ds = load_datasets(args.dataset_name)
    prompt = "Create an advertisement based on the dataset provided."  # Placeholder prompt
    # Dynamically create the output file name based on the dataset
    output_file = f"synthetic_advertisements_{args.dataset_name}.jsonl"
    # Generate synthetic advertisement content and save to file
    synthetic_advertisment(args, ds, args.num_sample, output_file)
    print(f"Generated {args.num_sample} synthetic advertisements. Saved to {output_file}.")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate advertisement content which references culture with an existing dataset"
    )
    parser.add_argument(
        '--dataset_name', 
        type=str, 
        required=True, 
        choices=['candle', 'mango', 'culture-bank', 'culture-atlas','culture-atlas-negative'],  # Restrict choices to these four
        default='culture-bank',  # Set default to 'culture-bank'
        help="Dataset to be used for the conversation"
    )
    parser.add_argument(
        '--num_sample', 
        type=int, 
        required=True, 
        default=5,  # Set default to 5
        help="Number of samples for dialogue generation"
    )
    args = parser.parse_args()
    main(args)
