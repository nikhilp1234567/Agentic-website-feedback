from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv
import asyncio
load_dotenv()

from browser_use import SystemPrompt
from langchain_core.messages import SystemMessage
from overrides import overrides
class MySystemPrompt(SystemPrompt):
    @overrides
    def get_system_message(self) -> SystemMessage:
        
        # Get existing rules from parent class
        existing_prompt = self.prompt_template.format(max_actions=self.max_actions_per_step)

        # Add custom rule
        new_prompt = """
       10. **FINAL OUTPUT AND FEEDBACK STRUCTURE (VERY IMPORTANT):**
       - You MUST structure the `text` parameter of the `done` action PRECISELY as follows:
       - **Part 1: Overall Task Summary:**
         - Start with a brief status and reiterate the website name (e.g., "Completed 5 out of 10 steps for www.pullandbear.com.", "Task finished successfully for www.pullandbear.com..", "Stopped due to error on step 3 on website www.pullandbear.com..").
       - **Part 2: Detailed Step Feedback Section Header:**
         - Include the exact, unique marker line: `=== DETAILED STEP-BY-STEP FEEDBACK ===`
       - **Part 3: Feedback for Each Completed Step:**
         - For EACH step you actually performed:
             - **Step Marker:** Use an exact, unique marker like `--- STEP [StepNumber]: [Description of Action] ---` (e.g., `--- STEP 1: Navigated to Homepage ---`).
             - **Structured 'Think Aloud' Feedback:** Below the step marker, provide extremely detailed feedback using the specific fields requested in the ultimate task, clearly labelled:
                 * `* **Goal:** [Your goal for this step]`
                 * `* **Clarity & Intuitiveness:** [Your assessment]`
                 * `* **Usability:** [Your assessment]`
                 * `* **Design & Layout:** [Your assessment]`
                 * `* **Issues:** [Note any issues or 'None']`
                 * `* **Positives:** [Note any positives or 'None']`
       - **Part 4: Final Summary Feedback Section Header:**
         - Include the exact, unique marker line: `--- Feedback Thoughts ---`
       - **Part 5: Overall Summary Feedback Text:**
         - Below this header, provide an extremely detailed and long  **overall summary** reflecting on the entire process, cross-step observations and general usability impressions, with specific areas for improvement. **This section should NOT just repeat the detailed step feedback.** It's your high-level takeaway.
it is IMPORTANT to format the content here in a way that will make it readable part by part and step by step in a markdown file."""

        # Make sure to use this pattern otherwise the exiting rules will be lost
        return SystemMessage(content=f'{existing_prompt}\n{new_prompt}')

# Create agent with the model
async def main(website):
    agent = Agent(
    initial_actions = [{'go_to_url': {'url': website}}],
        task="Act as a meticulous user tester, evaluating the UI/UX of the current website. You must stay within this website but can navigate its pages freely. Simulate a typical user journey: 1.  **Start:** Begin at the current page (assume it's a primary entry point like the homepage). 2.  **Explore Sequentially:** Examine the main navigation, click through primary sections, and follow logical user paths (e.g., trying to learn about the service/product, find contact info, or understand the site's purpose). 3.  **Interact:** Engage with buttons, links, menus, and forms as appropriate for your exploration. 4.  **'Think Aloud' Feedback:** For each step, provide feedback within a response field `Feedback` covering: * **Goal:** What were you trying to achieve on this page or by clicking that element? * **Clarity & Intuitiveness:** Was the purpose clear? Was the language understandable? Were icons/buttons self-explanatory? * **Usability:** How easy was it to perform the action or find the information? Did anything cause friction or confusion? * **Design & Layout:** Comment briefly on the visual appeal, consistency, and readability. * **Issues:** Note any broken links, slow loading times (if perceivable), errors, or confusing elements. * **Positives:** Mention anything particularly well-designed or easy to use.", 
        llm= ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(os.getenv('GEMINI_API_KEY'))),
        use_vision=True,           
        system_prompt_class= MySystemPrompt
    )


    history = await agent.run(max_steps=10)

    with open('logs/history.md', 'w') as f:
        f.write(f"{history.final_result()}\n")        

asyncio.run(main('https://www.ecolandscaping.org/'))
