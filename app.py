import streamlit as st
import pandas as pd

from lp_solver import solve_lp
from ga_solver import solve_ga
from chatbot import ask_chatbot
from pdf_report import create_report

st.set_page_config(
    page_title="Innovation Park Management System",
    page_icon="🚀",
    layout="wide"
)
st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

.block-container{
    padding-top:2rem;
}

h1,h2,h3{
    color:#0F4C81;
}

div[data-testid="stMetric"]{
    background:#ffffff;
    border-radius:12px;
    padding:15px;
    box-shadow:0 0 8px rgba(0,0,0,.1);
}

div.stButton > button{
    background:#0F4C81;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
}

div.stButton > button:hover{
    background:#1565C0;
}

</style>
""", unsafe_allow_html=True)

st.title("🚀 سیستم هوشمند مدیریت پارک علم و فناوری")

st.sidebar.title("Innovation Park")

page = st.sidebar.selectbox(
    "انتخاب بخش",
    [
        "صفحه اصلی",
        "برنامه‌ریزی خطی (LP)",
        "الگوریتم ژنتیک (GA)",
        "چت‌بات هوشمند"
    ]
)

# ==========================================
# صفحه اصلی
# ==========================================

if page == "صفحه اصلی":

    st.header("🏢 خوش آمدید")

    st.success("سیستم آماده اجرا است.")

    st.info("""
این سامانه برای مدیریت هوشمند پارک علم و فناوری طراحی شده است.

امکانات:

✅ برنامه‌ریزی خطی

✅ الگوریتم ژنتیک

✅ تحلیل هوشمند با Groq AI

✅ تولید گزارش PDF
""")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🚀 استارتاپ‌ها", "20+")

    with col2:
        st.metric("📈 الگوریتم‌ها", "2")

    with col3:
        st.metric("🤖 هوش مصنوعی", "Groq")

    with col4:
        st.metric("📄 گزارش", "PDF")

    st.divider()

    left, right = st.columns(2)

    with left:

        st.success("برنامه‌ریزی خطی")

        st.success("الگوریتم ژنتیک")

        st.success("چت‌بات هوشمند")

    with right:

        st.success("گزارش PDF")

        st.success("نمودارهای مدیریتی")

        st.success("تحلیل نتایج")

    st.divider()

st.success("🚀 سیستم آماده بهره‌برداری است.")

st.caption(
    "Innovation Park Management System 2026"
)

# ==========================================
# برنامه‌ریزی خطی
# ==========================================

if page == "برنامه‌ریزی خطی (LP)":

    st.header("📈 بهینه‌سازی تخصیص بودجه و فضای اداری")

    total_budget = st.number_input(
        "بودجه کل",
        min_value=100,
        value=1000
    )

    total_space = st.number_input(
        "فضای کل",
        min_value=100,
        value=500
    )

    startup_count = st.number_input(
        "تعداد استارتاپ‌ها",
        min_value=1,
        max_value=20,
        value=5
    )

    startups = []

    st.subheader("اطلاعات استارتاپ‌ها")

    for i in range(startup_count):

        st.markdown(f"### استارتاپ {i+1}")

        name = st.text_input(
            "نام",
            value=f"Startup {i+1}",
            key=f"name{i}"
        )

        score = st.number_input(
            "امتیاز",
            0,
            100,
            80,
            key=f"score{i}"
        )

        budget = st.number_input(
            "بودجه موردنیاز",
            0,
            10000,
            100,
            key=f"budget{i}"
        )

        space = st.number_input(
            "فضای موردنیاز",
            0,
            1000,
            20,
            key=f"space{i}"
        )

        startups.append({
            "name": name,
            "score": score,
            "budget": budget,
            "space": space
        })

if st.button("🚀 اجرای برنامه‌ریزی خطی"):

    result, total_score = solve_lp(
        startups,
        total_budget,
        total_space
    )

    if len(result) == 0:

        st.error("هیچ استارتاپی قابل انتخاب نیست.")

    else:

        df = pd.DataFrame(result)

        st.success("بهینه‌سازی انجام شد.")

        st.dataframe(
            df,
            use_container_width=True
        )

        used_budget = df["budget"].sum()
        used_space = df["space"].sum()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "استارتاپ انتخاب‌شده",
                len(df)
            )

        with col2:
            st.metric(
                "امتیاز کل",
                total_score
            )

        with col3:
            st.metric(
                "بودجه مصرفی",
                used_budget
            )

        st.divider()

        st.subheader("📊 نمودار بودجه")

        st.bar_chart(
            df.set_index("name")["budget"]
        )

        st.subheader("🏢 نمودار فضای تخصیص‌یافته")

        st.bar_chart(
            df.set_index("name")["space"]
        )

        st.subheader("⭐ نمودار امتیاز")

        st.bar_chart(
            df.set_index("name")["score"]
        )

        remaining_budget = total_budget - used_budget
        remaining_space = total_space - used_space

        budget_percent = (used_budget / total_budget) * 100
        space_percent = (used_space / total_space) * 100

        st.divider()

        st.subheader("📈 تحلیل مدیریتی")

        st.info(f"""
