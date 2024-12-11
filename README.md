# AI Presentation Generator

Automate and personalize PowerPoint presentations using OpenAI and Python.

## Features
- Topic-driven slide generation: Input a topic and get a structured presentation.
- Interactive interface: Built with Streamlit for ease of use.
- AI-powered content: Uses OpenAI's GPT-3.5-turbo to generate subtopics and slide content.
- **Customizable**: Modify parameters like slide count and API prompts.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- Streamlit
- OpenAI Python SDK
- Python-PPTX

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-presentation-generator.git
   cd ai-presentation-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key:
   Replace the `api_key` variable in the script with your OpenAI API key:
   ```python
   api_key = "your_openai_api_key"
   openai.api_key = api_key
   ```

### Usage

1. Run the Streamlit app:
   ```bash
   streamlit run PPT_Generator.py
   ```

2. Enter your topic and the desired number of slides (up to 10).

3. Click **Generate Presentation** to create the slides.

4. Download the generated presentation file (`{topic}_presentation.pptx`) directly from the interface.

---

## Code Overview

The script consists of:

- **Streamlit for UI**: Captures user input for topic and number of slides.
- **OpenAI API**: Generates subtopics and slide content.
- **Python-PPTX**: Creates the PowerPoint file with a title and content for each slide.

Key parameters:
- `max_tokens`: Controls the length of generated text.
- `time.sleep(10)`: Ensures compliance with API rate limits.

---

## Customization

- **Adjust Text Length**: Modify `max_tokens` for OpenAI API requests.
- **Change Slide Layouts**: Update `slide_layouts` for different designs.
- **API Rate Limits**: Adjust the sleep duration based on your OpenAI plan.

---

## Example Output

1. Generated Slides: A PowerPoint file with slides based on the provided topic.




