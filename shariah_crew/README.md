# ShariahCrew Crew

Welcome to the ShariahCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/shariah_crew/crew.py` to define your agents
- Modify `src/shariah_crew/crew.py` to define your tasks
- Modify `src/shariah_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/shariah_crew/main.py` to add custom inputs for your agents and tasks

We're using different models for different agent for optimization and fast response.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the src folder of the project:

```bash
$ pip install uvicorn
```

```bash
$ uvicorn shariah_crew.main:app --host 0.0.0.0 --port 8000 --reload
```
This command initializes the shariah_crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This will startup an application and gives you a URL for the API you need to follow by /docs to interact with the agent through Swaggey UI

POST -> Try Out -> change the token name -> Execute and wait for the response.

## Understanding Your Crew

The shariah_crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `crew.py`, leveraging their collective skills to achieve complex objectives. The `crew.py` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the ShariahCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
