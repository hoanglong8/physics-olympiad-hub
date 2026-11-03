import json, re, sys, datetime
raw = """pfbid029SMsTzNhi151ouZY3Qok4CdcAYdiEJBFu2YzLuK7Nz4s9MN96FgxLQcbmPwYMrTgl ~ [CHỌN ĐỘI TUYỂN OLYMPIC VẬT LÝ ĐÀI LOAN NĂM 2026]
pfbid02M9kqtnaf6Yyp66vTgCTnRLYZckJLdm6fpv5nzbr5DnYFmiqsCK7rSdHsipLzQWg6l ~ NEXUS | #15 - Điện từ học: Nam châm Bitter
pfbid02gYczDVzR9FGf1yBy9Ud5o5Lq5vjawaEgCMR42R9Zi3E6mycyvgEitEdHupo39ywCl ~ [OLYMPIC VẬT LÝ TRUNG QUỐC NĂM 2026 - VÒNG CHUNG KẾT]
pfbid0YkVVSSeXHPw7jBV9fGjupYqjWCW7BMEDNtZAjn3V63vFGkUdkqout9tw32pDHZQ6l ~ NEXUS | #14 - Nhiệt học: Công nghệ tăng trưởng màng mỏng MOCVD
pfbid0MVxjBW78GuVcMBuV4SPaS3LqgMQ2nvTpuhjtWAGYhzm6WQ2kNx6oJnfvkxERZeUBl ~ NEXUS | #13 - Cơ học: Bộ bài 52 lá
pfbid02u4ef6qU8wa32dNfnBdY2DrW4XxYkysrENgpTZmrikPcqJNkCC3Nh7onWnZX3KfN5l ~ NEXUS | #12 - Thực nghiệm: Viên nang đàn hồi
pfbid0386Gtj6UnL77iJ7djLDBuGZFqDnPMC64Jo2wqPtuytSyQ89cL8Hzzc9QF9yzK2eYtl ~ NEXUS | #11: Vật lý hiện đại - Tế bào quang điện và hiệu suất chuyển đổi năng lượng Mặt Trời
pfbid021xuWYqUJrAC95fupCBquRYAYtEHjjDXF3A6cLFdsyWGkSFQeNxRhcDuJeuLaAn2yl ~ NEXUS | #10: Quang học - Khảo sát giao thoa khe Young
pfbid02barP6EdB3rXHY285VZwcbryKH6p1ZWhcmiY1EYhn5XtRWmxLmGyAAAMVuVePubFbl ~ NEXUS | #9: Điện từ học - Tác động của tĩnh điện lên quá trình mở dù nhảy
pfbid027fNjUsfEFky4AgidJ2JGdMx8CX4EHmANPjP4M68sjyjbjjNAPa8RCArYFDVstXiWl ~ NEXUS | #8 - Nhiệt học: Hiện tượng trễ góc thấm ướt
pfbid02Ng7E1yoRzFx6AvwvH9oo8cPyUzpYJQxWWAEhQmoukgJ8q3QyhGGq3TyM5kt4CQssl ~ NEXUS | #7 - Cơ học: Chú chó vẫy nước
pfbid0ELR9cMLfq7pwqSEx9kty7LjUf1nSawwSwXjd2sGXoUYZs53swSuGDzkQjYgdLSS3l ~ NEXUS | #6 - Thực nghiệm: Đo hệ số dẫn nhiệt của nước đá
pfbid02fAu1LKPqbQYBz31RWkRdPCVENheRSLp9j9Tr3Dn5iTwqZ67cWFHGQfu8MohuCPFUl ~ NEXUS | #5 - Vật lý Hiện đại: Chào hỏi tương đối tính
pfbid02xL28tGBLjcAZG3SAP5o4MZJ7ftwfzv8com8xsnoUgEgk7NJyWrD4TVpfw7repkiXl ~ [CHỌN ĐỘI TUYỂN OLYMPIC SINGAPORE NĂM 2026]
pfbid02s9anniuLnsqwNoBDB5SXP53Lyw2Z31paRBMnMJDP7xkReB2wU9YkDKqNEStHA8cBl ~ NEXUS | #4: Quang học - Thấu kính GRIN
pfbid02ThUouTo33BeNkSvPWo8qe8W241PATuHFJBUuqi15ZG4ovtk7LCjfMdhF4EaQGhGPl ~ NEXUS | #3: Điện từ học - Mô hình hai thung lũng năng lượng và Hiệu ứng Gunn
pfbid0sr6oquAnoqpP6uKnM2yd2iU1eddNM1Nt7b9b9BwS3ZSVUtqzoavdVBDE5ViKUCf7l ~ [OLYMPIC VẬT LÝ THÁI LAN NĂM 2026]
pfbid02Qx2vSoXBTRjgefg9jvp1w7kejgJRv9UKmMxGCvsdw72KpjC8R1GFQn6m8t6QdfaBl ~ NEXUS | #2: Nhiệt học - Chu trình vô cùng nhỏ của máy bơm nhiệt
pfbid0NqW2QdcDFw8TVpU4FqSiYZLEdaRe6S7TA8dfwovWx41avtaHh36sJCV8Re1hpcSjl ~ [OLYMPIC VẬT LÝ INDONESIA NĂM 2026]
pfbid02kHBgKPdW6kREUNHarCAUUXkWgTmxLisYfs1nuz2EJdkjMiDDY68HV7W7NSBsCvAil ~ NEXUS | #1: Cơ học - Đồ chơi "Tiên bay"
pfbid09U7H4TMFzbGbWqWw3f2rh1sPTjqpSpiPM2UHAkpaTkQhWFAGttMvDbEBD8Et1yC1l ~ [CHỌN ĐỘI TUYỂN OLYMPIC PHÁP NĂM 2026]
pfbid02YgtRmmUu4Ey1M1qpjNw14Xp7cQSbmb83x4stPwWbJzPkbwf35uDEPSYJXkpkdw1el ~ [CHỌN ĐỘI TUYỂN OLYMPIC ROMANIA NĂM 2026]
pfbid02dyfA54Xpr228KVy6j5YXfSchjdMTLfhQ4yU3U1nXH3QewmyjwTJ9CG6QBFLNmGVSl ~ [OLYMPIC VẬT LÝ ROMANIA NĂM 2026 - LỚP 12]
pfbid0nhxUnck4MtzW8vdFg3dVLgBeZrkkNUvQb1Z8ZaL24xp6PKkq88NDYmWtNv9tSdvil ~ PHYSICS TRANSLATE - NHIỄU ĐỘNG KEPLER VÀ SỰ BIẾN THIÊN CÁC THAM SỐ QUỸ ĐẠO
pfbid02vFLqT5ZH3n2zfZyGE2qLTjXxz2NgD7kJ75y4NSNTb4sNicAkYiWV6E6ghH3PhhHwl ~ PHYSICS TRANSLATE - ĐỀ ÔN TẬP DHBB
pfbid02VVZHic4Fms8cHFj8GUFYsRCxXym5JNQd37a6JsFxTMzSNvXkTq4HPv6irVK22Zuzl ~ PHYSICS TRANSLATE - MÔ HÌNH MUZER CỦA NHÀ MÁY ĐIỆN MẶT TRỜI HỘI TỤ
pfbid02XUSrRp3AREbXr9X4kdgwLMgQtqxXnrdCCC2gCgCKtaTGTKa4SVsMwhZJgABBe6Rkl ~ PHYSICS TRANSLATE - CẢM BIẾN ĐIỆN DUNG ĐO MỨC CHẤT LỎNG
pfbid0XnaPSgDuxbXJqxw5ZVzpXYZvy1jC7e32S39eTrqpkJEscwLv6cJZ43mPoimWGp9Sl ~ PHYSICS TRANSLATE - PHYSICS IN LIFE: CÔNG NGHỆ CẢM BIẾN VÂN TAY DƯỚI MÀN HÌNH
pfbid02i1NHqY2RiSenvNuFRJWHAr7kQJKWPi6uu8q7FHC3Tuf9UhimRd1EvpEDis4mgyFVl ~ PHYSICS TRANSLATE - MÔ HÌNH DAO ĐỘNG TẬP THỂ CỦA ĐÁM MÂY ĐIỆN TỬ
pfbid02uUtpebP1CdMrFj9Uhzy8k17UshH8VWueh6eNjmBtBFVvsBSdZrHdrMkTfCY8j1zol ~ PHYSICS TRANSLATE - ĐỀ ÔN TẬP 30/4
pfbid0ZJvmZsSgrFUxXUffML8EeUvTE76WPCgM8b4R2szMepJ3aRKYUQsmFM7TwTPPRxXKl ~ PHYSICS TRANSLATE - PHYSICS IN LIFE: CAMERA NHẬN DIỆN BIỂN SỐ XE"""
BASE="https://www.facebook.com/physicstranslatevn/posts/"
paid = [
 ("pfbid02beZk78HWcVxxBcxd3qAzpPzWYvoDRqdn2vGotBtP8JSapsovF2A7kuYq3ks1Tj5yl","Tuyển tập Vật lý: Chuyên đề Nhiệt học (Thermodynamics)","80 bài: mao dẫn & căng bề mặt, chuyển pha, khí Van der Waals, vật lý thống kê, hiện tượng vận chuyển. PDF 199k (watermark cá nhân).","16/09/2026"),
 ("pfbid07Si2Yb1Xzs5qYyxgF3P5FnftgY4pNcGhDbJs3V19i4q3LbN94KFG41f4MjMSgSVKl","Tuyển tập Vật lý: Chuyên đề Cơ học (Mechanics)","85 bài: động lực học chất điểm & vật rắn, dao động, đàn hồi, cơ học thiên thể (giới hạn Roche, bài toán ba vật). PDF 279k.","08/09/2026"),
 ("pfbid0hgNChVbocRpb13LaLN9JWvapSXMRCxRNeJ7dyyj29kmxLWyTdhcaSC4bhKokyqHgl","Tuyển tập Vật lý: Quang sóng - Giao thoa (Wave Optics)","77 bài: khe Young, gương Fresnel, vân Newton, giao thoa kế Michelson/Fabry-Pérot/Mach-Zehnder/Sagnac. PDF 250k, có bản demo 9 bài miễn phí ở bình luận.","09/03/2026"),
]
COUNTRY={"ĐÀI LOAN":"Đài Loan","TRUNG QUỐC":"Trung Quốc","SINGAPORE":"Singapore","THÁI LAN":"Thái Lan","INDONESIA":"Indonesia","PHÁP":"Pháp","ROMANIA":"Romania"}
items=[]
for i,line in enumerate(raw.splitlines()):
    pid,title=[x.strip() for x in line.split(" ~ ",1)]
    if pid==paid[2][0]: continue
    t=title.strip("[]")
    comp=None; year=None
    if "OLYMPIC" in t:
        cat="Đề thi Olympic"
        for k,v in COUNTRY.items():
            if k in t: comp=v
        m=re.search(r"20\d\d",t); year=int(m.group()) if m else None
        summary=("Đề chọn đội tuyển " if "CHỌN ĐỘI TUYỂN" in t else "Đề thi Olympic Vật lý ")+f"{comp} {year or ''}".strip()+" — bản dịch tiếng Việt, đăng dạng ảnh."
        t=t.capitalize().replace("olympic","Olympic").replace("vật lý","Vật lý")
        for k,v in COUNTRY.items(): t=t.replace(k.lower(),v)
        t=t.replace(" năm "," ")
    elif t.startswith("NEXUS"):
        cat="Chuỗi NEXUS"; comp="NEXUS"
        m=re.match(r"NEXUS \| #(\d+)\s*[-:]\s*(.*)",t)
        summary=f"Chuỗi bài toán NEXUS số {m.group(1)}."; t=f"NEXUS #{m.group(1)} — {m.group(2)}"
    elif "PHYSICS IN LIFE" in t:
        cat="Physics in Life"; t=t.split("PHYSICS IN LIFE:")[1].strip().capitalize(); summary="Bài toán vật lý ứng dụng trong đời sống."
    else:
        t=t.replace("PHYSICS TRANSLATE - ","").strip().capitalize().replace("kepler","Kepler").replace("muzer","Muzer")
        cat="Đề thi Olympic" if "ÔN TẬP" in title else "Bài toán chọn lọc"
        if "DHBB" in title: comp="DHBB"; t="Đề ôn tập DHBB (Duyên hải Bắc Bộ)"
        if "30/4" in title: comp="Olympic 30/4"; t="Đề ôn tập Olympic 30/4"
        summary="Bài toán/đề ôn kèm file tải ở phần bình luận bài gốc."
    items.append(dict(id=pid,order=i,title=t,category=cat,competition=comp,year=year,free=True,summary=summary,date="",url=BASE+pid))
for j,(pid,t,s,d) in enumerate(paid):
    items.append(dict(id=pid,order=-10+j,title=t,category="Tuyển tập (trả phí)",competition=None,year=int(d[-4:]),free=False,summary=s,date=d,url=BASE+pid))
items.sort(key=lambda x:x["order"])
for x in items: x.pop("order")
json.dump({"updated":datetime.date.today().strftime("%d/%m/%Y"),"source":"https://www.facebook.com/physicstranslatevn","items":items},open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
print(len(items))
