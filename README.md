### Akinkunmi Interview Solution

Interview App

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch main
bench install-app akinkunmi_interview_solution
```
### API Usage
To access the custom api
```bash
use http://{url}/api/method/{appName}.api.customer_api
```

Then pass the example json to the body using either PUT or POST
```bash
POST - to create customer,
PUT - to update customer

id for customer is mobile_number
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/akinkunmi_interview_solution
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
