# Contributing to AutoMed Healthcare Chatbot

We love your input! We want to make contributing to this project as easy and transparent as possible.

## Development Process

1. Fork the repo and create your branch from `main`
2. Make your changes
3. Add tests if applicable
4. Ensure the code follows PEP8 guidelines
5. Submit a pull request

## Code Style

- Follow PEP8 guidelines
- Use descriptive variable and function names
- Add comments for complex logic
- Include type hints where appropriate

## Adding New Agents

To add a new specialized agent:

1. Create a new configuration in `config.py`
2. Add the agent to the `configure_agents()` function
3. Update the group chat setup in `main.py`
4. Add tests for the new agent
5. Update documentation

## Testing

Please add tests for new functionality:

- Unit tests for individual functions
- Integration tests for agent interactions
- Test edge cases and error conditions

## Documentation

- Update README.md for significant changes
- Add docstrings to new functions and classes
- Update examples if needed

## Pull Request Process

1. Ensure tests pass
2. Update documentation
3. Request review from maintainers
4. Address review comments
5. Merge after approval

## Bug Reports

When filing an issue, please include:

- Description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details

## Feature Requests

We welcome feature requests! Please include:

- The problem you're trying to solve
- Why this feature is important
- Suggested implementation (if you have one)

## Questions?

Feel free to open an issue with your question or contact the maintainers.