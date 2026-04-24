# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

def run_semantic_checks(doc_dict: dict) -> bool:
    content = doc_dict.get("content", "")
    
    # 1. Kiểm tra độ dài: Nếu content trống hoặc < 10 ký tự -> False
    if not content or len(content.strip()) < 10:
        print("Watchman Alert: content is empty or too short.")
        return False
    
    # 2. Kiểm tra từ khóa lỗi
    toxic_keywords = ["Null pointer exception", "OCR Error", "Traceback"]
    for keyword in toxic_keywords:
        if keyword.lower() in content.lower():
            print(f"Watchman Alert: toxic keyword detected -> {keyword}")
            return False
            
    return True
