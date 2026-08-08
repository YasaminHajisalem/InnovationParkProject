import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API:", api_key)

client = None

if api_key:
    try:
        client = Groq(api_key=api_key)
    except Exception:
        client = None


def offline_answer(question):

    q = question.lower()

    if "بودجه" in question:
        return (
            "بودجه یکی از محدودیت‌های اصلی مدل است. "
            "در صورت افزایش بودجه، امکان انتخاب استارتاپ‌های بیشتری وجود دارد."
        )

    elif "فضا" in question:
        return (
            "فضای اداری یکی از منابع محدود پارک علم و فناوری است. "
            "مدل تلاش می‌کند با رعایت محدودیت فضا، بیشترین امتیاز را کسب کند."
        )

    elif "برنامه" in question or "lp" in q:
        return (
            "برنامه‌ریزی خطی برای تخصیص بهینه بودجه و فضای اداری به استارتاپ‌ها استفاده شده است."
        )

    elif "ژنتیک" in question or "ga" in q:
        return (
            "الگوریتم ژنتیک برای زمان‌بندی استفاده شرکت‌های دانش‌بنیان از تجهیزات آزمایشگاه مرکزی استفاده می‌شود."
        )

    elif "استارتاپ" in question:
        return (
            "استارتاپ‌هایی که امتیاز بیشتری دارند و محدودیت‌های بودجه و فضا را رعایت می‌کنند، احتمال انتخاب بیشتری دارند."
        )

    elif "تابع هدف" in question:
        return (
            "تابع هدف مدل، بیشینه کردن مجموع امتیاز استارتاپ‌های انتخاب‌شده است."
        )

    elif "سلام" in question:
        return "سلام! من دستیار هوشمند پارک علم و فناوری هستم."

    else:
        return (
            "در حال حاضر پاسخ آفلاین ارائه شد. "
            "می‌توانید درباره بودجه، فضا، برنامه‌ریزی خطی، الگوریتم ژنتیک یا مدیریت استارتاپ‌ها سؤال بپرسید."
        )


def ask_chatbot(question):

    if client is None:
        return offline_answer(question)

    try:

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """
تو یک دستیار هوشمند برای پروژه مدیریت پارک علم و فناوری و مرکز رشد نوآوری هستی.

وظایف:
- پاسخ به سوالات درباره پارک علم و فناوری
- توضیح برنامه‌ریزی خطی (LP)
- توضیح الگوریتم ژنتیک (GA)
- تحلیل تخصیص بودجه و فضا
- پاسخ درباره استارتاپ‌ها
- ارائه پیشنهاد مدیریتی
- پاسخ‌ها فقط به زبان فارسی باشند.
- پاسخ‌ها کوتاه، دقیق و کاربردی باشند.
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception:

        return offline_answer(question)