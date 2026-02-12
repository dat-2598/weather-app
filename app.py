import streamlit as st

st.set_page_config(layout="wide")

# ===== HEADER =====
col1, col2, col3 = st.columns([1, 4, 2])

with col1:
    st.image("https://via.placeholder.com/120x80.png?text=Logo+1")

with col2:
    st.markdown(
        """
        <h1 style='text-align:center; color:#2d7d32;'>
        BẢN TIN KHÍ HẬU NÔNG NGHIỆP<br>
        VÙNG DỰ ÁN SACCR KHÁNH HÒA
        </h1>
        <h4 style='text-align:center; color:#B8860B;'>
        Dự án tăng cường khả năng chống chịu của nông nghiệp quy mô nhỏ
        </h4>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.image("https://via.placeholder.com/200x80.png?text=Logo+2")

st.divider()

# ===== MENU =====
st.subheader("Chức năng")

colA, colB, colC, colD = st.columns(4)

with colA:
    st.link_button("Hiện trạng cây trồng - Khánh Sơn",
                   "https://docs.google.com/spreadsheets/d/1oKPQjOq0_syQFnt_CEMUl0h4CKJodnCx3z3bVOhyks0")

with colB:
    st.link_button("Bản tin 10 ngày - Khánh Sơn",
                   "https://example.com")

with colC:
    st.link_button("Bản tin 3 tháng - Khánh Sơn",
                   "https://example.com")

with colD:
    st.link_button("Bản tin 6 tháng - Khánh Sơn",
                   "https://example.com")

st.divider()

# ===== MAIN IMAGE =====
st.image("https://images.unsplash.com/photo-1501004318641-b39e6451bec6",
         use_container_width=True)

st.divider()

# ===== FOOTER =====
st.markdown("""
**Trưởng nhóm ACIS tỉnh Khánh Hòa:** Ông Võ Văn Công  
**Chi cục Trồng trọt & BVTV:** Bà Lương Kim Ngân  
**Đài KTTV tỉnh Khánh Hòa:** Ông Nguyễn Văn Lý  

**IMHEN:** Ông Trịnh Hoàng Dương  
""")
