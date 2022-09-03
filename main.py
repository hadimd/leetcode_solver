import streamlit as st

st.set_page_config(
    page_title="Hadi's Leetcode Solver",
    page_icon="https://www.flaticon.com/free-icon/rubber-duck_1012600#",
    layout="wide"
)

st.header("Please copy and paste your leetcode question here")

question: str = st.text_area(
    label="Copy and paste question here",
    height=400
)

if st.button("Get Answer"):
    st.header("Python Leetcode Solution")
    st.text("""
    class Solution:
        def twoSums(self, arr: List[str]) -> Tuple[int, int]:
            return [0, 1]
    """)