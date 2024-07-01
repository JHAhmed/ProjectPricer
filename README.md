# Project Pricer

Project Pricer is a Streamlit web application developed by Wurks Studio to quickly calculate and visualize rough price estimates for website development projects.

## Features

- Calculate base price for website development
- Add costs for additional pages
- Include pricing for various additional services:
  - Social Media Management
  - Content Creation
  - E-commerce
  - Digital Marketing
- Adjust pricing based on service duration
- Generate an itemized cost breakdown
- Responsive design for easy use on different devices

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/project-pricer.git
   cd project-pricer
   ```

2. Install the required packages:
   ```
   pip install streamlit
   ```

3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage

1. Open the app in your web browser (typically at `http://localhost:8501`).
2. Use the sliders and dropdown menus to input project details:
   - Number of additional pages
   - Additional services required
   - Duration of services
3. View the total estimated cost and detailed cost breakdown.

## Customization

You can easily customize the pricing structure by modifying the `services` and `duration` dictionaries in the script.

## Note

This tool provides rough estimates and is not intended for generating final bills. Always review and adjust the pricing based on specific project requirements and your business policies.
