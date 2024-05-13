# API integration testing with python

## Instructions

Create a testing framework that uses `pytest` to run functional integration tests for the API: [Cat Facts API](https://catfact.ninja/#/.). The framework should:

- Have a way of configuring the tests to target different environments, for example, another instance of the API at (an hypothetical): `https://dev.catfact.ninja`.
- Make HTTP requests and assert the data returned is correct.
- Be hosted in a public GitHub repository.

### Bonus

- Use GitHub workflows to run the integration tests automatically Monday to Friday at noon.