بودجه مصرف شده:
{used_budget}

بودجه باقی‌مانده:
{remaining_budget}

فضای مصرف شده:
{used_space}

فضای باقی‌مانده:
{remaining_space}

درصد استفاده از بودجه:
{budget_percent:.1f}%

درصد استفاده از فضا:
{space_percent:.1f}%

امتیاز کل:
{total_score}
""")

        filename = create_report(
            result,
            total_score
        )

        with open(filename, "rb") as file:

            st.download_button(
                label="📄 دانلود گزارش PDF",
                data=file,
                file_name="InnovationParkReport.pdf",
                mime="application/pdf"
            )
# ==========================================
# الگوریتم ژنتیک
# ==========================================

if page == "الگوریتم ژنتیک (GA)":

    st.header("🧬 زمان‌بندی تجهیزات آزمایشگاه")

    st.info("""
در این بخش با استفاده از الگوریتم ژنتیک،
زمان‌بندی استفاده از تجهیزات آزمایشگاهی انجام می‌شود.
""")

    company_count = st.number_input(
        "تعداد شرکت‌ها",
        min_value=2,
        value=5,
        key="ga_company"
    )

    equipment_count = st.number_input(
        "تعداد تجهیزات",
        min_value=1,
        value=3,
        key="ga_equipment"
    )

    if st.button("🚀 اجرای الگوریتم ژنتیک"):

        best_schedule, score = solve_ga(
            company_count,
            equipment_count
        )

        df = pd.DataFrame(best_schedule)

        st.success("زمان‌بندی با موفقیت انجام شد.")

        st.dataframe(
            df,
            use_container_width=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "شرکت‌ها",
                company_count
            )

        with col2:
            st.metric(
                "تجهیزات",
                equipment_count
            )

        with col3:
            st.metric(
                "امتیاز",
                score
            )

        st.divider()

        st.subheader("📊 میزان استفاده از تجهیزات")

        equipment_usage = df["تجهیز"].value_counts()

        st.bar_chart(equipment_usage)

        most_used = equipment_usage.idxmax()
        least_used = equipment_usage.idxmin()

        st.success(f"""
🔹 پرکاربردترین تجهیز:

{most_used}

🔹 کم‌استفاده‌ترین تجهیز:

{least_used}
""")

        if st.button("🤖 تحلیل هوشمند"):

            summary = f"""
تعداد شرکت‌ها: {company_count}

تعداد تجهیزات: {equipment_count}

امتیاز: {score}

جدول:

{df.to_string(index=False)}
"""

            prompt = f"""
نتایج زیر مربوط به الگوریتم ژنتیک است.

{summary}

لطفاً:

1- کیفیت زمان‌بندی را بررسی کن.
2- نقاط قوت را توضیح بده.
3- مشکلات احتمالی را بیان کن.
4- پیشنهاد بهبود بده.
5- جمع‌بندی مدیریتی بنویس.

فقط فارسی پاسخ بده.
"""

            answer = ask_chatbot(prompt)

            st.subheader("🤖 تحلیل هوشمند")

            st.write(answer)
            # ==========================================
# چت‌بات هوشمند
# ==========================================

st.warning(
"این دستیار مبتنی بر هوش مصنوعی Groq است."
)

if page == "چت‌بات هوشمند":

    st.header("🤖 دستیار هوشمند پارک علم و فناوری")

    st.info("""
هر سوالی درباره مدیریت پارک علم و فناوری،
استارتاپ‌ها، بودجه، تجهیزات یا بهینه‌سازی دارید بپرسید.
""")

    user_question = st.text_area(
        "سوال خود را وارد کنید",
        height=150
    )

    if st.button("ارسال سوال"):

        if user_question.strip() == "":

            st.warning("ابتدا سوال خود را وارد کنید.")

        else:

            with st.spinner("در حال تحلیل ..."):

                answer = ask_chatbot(user_question)

            st.subheader("پاسخ هوش مصنوعی")

            st.write(answer)
            st.divider()

st.caption(
"""
© 2026 Innovation Park Management System

Developed by Yasamin Hajisalem

Artificial Intelligence • Linear Programming • Genetic Algorithm
"""
)