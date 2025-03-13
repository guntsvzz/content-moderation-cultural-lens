from enum import Enum
from typing import Optional
from pydantic import BaseModel
import json
import os
import random
from dotenv import load_dotenv
from openai import AzureOpenAI

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
    ad_type: str
    concept: str
    storyboard: str
    ads_description: str
    social_bias: Optional[str] = None
    hate_speech: Optional[str] = None
    culture: Optional[str] = None

# List of possible concepts
CONCEPTS = [
    "Social Bias",
    "Cultural Misinterpretation",
    "Implicit Hate Speech",
    "Gender Stereotyping",
    "Classism",
    "Racial Stereotyping",
    "Ageism",
    "Ableism",
    "Cultural Appropriation",
    "Body Image Issues",
    "Beauty Standards",
    "Consumerism",
    "Elitism",
    "Environmental Injustice",
    "Marginalization",
    "Sexual Stereotyping",
    "Economic Disparities",
    "Religious Bias",
    "Political Bias",
    "Cultural Homogenization",
    "Ethnocentrism",
    "Misrepresentation of Minorities",
    "Privilege",
    "Exclusion of Disabled People",
    "Tokenism",
    "Heteronormativity",
    "Exoticization of Cultures",
    "Gender Non-Conformity Stigmatization",
    "Mental Health Stigma",
    "Discrimination in the Workplace",
    "Unconscious Bias",
    "Privilege Reinforcement",
    "Stereotypes in Media",
    "Nationalism",
    "Globalization and Its Impacts",
    "Consumerism and Environmental Damage",
    "Fetishization of Cultures",
    "Historical Inaccuracies",
    "Cultural Stereotyping in Advertising",
    "Misrepresentation of LGBTQ+ Individuals",
    "Economic Exploitation",
    "Overgeneralization of Cultures",
    "Normative Gender Roles",
    "Discriminatory Consumer Targeting",
    "Marketing Manipulation",
    "Racialized Marketing Strategies",
    "Cultural Erasure",
    "Reinforcement of Patriarchy",
    "Historical Revisionism",
    "Gendered Marketing",
    "Racial Profiling in Advertising",
    "Class Divide in Marketing",
    "Cultural Sensitivity in Advertising",
    "Cultural Colorism",
    "Privileged Language in Advertising",
    "Cultural Neglect",
    "Linguistic Bias",
    "Exclusionary Practices in Advertising",
    "Homogenization of Cultural Narratives"
]

CONCEPTS = [
    "Social Bias",
    "Cultural Misinterpretation",
    "Implicit Hate Speech",
    "Gender Stereotyping",
    "Classism",
    "Racial Stereotyping",
    "Ageism",
    "Ableism",
    "Cultural Appropriation",
    "Body Image Issues",
    "Beauty Standards",
    "Consumerism",
    "Elitism",
    "Environmental Injustice",
    "Marginalization",
    "Sexual Stereotyping",
    "Economic Disparities",
    "Religious Bias",
    "Political Bias",
    "Cultural Homogenization",
    "Ethnocentrism",
    "Misrepresentation of Minorities",
    "Privilege",
    "Exclusion of Disabled People",
    "Tokenism",
    "Heteronormativity",
    "Exoticization of Cultures",
    "Gender Non-Conformity Stigmatization",
    "Mental Health Stigma",
    "Discrimination in the Workplace",
    "Unconscious Bias",
    "Privilege Reinforcement",
    "Stereotypes in Media",
    "Nationalism",
    "Globalization and Its Impacts",
    "Consumerism and Environmental Damage",
    "Fetishization of Cultures",
    "Historical Inaccuracies",
    "Cultural Stereotyping in Advertising",
    "Misrepresentation of LGBTQ+ Individuals",
    "Economic Exploitation",
    "Overgeneralization of Cultures",
    "Normative Gender Roles",
    "Discriminatory Consumer Targeting",
    "Marketing Manipulation",
    "Racialized Marketing Strategies",
    "Cultural Erasure",
    "Reinforcement of Patriarchy",
    "Historical Revisionism",
    "Gendered Marketing",
    "Racial Profiling in Advertising",
    "Class Divide in Marketing",
    "Cultural Sensitivity in Advertising",
    "Cultural Colorism",
    "Privileged Language in Advertising",
    "Cultural Neglect",
    "Linguistic Bias",
    "Exclusionary Practices in Advertising",
    "Homogenization of Cultural Narratives"
]


