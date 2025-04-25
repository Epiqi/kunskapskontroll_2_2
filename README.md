# AI Meal Planner

This application generates personalized weekly meal plans based on your cravings and food preferences for four people.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

3. Modify the `food_preferences.json` file to include the preferences for your four people.

## Usage

Run the application:
```bash
python meal_planner.py
```

Enter your craving when prompted, and the application will generate a personalized meal plan that takes into account:
- Allergies
- Dietary restrictions
- Food preferences
- Dislikes

The meal plan will include:
- Dinner only for Monday to Friday
- Both lunch and dinner for Saturday and Sunday

Type 'quit' to exit the application.

## Features

- Personalized meal planning based on multiple preferences
- Allergy-aware meal suggestions
- Dietary restriction compliance
- Balanced and varied meal options
- Interactive command-line interface 