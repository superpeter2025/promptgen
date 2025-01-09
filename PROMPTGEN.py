import tkinter as tk
from tkinter import messagebox

# Function to generate marketing prompts
def generate_prompts():
    name = entry_name.get()
    product_name = entry_product_name.get()
    company_name = entry_company_name.get()
    price = entry_price.get()
    value_proposition = entry_value_proposition.get()
    target_market = entry_target_market.get()

    if not all([name, product_name, company_name, price, value_proposition, target_market]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

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

    # Display prompts in the text box
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, "\n\n".join(prompts))

# GUI Setup
root = tk.Tk()
root.title("Marketing Prompt Generator")

# Input Fields
fields = ["Name", "Product Name", "Company Name", "Price", "Value Proposition", "Target Market"]
entries = []

for idx, field in enumerate(fields):
    label = tk.Label(root, text=field)
    label.grid(row=idx, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root, width=40)
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries.append(entry)

entry_name, entry_product_name, entry_company_name, entry_price, entry_value_proposition, entry_target_market = entries

# Submit Button
submit_button = tk.Button(root, text="Submit", command=generate_prompts)
submit_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

# Output Text Box
text_output = tk.Text(root, wrap=tk.WORD, width=80, height=20)
text_output.grid(row=len(fields) + 1, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
