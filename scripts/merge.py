"""Gộp bài mới vào data/posts.json.
Dùng: python3 scripts/merge.py new.json   (new.json = [{"id":"pfbid...","title":"...","date":"dd/mm/yyyy"}])
Bài đã có (trùng id) bị bỏ qua. Bài mới được chèn lên đầu (sau các tuyển tập trả phí)."""
import json, re, sys, datetime, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "posts.json"
BASE = "https://www.facebook.com/physicstranslatevn/posts/"
COUNTRY = {"ĐÀI LOAN":"Đài Loan","TRUNG QUỐC":"Trung Quốc","SINGAPORE":"Singapore","THÁI LAN":"Thái Lan","INDONESIA":"Indonesia","PHÁP":"Pháp","ROMANIA":"Romania","NHẬT BẢN":"Nhật Bản","HÀN QUỐC":"Hàn Quốc","MỸ":"Mỹ","NGA":"Nga","ẤN ĐỘ":"Ấn Độ","ÚC":"Úc","CANADA":"Canada","ANH":"Anh","ĐỨC":"Đức","IPHO":"IPhO","APHO":"APhO","EUPHO":"EuPhO","VPHO":"VPhO","HSGQG":"HSGQG"}

def classify(pid, title, date=""):
    t = title.strip().strip("[]"); U = t.upper()
    comp = None; year = None; free = True
    m = re.search(r"20\d\d", t); year = int(m.group()) if m else None
    if "TUYỂN TẬP" in U and ("CHI PHÍ" in U or "PDF" in U or "MUA" in U):
        cat, free = "Tuyển tập (trả phí)", False; summary = "Tuyển tập chuyên đề trả phí — xem giá và cách mua tại bài gốc."
    elif "OLYMPIC" in U or "IPHO" in U or "APHO" in U or "ĐỀ ÔN" in U or "ĐỀ THI" in U:
        cat = "Đề thi Olympic"
        for k, v in COUNTRY.items():
            if k in U: comp = v; break
        if "DHBB" in U: comp = "DHBB"
        if "30/4" in U: comp = "Olympic 30/4"
        summary = "Đề thi/đề ôn — bản dịch tiếng Việt, xem tại bài gốc."
    elif U.startswith("NEXUS"):
        cat, comp = "Chuỗi NEXUS", "NEXUS"; summary = "Chuỗi bài toán NEXUS."
    elif "PHYSICS IN LIFE" in U:
        cat = "Physics in Life"; summary = "Bài toán vật lý ứng dụng trong đời sống."
    else:
        cat = "Bài toán chọn lọc"; summary = "Bài toán kèm file tải ở phần bình luận bài gốc."
    t = re.sub(r"^PHYSICS TRANSLATE\s*-\s*", "", t).strip()
    return dict(id=pid, title=t, category=cat, competition=comp, year=year, free=free, summary=summary, date=date, url=BASE + pid)

if __name__ == "__main__":
    db = json.loads(DB.read_text(encoding="utf-8"))
    have = {x["id"] for x in db["items"]}
    new = [classify(n["id"], n["title"], n.get("date", "")) for n in json.load(open(sys.argv[1], encoding="utf-8")) if n["id"] not in have]
    paid = [x for x in db["items"] if not x["free"]]; rest = [x for x in db["items"] if x["free"]]
    db["items"] = paid + [x for x in new if not x["free"]] + [x for x in new if x["free"]] + rest
    db["updated"] = datetime.date.today().strftime("%d/%m/%Y")
    DB.write_text(json.dumps(db, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"added {len(new)}: " + "; ".join(x["title"] for x in new))
