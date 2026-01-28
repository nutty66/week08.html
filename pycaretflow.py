import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# โหลดข้อมูลและสร้าง Pipeline (จาก Lab ที่เราทำกัน)
# ... (ใส่โค้ด Pipeline ที่คุณรันผ่านล่าสุด) ...

# วิเคราะห์ผลลัพธ์ด้วย AI
def ai_critique(acc, f1):
    prompt = f"Accuracy {acc}, F1 {f1}. วิเคราะห์ว่าโมเดลนี้พร้อมใช้งานหรือไม่?"
    # ส่วนนี้คือส่วนที่คุณนำไปถาม AI แล้วนำคำตอบมาใส่ใน README.md
    return "โมเดลพร้อมใช้งานในระดับทดสอบ แต่ควรปรับจูนคลาสที่ข้อมูลน้อย"

# บันทึกผลลง README.md อัตโนมัติ
with open("README.md", "a", encoding="utf-8") as f:
    f.write(f"\n## AI Model Analysis Result\n")
    f.write(ai_critique(0.90, 0.88))
