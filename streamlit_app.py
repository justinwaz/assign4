# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Justin Wang")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "💡 Quote of the Day"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

#Tab 4: Quote of the Day
with tabs[3]:
    st.subheader("💡 Quote of the Day")

    from datetime import date

    quotes = [
        "The best way to predict the future is to create it.",
        "Success is not final, failure is not fatal.",
        "Dream big and dare to fail.",
        "Great things take time.",
        "Work hard in silence, let success make the noise.",
        "Every day is a new opportunity.",
        "Don't watch the clock; do what it does. Keep going."
    ]

    # Choose a different quote each day
    today = date.today()
    quote = quotes[today.toordinal() % len(quotes)]

    st.info(quote)
    st.write(f"📅 {today.strftime('%B %d, %Y')}")
    st.caption("Made by Justin Wang 🚀")
    
