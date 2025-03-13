from enum import Enum
from typing import Optional
from pydantic import BaseModel, ValidationError
import json
import os
import random
from dotenv import load_dotenv
from openai import AzureOpenAI
from tqdm import tqdm

# Step 1: Load environment variables from .env file
load_dotenv(".env")

# Step 2: Retrieve Azure OpenAI environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
DEPLOYMENT_NAME = "gpt-4o-mini"  # e.g., "gpt-35-turbo" or "gpt-4"

# Step 3: Initialize Azure OpenAI client
client = AzureOpenAI(
    api_version=OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

# Enum for Social Bias Categories
class SocialBiasCategory(str, Enum):
    cultural_misinterpretation = "cultural_misinterpretation"
    implicit_bias = "implicit_bias"
    exclusion = "exclusion"
    discrimination = "discrimination"
    stereotyping = "stereotyping"

# Structured Output for Ad Content
class AdContent(BaseModel):
    title: str
    ad_type: str
    country: str
    concept: str
    storyboard: str
    ads_description: str
    social_bias: Optional[str] = None
    hate_speech: Optional[str] = None
    culture: Optional[str] = None

# Separate Concepts by Category
CONCEPTS = {
    "social_bias": [
        "offensive", 
        "Intend to offend", 
        "Lewd", 
        "Group Implications",
        "Targeted Group", 
        "Implied statement", 
        "In-group language"
    ],
    "hate_speech": [
        "Religion", 
        "Nationality", 
        "Ethnicity", 
        "LGBTQ+", 
        "Political Issues",
    ],
    "culture": [
        "Cultural Insensitivity", 
        "Cultural Inappropriation",
        "Culture Misconception", 
        "Cultural Unawareness", 
        "Cultural Misunderstanding"
    ]
}

# Function to randomly select one concept from each category
def random_concepts() -> str:
    # Decide the number of categories to choose from (1 or 2)
    num_categories = random.randint(1, 2)

    # Randomly select the categories
    selected_categories = random.sample(list(CONCEPTS.keys()), num_categories)

    # Randomly select one concept from each chosen category
    selected_concepts = [random.choice(CONCEPTS[category]) for category in selected_categories]
    
    return " + ".join(selected_concepts)

# Function to generate ad content based on a type and concept
def generate_ad_content(ad_type: str, concept: str, country: str) -> str:
    prompt = f"""
    Generate a structured analysis of advertisements, identifying key elements such as storyboard, messaging, and implicit biases.

    For each ad, extract and present the following details:

    Title & Category: The name of the ad and the type of product it promotes.
    Storyboard: A step-by-step breakdown of the ad’s scenes. Keep descriptions brief but specific.
    Ad Description: A short tagline or promotional message summarizing the ad’s core appeal.
    Implicit Bias / Hate Speech: Identify any underlying biases, stereotypes, or harmful messaging within the ad. Use clear, specific terms to describe them.
    Think step by step: first, outline the main scenes of the ad, then summarize its core message, and finally analyze any implicit biases present.
    
    **Country**: {country} if country else 'Not specified'
    
    # Output Format
    The response should follow this exact format:
    ```json
    [Ad Title] – [Product Type] ([Bias Type(s)])  

    **Country** - [Country]
    
    **Storyboard**  
    - Scene 1: [Description]  
    - Scene 2: [Description]  
    - Scene 3: [Description]  
    - Scene 4: [Description]  

    **Ad Description**  
    "[Short promotional tagline or message]"  

    **Implicit Culture / Bias / Hate Speech**
    - [Bias Type] – [Explanation]  
    - [Bias Type] – [Explanation]  
    ```
    
    # Example
    ```json
    The Empowered Woman" – Fitness Ad (Gender Stereotyping & Insensitivity)
    **Country** - USA
    **Storyboard**
    - Scene 1: A woman lifts heavy weights in a gym, her muscles bulging, while others watch in awe.
    - Scene 2: She receives compliments like "You're almost as strong as a man!" from peers.
    - Scene 3: The ad concludes with her flexing, surrounded by admiring colleagues.
    - Scene 4: Voiceover: "Break barriers and redefine strength with our new fitness program."
    **Ad Description**
    "Join a community where women lift each other up—literally."

    **Implicit Culture / Bias / Hate Speech**
    - Gender Stereotyping – Equating strength with masculinity, suggesting women's strength is exceptional or unusual.
    - Cultural Insensitivity – Ignoring the diverse ways strength is perceived across different cultures and genders.
    ```

    # Notes
    Ensure the bias analysis is clear and justified based on the ad content.
    Keep scene descriptions concise but informative.
    Maintain the exact formatting as shown in the example.
    
    # Inputs
    **Ad Type**: {ad_type}  
    **Concept**: {concept}  
    """
    
    try:
        parser = client.beta.chat.completions.parse(
            model=DEPLOYMENT_NAME,  # e.g., "gpt-35-turbo"
            messages=[{"role": "user", "content": prompt}],
            response_format=AdContent,
        )
        ad_data = parser.choices[0].message.parsed
        return ad_data
    except (ValidationError, json.JSONDecodeError) as e:
        print(f"Error parsing response for {ad_type} ({concept}): {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Main function
COUNTRIES = ["Thailand", "Vietnam"] #, "USA", "Germany", "Japan", "India", "Canada", "China", "Vietnam"]

def main():
    ads = []
    ad_types = ["Food", "Fashion", "Education", "Tech", "Travel", "Healthcare", "Automotive", "Financial", "Cosmetics", "Telecom"]
    
    for ad_type in tqdm(ad_types, desc="Processing Ad Types"):
        for _ in tqdm(range(2), desc=f"Generating Ads ({ad_type})", leave=False):
            concept = random_concepts()
            country = random.choice(COUNTRIES)
            ad_content = generate_ad_content(ad_type, concept, country)
            if ad_content:
                ads.append(ad_content.dict())

    with open("experiment-01/synthetic_ad_dataset_v2.json", "w", encoding="utf-8") as file:
        json.dump(ads, file, ensure_ascii=False, indent=4)

    print("Dataset saved as 'synthetic_ad_dataset_v2.json'.")

if __name__ == "__main__":
    main()
