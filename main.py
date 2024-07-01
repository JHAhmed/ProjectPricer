from pathlib import Path
import streamlit as st
from datetime import datetime
import os

st.set_page_config(page_title="Project Pricer", layout="wide", page_icon="📃",
)


services = {
    "Social Media Management": 8000,
    "Content Creation": 5000,
    "E-commerce": 15000,
    "Digital Marketing": 10000,
}

duration = {
    "1 month": 1,
    "3 months": 3,
    "6 months": 6,
    "12 months": 12,
}

col1, col2 = st.columns(2, gap="large")

with col1:
    st.title("Project Pricer")
    st.subheader("By Wurks Studio")
    addition_pages = st.slider("How many additional pages are required?", 0, 10, 2, 1, key="additional_pages")

    if (addition_pages > 9):
        addition_pages_2 = st.slider("How many (more) additional pages are required?", 0, 10, 0, 1, key="additional_pages_2")
    else:
        addition_pages_2 = 0    

    options = st.multiselect(
        "What additional services are required?",
        services.keys()
    )

    timeline = st.selectbox(
    "How long are our (additional) services required (where applicable)?",
    duration.keys(),
    index=1,
    )

    services_cost = 0
    for i in range(len(options)):

        services_cost += services[options[i]] * (duration[timeline] / (list(duration.keys()).index(timeline) + 1))

        services_cost = int(services_cost)
        
    # final_cost = 10000 + 5000 + (addition_pages * 2000) + (addition_pages_2 * 1000) + sum([services[option] * duration[timeline] for option in options]) 
    final_cost = 10000 + 5000 + (addition_pages * 2000) + (addition_pages_2 * 1000) + services_cost 

    st.markdown(
        f"""
        # ₹{final_cost}
        """
    )

with col2:

    services_items = f"    |||"
    if (len(options) > 0):
        services_items = f""
        for i in range(len(options)):

            i_cost = services[options[i]] * (duration[timeline] / (list(duration.keys()).index(timeline) + 1))
            i_cost = int(i_cost)

            if (i + 1 == len(options)):
                services_items += f"    |   {options[i]}  | × {timeline}       | **₹{i_cost}** |"
            else:
                services_items += f"    |   {options[i]}  | × {timeline}       | **₹{i_cost}** |\n"

    # print(services_items)


    markdown_string = f'''
    ## Cost Breakdown
    **Wurks Studio**  
    **Date:** {datetime.now().strftime('%B %d, %Y')}  
    **Notes:** This is **NOT** the final bill, this is a rough estimate!

    | Sub-Item               | Description          | Price    |
    |------------------------|----------------------|---------:|
    | **Website Base Price** |                      | ₹10,000  |
    |                        | Search Engine Optimization   |          |
    |                        | Responsive Design & Development   |          |
    | **Hosting Costs**      |                      |  ₹5,000  |
    |                        | Domain & Maintenance   |          |
    |                        | SSL Certificates & Security   |          |
    | **Additional Pages**   | × {addition_pages + addition_pages_2}   |₹{(addition_pages * 2000) + (addition_pages_2 * 1000)}|
    | **Services**           |         |       |
{services_items}
    |                        | **Subtotal**         | **₹{final_cost}** |

    '''
    print(markdown_string)

    st.markdown(markdown_string)