# Function to randomly select one or two concepts
def random_concepts() -> str:
    selected_concepts = random.sample(CONCEPTS, k=random.randint(1, 2))
    return " + ".join(selected_concepts)

# Function to generate ad content based on a type and concept
def generate_ad_content(ad_type: str, concept: str) -> str:
    prompt = f"""
    Create a short advertisement based on the concept of {concept}. The ad should reflect implicit social biases or cultural insensitivity without being overt. Ensure that the message and visuals suggest or reinforce subtle bias or stereotyping.

    **Instructions:**
    1. **Storyboard** (4-step scene-by-scene breakdown, concise and clear):
       - Keep the scenes short and focused.
       - Make sure the story flows in a way that seems normal, but with subtle biases woven in.
    
    2. **Ad Description**: 
       - Craft a brief and engaging marketing message that aligns with the ad type and concept.
       - Ensure the language conveys luxury or exclusion without being too obvious.

    3. **Implicit Bias / Cultural / Hate Speech Analysis**: 
       - Analyze the subtle implicit bias, cultural misunderstanding, or hate speech in the ad.
       - Provide a short, clear explanation of how the ad communicates bias or hate speech without explicitly mentioning it.

    **Example Format:**
    ---
    **Ad Type**: {ad_type}  
    **Concept**: {concept}  

    **Storyboard**:
    - Scene 1: [Brief setting of characters and environment]
    - Scene 2: [Implicit bias or cultural misunderstanding introduced subtly]
    - Scene 3: [Brand/product shown as solution to "better" lifestyle]
    - Scene 4: [Close with tagline that reinforces the bias without being obvious]

    **Ad Description**:
    "Write the ad copy in a concise, engaging tone with subtle bias."

    **Implicit Bias / Cultural / Hate Speech Analysis**:
    - Subtle social bias or stereotyping.
    - Hidden cultural misunderstanding or exclusion.
    - Any elements of implicit hate speech or discrimination.

    ---
    Ensure the ad feels normal, but upon analysis, you can see how bias is subtly embedded in it.
    """

    completion = client.chat.completions.create(
        model=DEPLOYMENT_NAME,  # e.g., "gpt-35-turbo"
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content

# Function to extract the different sections from the generated ad content
def extract_sections(ad_content: str, concept: str) -> AdContent:
    try:
        storyboard = ad_content.split("**Storyboard**:")[1].split("**Ad Description**:")[0].strip()
    except IndexError:
        storyboard = "Not Available"

    try:
        ads_description = ad_content.split("**Ad Description**:")[1].split("**Implicit Bias / Cultural / Hate Speech Analysis**:")[0].strip()
    except IndexError:
        ads_description = "Not Available"

    try:
        analysis_part = ad_content.split("**Implicit Bias / Cultural / Hate Speech Analysis**:")[1]
        social_bias = analysis_part.split("Hate Speech")[0].strip()
        hate_speech = analysis_part.split("culture")[0].strip() if "culture" in analysis_part else "Not Available"
        culture = analysis_part.split("culture")[1].strip() if "culture" in analysis_part else "Not Available"
    except IndexError:
        social_bias = hate_speech = culture = "Not Available"

    return AdContent(
        ad_type="Food",  # Example for Food, you can adapt for other types
        concept=concept,
        storyboard=storyboard,
        ads_description=ads_description,
        social_bias=social_bias,
        hate_speech=hate_speech,
        culture=culture
    )

def main():
    # Generate multiple ad variations
    ads = []
    ad_types = ["Food"] #, "Fashion", "Education", "Tech", "Travel"]
    
    # Generate random concepts
    for ad_type in ad_types:
        for _ in range(3):  # Generate 3 different ads for each ad type
            concept = random_concepts()  # Randomly pick 1 or 2 concepts
            ad_content = generate_ad_content(ad_type, concept)
            ad = extract_sections(ad_content, concept)
            ads.append(ad.dict())  # Convert Pydantic model to dict for JSON output

    # Save the synthetic dataset as a JSON file
    with open("synthetic_ad_dataset.json", "w", encoding="utf-8") as file:
        json.dump(ads, file, ensure_ascii=False, indent=4)

    print("Synthetic dataset generated and saved as 'synthetic_ad_dataset.json'.")

if __name__ == "__main__":
    main()
