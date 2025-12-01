month = 1
paid_months = 0

while month<=12:
    status = input(f"{month}-oy ijarani to`ldizmi? (ha/yoq): ")
    try:
        if status.lower() not in ("ha","yoq"):
            raise ValueError("Faqat ha yoki yoq")
        
    except  ValueError as e:
        print("xatolik",e)
    if status == "ha":
        paid_months+=1
    month+=1
print(f"siz {paid_months} oy ijarani to`ladingiz.")