import streamlit as st

# Function to generate marketing prompts
def generate_prompts(name, product_name, company_name, price, value_proposition, target_market):
    if not all([name, product_name, company_name, price, value_proposition, target_market]):
        st.error("Please fill in all fields.")
        return []

    prompts = [
        f"Write a compelling sales pitch for {name}'s product, {product_name}, by {company_name}. Highlight the price of ${price}, the value proposition '{value_proposition}', and appeal to the {target_market}.",
        f"Draft a social media ad for {product_name} that emphasizes its value proposition '{value_proposition}' and targets {target_market}.",
        f"Create a tagline for {product_name} by {company_name} that reflects its value proposition and resonates with {target_market}.",
        f"Write an email marketing campaign for {product_name} with the subject line 'Discover {product_name} - Only ${price} for {target_market}!'.",
        f"Generate a blog post idea for {company_name} that promotes {product_name} and its value to {target_market}.",
        f"Develop a script for a 30-second video ad for {product_name} focusing on '{value_proposition}' for {target_market}.",
        f"Suggest 5 questions {company_name} can ask {target_market} to better understand their needs regarding {product_name}.",
        f"Write a press release announcing the launch of {product_name} by {company_name} at a price of ${price}, highlighting its value proposition for {target_market}.",
        f"Create a comparison ad that shows why {product_name} outshines competitors for {target_market}.",
        f"Suggest a content marketing strategy for promoting {product_name} to {target_market}.",
        f"Write a persuasive customer testimonial for {product_name} by {company_name} focusing on its value to {target_market}.",
        f"Draft a social proof campaign using customer stories for {product_name} targeting {target_market}.",
        f"Propose a referral program for {product_name} by {company_name} to attract more customers in {target_market}.",
        f"Write a script for a webinar to educate {target_market} about {product_name}'s benefits and value proposition.",
        f"Develop a strategy for leveraging influencers to promote {product_name} to {target_market}.",
        f"Create an FAQ section for {product_name} by {company_name} aimed at answering common questions from {target_market}.",
        f"Write a headline for a Google ad promoting {product_name} to {target_market} that emphasizes its unique value proposition.",
        f"Generate a 10-step social media content plan to promote {product_name} by {company_name} for {target_market}.",
        f"Suggest a seasonal marketing campaign for {product_name} that appeals to {target_market} during the holidays.",
        f"Write a customer journey map showing how {target_market} discovers, evaluates, and purchases {product_name}.",
    ]

    return prompts

# Initialize Session State
if "prompts" not in st.session_state:
    st.session_state["prompts"] = []

# Streamlit App
st.title("Marketing Prompt Generator")

# Input Fields
name = st.text_input("Your Name", key="name")
product_name = st.text_input("Product Name", key="product_name")
company_name = st.text_input("Company Name", key="company_name")
price = st.text_input("Price (e.g., 100)", key="price")
value_proposition = st.text_input("Value Proposition", key="value_proposition")
target_market = st.text_input("Target Market", key="target_market")

# Generate Button
if st.button("Generate Prompts"):
    prompts = generate_prompts(
        st.session_state["name"],
        st.session_state["product_name"],
        st.session_state["company_name"],
        st.session_state["price"],
        st.session_state["value_proposition"],
        st.session_state["target_market"],
    )
    st.session_state["prompts"] = prompts

# Display Prompts
if st.session_state["prompts"]:
    st.success("Prompts Generated!")
    for i, prompt in enumerate(st.session_state["prompts"], 1):
        st.markdown(f"**Prompt {i}:** {prompt}")
