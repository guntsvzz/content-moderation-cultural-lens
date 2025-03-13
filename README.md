# Content Moderations in Advertisements through Cultural Lens

## Table of Contents
- [Content Moderations in Advertisements through Cultural Lens](#content-moderations-in-advertisements-through-cultural-lens)
  - [Table of Contents](#table-of-contents)
  - [News](#news)
  - [Introduction](#introduction)
    - [Research Questions (Tentative)](#research-questions-tentative)
    - [Hypotheses (Tentative)](#hypotheses-tentative)
  - [Cultural Terminology](#cultural-terminology)
    - [Cultural Awareness](#cultural-awareness)
    - [Cultural Knowledge](#cultural-knowledge)
    - [Cultural Sensitivity](#cultural-sensitivity)
    - [Cultural Misunderstanding](#cultural-misunderstanding)
    - [Cultural Misconception](#cultural-misconception)
  - [What is the Culture Iceberg Theory?](#what-is-the-culture-iceberg-theory)
    - [Aspect Comparison: Surface Level vs. Deep-Level](#aspect-comparison-surface-level-vs-deep-level)
  - [Methodology](#methodology)
  - [Papers](#papers)
    - [Literature Review](#literature-review)
  - [Citation](#citation)

## News
- [2025/02/05] Synthetic dataset 

## Introduction
Social media platforms are widely popular and frequently serve as channels for advertisements. Increasingly, these advertisements rely on AI-driven content moderation to detect and filter harmful content such as hate speech, misinformation, and explicit material. While such advancements have improved online safety, current moderation systems often lack a cultural sensitivity lens—critical for understanding how diverse audiences interpret information.

To address this gap, we propose a **Cultural (Sensitivity) Content Moderation Framework** based on the Cultural Iceberg Theory. This framework moves beyond traditional harmful content detection by analyzing both:
- **Surface-Level Cultural Elements (Explicit Knowledge):** Observable traits like language, symbols, and clothing.
- **Deep-Level Cultural Implications (Implicit Meanings):** Subtle aspects like power dynamics, historical sensitivities, and emotional norms.

By integrating commonsense cultural knowledge with bias detection, our approach aims to ensure that AI moderation not only identifies overt harmful content but also flags culturally insensitive representations that might reinforce stereotypes, misunderstandings, or unintentional offenses.

### Research Questions (Tentative)
- **R1:** To what extent do existing AI moderation models fail to recognize implicit cultural biases, and what are the key factors contributing to these failures?
- **R2:** How can AI-driven content moderation systems be enhanced to detect and address cultural insensitivity, rather than just harmful content?
- **R3:** What role does the Cultural Iceberg Theory play in distinguishing surface-level explicit cultural elements from deep-level implicit cultural meanings in advertisements?

### Hypotheses (Tentative)
- **H1:** LLM-based context-aware reasoning will improve AI moderation’s ability to detect historically and socially sensitive themes, thereby reducing the risk of unintended cultural bias in advertisements.
- **H2:** Combining explicit (knowledge graph-based) and implicit (hypothetical thinking) cultural analysis will lead to a more balanced and contextually aware AI moderation system, mitigating over-censorship while improving fairness across diverse audiences.
- **H3:** The Cultural Iceberg Theory can enhance AI moderation by providing a structured framework that differentiates explicit cultural markers from implicit cultural meanings, reducing misclassification errors in advertisements.

## Cultural Terminology

### Cultural Awareness
- **Definition:** Recognition that different cultures exist and influence people's behaviors, beliefs, and values.
- **Example:** Realizing that bowing is a common greeting in Japan, while handshakes are preferred in the West.

### Cultural Knowledge
- **Definition:** A deeper understanding of different cultures, including their history, values, traditions, and communication styles.
- **Example:** Understanding that in some Middle Eastern cultures, showing the sole of your shoe is considered disrespectful.

### Cultural Sensitivity
- **Definition:** The ability to interact with and respect different cultures without offending or imposing one’s own cultural values.
- **Example:** Avoiding jokes or stereotypes that might be offensive to a particular cultural group.

### Cultural Misunderstanding
- **Definition:** Situations where differences in cultural norms or expectations lead to confusion or incorrect assumptions, often due to a lack of awareness.
- **Example:** A Western manager mistakenly assuming that an employee from an East Asian background is uninterested in leadership roles because they do not actively self-promote.

### Cultural Misconception
- **Definition:** A false or inaccurate belief about a culture, often based on stereotypes, biases, or limited exposure.
- **Example:** Thinking that all people from a certain culture eat spicy food or that a particular nationality is inherently rude.

## What is the Culture Iceberg Theory?
The Culture Iceberg Theory is a powerful analogy that illustrates how much of culture is invisible and intangible. It emphasizes that:
- **Surface-Level (Explicit):** Represents the visible and observable aspects of culture that outsiders first notice.
- **Deep-Level (Implicit):** Represents the unseen, subconscious aspects that influence behaviors, values, and ways of thinking.

Developed by anthropologist **Edward T. Hall in 1976**, this theory underscores that values and beliefs are deeply ingrained, and understanding them is essential for effective cross-cultural communication and content moderation.

### Aspect Comparison: Surface Level vs. Deep-Level
| **Aspect**             | **Surface Level (Explicit)**                         | **Deep-Level (Implicit)**                             |
|------------------------|------------------------------------------------------|-------------------------------------------------------|
| **Visibility**         | Easily seen, observed, or described                  | Hidden, requires deep understanding                   |
| **Detection Method**   | Directly recognizable via rules or knowledge graphs  | Requires hypothesis-driven context analysis           |
| **Examples**           | Clothing, food, language, symbols                    | Power dynamics, historical sensitivities, emotional norms |
| **LLM Role**           | Uses ConceptNet/Knowledge Graphs to map explicit elements | Uses hypothesis thinking to extract objects and analyze cultural depth |

## Methodology
Our methodology integrates both explicit and implicit analysis to enhance AI-driven content moderation through cultural sensitivity. The process involves several key stages:

1. **Data Collection:**  
   - Gathering advertisements and social media content from diverse cultural backgrounds.
   - Curating datasets that include both overt cultural markers and subtle contextual cues.

2. **Explicit Cultural Analysis:**  
   - Utilizing knowledge graphs (e.g., ConceptNet) to identify visible cultural elements such as language, symbols, and attire.
   - Applying rule-based systems to map and tag explicit content features.

3. **Implicit Cultural Analysis:**  
   - Employing hypothesis-driven techniques to extract and analyze hidden cultural meanings.
   - Integrating contextual reasoning models to assess power dynamics, historical sensitivities, and emotional norms that might not be immediately apparent.

4. **Integration and Moderation:**  
   - Combining results from explicit and implicit analyses to generate a comprehensive cultural sensitivity score.
   - Implementing feedback loops where human moderators validate and refine AI decisions, ensuring reduced misclassification and over-censorship.

5. **Evaluation:**  
   - Benchmarking the system against existing moderation frameworks.
   - Conducting user studies to assess cultural fairness and accuracy.

The workflow and integration of these components are visually summarized in the figure below:

![Methodology Overview](./figures/framework-com-ads.png)

## Papers
Below is a curated list of key papers that have contributed to the field, along with their associated resources. Feel free to explore these works for more insights:

- **ACL-2023: Title of the Paper**  
  [paper](#) | [code](#) | *Authors: Author1, Author2, Author3*
- **Example Paper 2**  
  [paper](#) | [code](#) | *Authors: AuthorA, AuthorB*

### Literature Review
This section provides a comprehensive review of existing literature on AI moderation, cultural sensitivity, and related frameworks. It highlights:
- Trends and challenges in AI content moderation.
- The role of cultural sensitivity in improving automated systems.
- Comparative analyses of explicit vs. implicit cultural elements in research.
  
_Additional detailed summaries and comparisons of each work will be added as the literature review is expanded._

## Citation 
If you find this work useful, please consider citing our paper:
```
@misc{tt2025comads,
      title={Content Moderations in Advertisements through Cultural Lens}, 
      author={Todsavad Tangtortan},
      year={2025},
}
```