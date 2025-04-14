# Sales Bot Agent

This project contains an agent designed to evaluate the UI/UX of websites by simulating a user journey. The agent is built using the LangChain framework and integrates with Google's Gemini AI model for natural language processing.

## Features

- **Website Navigation**: The agent can navigate through a website, starting from the homepage and exploring primary sections.
- **User Interaction**: It interacts with buttons, links, menus, and forms to simulate a typical user journey.
- **Detailed Feedback**: For each step, the agent provides structured feedback on clarity, usability, design, and any issues encountered.
- **Vision Integration**: The agent can use vision capabilities to enhance its understanding of the website's UI.

## Usage

1. **Setup**: Ensure you have the required dependencies installed. You can install them using pip:

   ```bash
   pip install langchain-google-genai pydantic python-dotenv
   ```

2. **Environment Variables**: Create a `.env` file in the root directory and add your Google Gemini API key:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

3. **Running the Agent**: To run the agent, execute the `agent.py` script. The agent will start evaluating the specified website:

   ```python
   python agent.py
   ```

4. **Output**: The agent's feedback and history will be saved in `logs/history.md`.

## Example

Here's an example of how to run the agent to evaluate a specific website:

```python
asyncio.run(main('https://www.ecolandscaping.org/'))
```

## Feedback Structure

The agent's feedback is structured into several parts:

- **Overall Task Summary**: A brief status of the task.
- **Detailed Step-by-Step Feedback**: Feedback for each step performed, including goals, clarity, usability, design, issues, and positives.
- **Final Summary Feedback**: An overall summary reflecting on the entire process.

## Dependencies

- `langchain-google-genai`: For integrating with Google's Gemini AI model.
- `pydantic`: For data validation and settings management.
- `python-dotenv`: For loading environment variables from a `.env` file.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
