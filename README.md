# Sort Packages - Automation System

This project contains a function that sorts packages based on their dimensions and mass. It is designed for an automation system where packages need to be dispatched to different stacks based on specific criteria.

## Objective

The goal of this system is to classify packages into three categories:

- **STANDARD**: For packages that are neither bulky nor heavy. These can be handled normally.
- **SPECIAL**: For packages that are either bulky or heavy. These require special handling.
- **REJECTED**: For packages that are both bulky and heavy. These packages cannot be handled automatically and are rejected.

### Classification Criteria:

- A package is **bulky** if:
  - Its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³.
  - Or if one of its dimensions is greater than or equal to 150 cm.

- A package is **heavy** if:
  - Its mass is greater than or equal to 20 kg.

## How It Works

- The function `sort_packages(width, height, length, mass)` classifies a package based on its volume and mass into one of the following categories:
  - `"REJECTED"`: If the package is both bulky and heavy.
  - `"SPECIAL"`: If the package is either bulky or heavy, but not both.
  - `"STANDARD"`: If the package is neither bulky nor heavy.

## Installation

To run this project locally, you need to have Python 3.x installed. Follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/sort-packages.git
cd sort-packages
```


2. Install the required dependencies:

You can install the required dependencies using the requirements.txt file. Run the following command (Linux bash):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip 
pip install -r requirements.txt
```

This will install the necessary packages, such as pytest for running the tests.

## Running the Tests
To ensure everything is working correctly, you can run the tests using pytest. From the project directory, execute:

```bash
pytest .
```
This will run all the test cases and display the results.

## Command-Line Usage
You can also run the script directly from the command line by passing the dimensions and mass as arguments.


### Command-Line Arguments:
The script expects four arguments: width, height, length, and mass, in that order.

Example command:

```bash
python run_sort.py 100 100 101 21
```

This will print the result of the sort_packages function based on the provided package dimensions and mass. For example, it will print "REJECTED" if the package is both bulky and heavy.



  <div>
  <h1 align="center"> Contact </h1> 
  <div align="center">
    <table>
        </tr>
            <td>
                <a  href="https://www.linkedin.com/in/robinsonbrz/">
                <img src="https://raw.githubusercontent.com/robinsonbrz/robinsonbrz/main/static/img/linkedin.png" width="50" height="50">
            </td>
            <td>
                <a  href="https://www.linkedin.com/in/robinsonbrz/">
                <img  src="https://avatars.githubusercontent.com/u/18150643?s=96&amp;v=4" alt="@robinsonbrz" width="50" height="50">
            </td>
            <td>
                <a href="https://www.enedino.com.br/contato">
                <img src="https://raw.githubusercontent.com/robinsonbrz/robinsonbrz/main/static/img/gmail.png" width="50" height="50" ></a>
            </td>
        </tr>
    </table> 
  </div>
  <br>
</div>








