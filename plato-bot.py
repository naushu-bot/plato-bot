import time
import pandas as pd
from datetime import datetime

print("Plato Bot initializing...")

# यहाँ हम मेंबर्स के मैसेज ट्रैक करने के लिए डेटाबेस बनाएंगे
message_records = {}

def track_message(username):
    """यह फंक्शन चेक करेगा कि किस यूजर ने मैसेज भेजा है और उसका काउंट बढ़ाएगा"""
    if username in message_records:
        message_records[username] += 1
    else:
        message_records[username] = 1
    print(f"Message recorded from {username}. Total: {message_records[username]}")

def generate_weekly_report():
    """यह फंक्शन हर हफ्ते का रिकॉर्ड सेव करेगा"""
    print("\n--- Weekly Report Generating ---")
    df = pd.DataFrame(list(message_records.items()), columns=['Username', 'Message Count'])
    print(df)
    
    filename = f"weekly_report_{datetime.now().strftime('%Y-%m-%d')}.csv"
    df.to_csv(filename, index=False)
    print(f"Report saved as {filename}")
    
    message_records.clear()
    print("Weekly records reset for the next cycle.\n")

if name == "main":
    print("Plato Bot is running and monitoring messages...")
    try:
        track_message("User_A")
        track_message("User_B")
        track_message("User_A")
    except KeyboardInterrupt:
        print("Bot stopped manually.")