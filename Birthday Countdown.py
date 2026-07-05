from datetime import datetime
from dateutil import parser
import time
import os

# # -----------------------------
# # Get Birthdate
# # -----------------------------

# while True:
#     user_input = input("🎂 Enter your birthdate: ")

#     try:
#         birth_date = parser.parse(user_input, fuzzy=True)
#         break
#     except ValueError:
#         print("❌ Invalid date. Please try again.\n")

# today = datetime.now()

# # -----------------------------
# # Calculate Next Birthday
# # -----------------------------

# next_birthday = birth_date.replace(year=today.year)

# if next_birthday < today:
#     next_birthday = next_birthday.replace(year=today.year + 1)

# # -----------------------------
# # Calculate Age
# # -----------------------------

# age = today.year - birth_date.year

# if (today.month, today.day) < (birth_date.month, birth_date.day):
#     age -= 1

# # -----------------------------
# # Countdown
# # -----------------------------

# while True:

#     now = datetime.now()

#     remaining = next_birthday - now

#     if remaining.total_seconds() <= 0:
#         os.system("cls" if os.name == "nt" else "clear")
#         print("\n🎉🎂 HAPPY BIRTHDAY! 🎂🎉")
#         break

#     days = remaining.days
#     hours, remainder = divmod(remaining.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)

#     os.system("cls" if os.name == "nt" else "clear")

#     print("=" * 45)
#     print("        🎂 BIRTHDAY COUNTDOWN 🎂")
#     print("=" * 45)

#     print(f"\n👤 Birth Date      : {birth_date.strftime('%d %B %Y')}")
#     print(f"🎈 Next Birthday   : {next_birthday.strftime('%d %B %Y')}")
#     print(f"📅 Day             : {next_birthday.strftime('%A')}")
#     print(f"🎂 Current Age     : {age}")
#     print(f"🎉 Turning         : {age + 1}")

#     print("\n⏳ Time Remaining")
#     print("-" * 30)
#     print(f"📆 Days    : {days}")
#     print(f"🕐 Hours   : {hours}")
#     print(f"⏰ Minutes : {minutes}")
#     print(f"⌛ Seconds : {seconds}")

#     print("=" * 45)

#     time.sleep(1)