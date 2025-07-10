import pandas as pd
import streamlit as st

st.set_page_config(page_title="Alternate Supplier Tool")
st.title("🔍 Alternate Supplier Suggestion Tool")

# Load supplier data
df = pd.read_csv("demo_lead_time.csv")

# UI: Text input
part_input = st.text_input("Enter Part Number (e.g. P003):")

if part_input:
    df_filtered = df[df["part"].str.upper() == part_input.upper()]

    if df_filtered.empty:
        st.warning("❌ No suppliers found for this part.")
    else:
        min_lead = df_filtered["effective_lead_time"].min()

        # Highlight the supplier with lowest lead time
        def highlight_min(row):
            return ['background-color: lightgreen' if row["effective_lead_time"] == min_lead else '' for _ in row]

        st.success(f"✅ Found {len(df_filtered)} supplier(s) for part '{part_input}'")
        st.dataframe(df_filtered.style.apply(highlight_min, axis=1))
