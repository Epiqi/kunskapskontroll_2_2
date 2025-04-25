import json
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MealPlanner:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.preferences = self._load_preferences()

    def _load_preferences(self):
        with open('food_preferences.json', 'r') as f:
            return json.load(f)

    def generate_meal_plan(self, craving):
        # Create a prompt that includes all preferences and the craving
        prompt = f"""Create a weekly meal plan based on the following craving: {craving}
        Take into account these food preferences for 4 people:
        {json.dumps(self.preferences, indent=2)}

        The meal plan should include:
        - Dinner only for Monday to Friday
        - Both lunch and dinner for Saturday and Sunday
        
        Format the response as a clear, organized menu with days and meals.
        Make sure to:
        1. Avoid any allergens mentioned
        2. Respect dietary restrictions
        3. Include a mix of liked foods
        4. Avoid disliked foods
        5. Create balanced and varied meals
        6. Make sure that the recipes are varied and not the same thing every day
        7. IMPORTANT: Include the craved ingredient ({craving}) in MAXIMUM 3 meals throughout the week. The other meals should be completely different and not include this ingredient.
        8. Make sure that the recipes are healthy
        9. Create a good mix of different types of meals (more with meat, less vegetarian, some with fish and chicken, etc.)
        10. Make sure to use different cooking methods (baking, grilling, frying, etc.)
        11. Make sure to include a recipe for every meal after the week is planned
        12. Make sure everyone is happy with the plan
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful meal planning assistant. You must strictly follow the rules about limiting the craved ingredient to maximum 3 times in the week."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message['content']
        except Exception as e:
            return f"Error generating meal plan: {str(e)}"

def main():
    planner = MealPlanner()
    print("Welcome to the AI Meal Planner!")
    print("Enter your craving or type 'quit' to exit:")
    
    while True:
        craving = input("What are you craving? ").strip()
        if craving.lower() == 'quit':
            break
            
        meal_plan = planner.generate_meal_plan(craving)
        print("\nHere's your personalized meal plan:")
        print(meal_plan)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main() 