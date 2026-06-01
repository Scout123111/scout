import streamlit as st
from sklearn.linear_model import LinearRegression
import feedparser
import random
import time

st.sidebar.title("danh sánh nghệ sĩ")
selected_artist = st.sidebar.radio("Chọn nghệ sĩ:", ["Đen Vâu", "Hà Anh Tuấn", "Sơn Tùng M-TP", "Những bản nhạc giúp tâm trạng vui vẻ hơn"])

videos = {
    "Đen Vâu": [
        ("Nấu ăn cho em", "https://www.youtube.com/watch?v=ukHK1GVyr0I"),
        ("Mang tiền về cho mẹ", "https://www.youtube.com/watch?v=UVbv-PJXm14"),
        ("Trời hôm nay nhiều mây cực!", "https://www.youtube.com/watch?v=MBaF0l-PcRY"),
        ("Hai triệu năm", "https://www.youtube.com/watch?v=LSMDNL4n0kM")        
    ],
    "Hà Anh Tuấn": [
        ("Tuyết rơi mùa hè", "https://www.youtube.com/watch?v=pTh3KCD7Euc"),
        ("Nước ngoài", "https://www.youtube.com/watch?v=pU3O9Lnp-Z0"),
        ("Tháng tư là lời nói dối của em", "https://www.youtube.com/watch?v=UCXao7aTDQM"),
        ("Xuân thì", "https://www.youtube.com/watch?v=3s1r_g_jXNs")
    ],
    "Sơn Tùng M-TP": [
        ("Lạc trôi", "https://www.youtube.com/watch?v=Llw9Q6akRo4"),
        ("Chúng ta không thuộc về nhau", "https://www.youtube.com/watch?v=qGRU3sRbaYw"),
        ("Muộn rồi mà sao còn", "https://www.youtube.com/watch?v=xypzmu5mMPY"),
        ("Hãy trao cho anh", "https://www.youtube.com/watch?v=knW7-x7Y7RE")
    ],
    "Những bản nhạc giúp tâm trạng vui vẻ hơn":[
        ("Những bản nhạc giúp tâm trạng vui vẻ hơn", "https://www.youtube.com/watch?v=SlsH6PbDJZk&t=898s"),
        ("Lỡ Duyên", "https://www.youtube.com/watch?v=fq_H4A3HgD4&list=RDfq_H4A3HgD4&start_radio=1&rv=fq_H4A3HgD4"),
        ("Bài hat về tình yêu quê hương đất nước", "https://www.youtube.com/watch?v=GOMGeUetqlI&list=RDSlsH6PbDJZk&index=3"),
        ("Đi giữa trời rực rỡ", "https://www.youtube.com/watch?v=D1Uf9vREh6Q&list=RDSlsH6PbDJZk&index=3"),
        ("STAY HOME, STAY HAPPY, STAY HÀANHTUẤN", "https://www.youtube.com/watch?v=MMgPOQ9gJhM&list=RDEMrx5Xy48sg-WCr9qiaw1hhg&index=2"),
        ("Focus Time", "https://www.youtube.com/watch?v=Lcmlq9utGYk")
    ]    
}
st.title(" ứng dụng giải trí và sức khỏe")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["MV yêu thích " ,"Kiểm tra sức khỏe" ,"Đọc báo" , "Giai tri", "Kiểm tra tính cách theo DISC", "Ứng dụng theo dõi sức khỏe nâng cao"])
with tab1:
    st.header(f"Các bài hát của {selected_artist}")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)
with tab2:
    tabA, tabB, tabC, tabD = st.tabs(
     ["Dự đoán giờ đi ngủ mỗi đêm ",
      "📊 Kiểm tra chỉ số BMI của bạn",
      "Kiểm tra lượng nước cần uống ",
      "Kiểm tra số bước đi phù hợp mỗi ngày"])
    with tabA:
        st.header("Dự đoán giờ đi ngủ mỗi đêm ")
        #Tuổi, mức độ hoạt động thể chất, thời gian dùng máy tính
        x = [
            [10, 1, 8],
            [20, 5, 6],
            [25, 8, 3],
            [30, 6, 5],
            [35, 2, 9],
            [40, 4, 3],
        ]
        y = [10, 8, 6, 7, 9.5, 9]
        model = LinearRegression()
        model.fit(x, y)
        st.write("Nhập thông tin cá nhân: ")
        age = st.number_input("Tuổi của bạn", min_value=5, max_value=100, value=5)
        activity = st.slider("Mức độ hoạt động thể chất (1 = ít, 10 = rất nhiều)", 1, 10, 5)
        screen_time = st.number_input("Thời gian dùng màn hình trong 1 ngày (giờ)", min_value=0, max_value=24, value=6)
        if st.button("Dự đoán ngay"):
            input_data = [[age, activity, screen_time]]
            result = model.predict(input_data)[0]
            st.success(f"Bạn nên ngủ khoảng {result: .1f} giờ mỗi đêm")

            if result < 6.5:
                st.warning("có thể bạn cần nghỉ ngơi nhiều hơn để cái thiện sức khỏe. ")
            elif result > 9:
                st.info("có thể bạn đang vận động nhiều, bạn cần ngủ bù hợp lý nhé")
            else:
                st.success("Lượng ngủ lý tưởng, hãy giữ thói quan tốt ")
    with tabB:
        st.header("📊 Kiểm tra chỉ số BMI của bạn")

        can_nang = st.number_input("Nhập cân nặng của bạn (kg)", min_value=10.0, max_value=200.0, value=60.0, step=0.1)
        chieu_cao = st.number_input("Nhập chiều cao của bạn (m)", min_value=1.0, max_value=2.5, value=1.7, step=0.01)

        if st.button("📏 Tính BMI"):
            bmi = can_nang / (chieu_cao ** 2)
            st.success(f"Chỉ số BMI của bạn là: {bmi:.2f}")

            # Ngưỡng BMI
            bmi_min = 18.5
            bmi_max = 24.9

            # Cân nặng tương ứng
            can_nang_min = bmi_min * (chieu_cao ** 2)
            can_nang_max = bmi_max * (chieu_cao ** 2)

            if bmi < 18.5:
                st.warning("Bạn đang thiếu cân, nên ăn uống đầy đủ và dinh dưỡng hơn.")
                can_tang = can_nang_min - can_nang
                st.info(f"👉 Bạn cần **tăng ít nhất {can_tang:.2f} kg** để đạt mức cân nặng tối thiểu bình thường.")

            elif 18.5 <= bmi < 25:
                st.info("Bạn có cân nặng bình thường. Hãy tiếp tục duy trì lối sống lành mạnh.")
                st.success("👍 Bạn không cần tăng hoặc giảm cân.")

            elif 25 <= bmi < 30:
                st.warning("Bạn đang thừa cân. Nên cân đối chế độ ăn và tập thể dục.")
                can_giam = can_nang - can_nang_max
                st.info(f"👉 Bạn cần **giảm ít nhất {can_giam:.2f} kg** để quay về mức bình thường.")

            else:
                st.error("Bạn đang béo phì. Nên gặp chuyên gia dinh dưỡng hoặc bác sĩ để được tư vấn.")
                can_giam = can_nang - can_nang_max
                st.info(f"👉 Bạn cần **giảm ít nhất {can_giam:.2f} kg** để về ngưỡng cân nặng bình thường.")
    with tabC:
        age = st.number_input("Nhập tuổi của bạn: ", min_value=1, max_value=100, value=18, step=1)
        if st.button("Kiểm tra lượng nước cần uống "):
            if age < 4:
                st.info("Khuyến nghị: 1.3 lít/ngày ")
            elif 4 <= age <= 8:
                st.info("Khuyến nghị: 1.7 lít/ngày ")
            elif 9 <= age <= 13:
                st.info("Khuyến nghị: 2.1 đến 2.4 lít/ngày ")
            elif 14 <= age <= 18:
                st.info("Khuyến nghị: 2.3 đến 3.3 lít/ngày ")
            elif 19 <= age <= 50:
                st.info("Khuyến nghị: 2.7 lít/ngày đối với nữ, 3.7 lít/ ngày đối với nam ")
            elif age > 50:
                st.info("khuyến nghị: khoảng 2.5lit/ngay đến 3 lít/ngày (phụ thuộc vào sức khỏe và mức độ vận động")
            else:
                st.warning("Vui lòng nhập độ tuổi hợp lệ")
    with tabD:
        st.header("Kiểm tra số bước đi phù hợp mỗi ngày ")
        age2 = st.number_input("Nhập tuổi của bạn: ", min_value=0.0, max_value=130.0, value=18.0, step=1.0)
        if st.button("Kiểm tra số bước "):
            st.success(f"tuổi của bạn: {age2: .0f}")
            if age2 < 18:
                st.info("bạn nên đi 12000 - 15000 bước mỗi ngày ")
            elif 17 < age2 <=39:
                st.info("Bạn nên đi 8000 - 10000 bước mỗi ngày ")
            elif 39 < age2 <= 64:
                st.info("Bạn nên đi từ 7000 - 9000 bước mỗi ngày ")
            elif age2 > 64:
                st.info("bạn nên đi 6000 đến 8000 bước mỗi ngày ")
            else:
                st.error("có lỗi xảy ra . Vui lòng kiểm tra lại thông tin ")
with tab3:
    tabA, tabB = st.tabs(["cập nhật giá vàng từ Vietnamnet", "tin tức mới nhất"])
    with tabA:
        st.header("cập nhật giá vàng từ Vietnamnet")
        feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
        gold_news = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]
        if gold_news:
            for entry in gold_news[:5]: #hiển thị 5 bài báo gần nhất
                st.subheader(entry.title)
                st.write(entry.published)
                st.write(entry.link)
    with tabB:
        st.header("tin tức mới nhất")
        feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
        for entry in feed.entries[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
with tab4:
    tabA, tabB, tabC, tabD, tabE = st.tabs(["Game tung xúc sắc", "Game đoán số", "Kéo - Búa - Bao", "Game quay số may mắn", "Game quay số may mắn V2 "])
    with tabA:
        st.header("🤖Game tung xúc sắc")
        st.image("https://thumb.ac-illust.com/11/11208a7f39207d32b1cff1a66d22dd75_t.jpeg")
        st.write("Luật chơi")
        st.write("Bấm lắc xúc sắc để được một số ngẫu nhiên từ 1 đến 6 ")
        if st.button(" 🎲 Lắc xúc sắc"):
            roll = random.randint(1, 6)
            st.success(f"Bạn tung được số {roll} !!!!")
            if roll == 1:
                st.image(
                    "http://www.clker.com/cliparts/m/v/m/J/4/V/dice-1-md.png"
                )
            if roll == 2:
                st.image(
                "https://www.clker.com/cliparts/a/Y/E/o/z/t/dice-2-md.png"
            )
            if roll == 3:
                st.image(
                "https://www.clker.com/cliparts/O/I/r/9/W/x/dice-3-md.png"
            )
            if roll == 4:
                st.image(
                "https://www.clker.com/cliparts/r/z/d/a/L/V/dice-4-md.png"
            )
            if roll == 5:
                st.image(
                "https://www.clker.com/cliparts/U/N/J/F/T/x/dice-5-md.png"
            )
            if roll == 6:
                st.image(
                "https://www.clker.com/cliparts/l/6/4/3/K/H/dice-6-md.png"
            )
    with tabB:
        st.header("Game đoán số bí mật 1 - 100")
        st.image("https://m.media-amazon.com/images/I/71Agu95C-jL._AC_UF894,1000_QL80_.jpg")
        st.write("Luật chơi")
        st.write("Đoán số bất kì từ 1 đến 100, nhập số để biết được số chính xác lớn hơn hay nhỏ hơn số đã nhập, cố gắng đoán trong ít lần thử nhất có thể." \
        "bấm chơi lại sau khi đoán đúng để được chơi lại")
        if "secret" not in st.session_state:
            st.session_state.secret = random.randint(1, 100)
            st.session_state.tries = 0
        guess = st.number_input("Nhập số dự đoán 1 - 100", min_value=1, max_value=100, step=1)
        if st.button("Đoán !!!!"):
            st.session_state.tries += 1
            if guess < st.session_state.secret:
                st.warning("Lớn hơn")
                st.image("https://i.kym-cdn.com/editorials/icons/original/000/013/755/mon.jpg")
            elif guess > st.session_state.secret:
                st.warning("Nhỏ hơn")
                st.image("https://i.kym-cdn.com/editorials/icons/original/000/013/755/mon.jpg")
            else:
                st.success(f"Chính xác ! Bạn đoán đúng sau {st.session_state.tries} lần")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2pBfdCwgvKb7E8RBYkSluf3u3EdNxv54GuQ&s")
        if st.button("chơi lại"):
            st.session_state.secret = random.randint(1, 100)
            st.session_state.tries = 0
    with tabC:
        st.header("Kéo - Búa - Bao")
        st.image("https://static.tvtropes.org/trope_videos_transcoded/images/sd/q7uwxt.jpg")
        st.write("Luật chơi")
        st.write("Bạn bấm nút để ra một trong kéo, búa học bao. Hãy cố gắng thắng con bot nha !")
        st.write("kéo thắng bao")
        st.write("búa thắng kéo ")
        st.write("bao thắng búa")
        user = st.selectbox("Bạn chọn: ", ["Kéo", "Búa", "Bao"])
        bot = random.choice(["Kéo", "Búa", "Bao"])
        if st.button("Ra tay nào !!!!!"):
            st.write(f"Bot chọn: {bot}")
            if user == bot:
                st.warning("Hòa !!!!!")
                st.image("https://i1.sndcdn.com/artworks-ecyyzfetWzmHLDpo-X7ICfQ-t500x500.jpg")
            elif(user == "Kéo" and bot =="Bao" or (user == "Bao" and bot == "Búa") or (user == "Búa" and bot == "Kéo")):
                st.success("Bạn chiến thắng !!!!!")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1MBsQ9GnV0RNq9b_rJA63UN8m4e0Xq6HpGQ&s")
            else:
                st.error("Bạn Thua !!!!!")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGlF-k_0Gsm39dJSSZCSEJUF-UsSkm_SAkHg&s")
    with tabD:
        st.title("Game quay số may mắn ")
        #khởi tạo danh sách phần thưởng
        if "prizes" not in st.session_state:
            st.session_state.prizes = []

        #Nhập phần thưởng
        new_prize = st.text_input("Nhập phần thưởng")
        if st.button("➕ Thêm phần thưởng"):
            if new_prize:
                st.session_state.prizes.append(new_prize)

        #hiển thị danh sách
        st.write("Danh sách phần thưởng: ", st.session_state.prizes)
        #Quay số 
        if st.button ("🏆 Quay số"):
            if st.session_state.prizes:
                result = random.choice(st.session_state.prizes)
                st.success(f"Bạn quay trúng: {result}")
            
                #xóa phẩn thưởng
                st.session_state.prizes.remove(result)
            else:
                st.warning("Chưa có phần thưởng")
        # reset 
        if st.button(" Reset"):
            st.session_state.prizes = []
    with tabE:
        st.title("Game quay số may măn V2")
        #khởi tạo dữ liệu 
        if "new prizes" not in st.session_state:
            st.session_state.new_prizes = []
        if "weight" not in st.session_state:
            st.session_state.weights = []
        #Thêm phần thưởng
        st.subheader("Thêm phần thưởng")
        col1, col2 = st.columns(2)
        with col1:
            new_prizes = st.text_input("Tên phần thưởng")
        with col2:
            weight = st.number_input("Tỷ lệ trúng % ", 1, 100, 1)
        if st.button("Thêm phần thưởng"):
            if new_prize:
                st.session_state.new_prizes.append(new_prize)
                st.session_state.weights.append(weight)
                st.success(f"Đã thêm: {new_prize}")
        #danh sách phần thưởng
        st.subheader("Danh sách phần thưởng ")
        if st.session_state.new_prizes:
            for i, prizes in enumerate(st.session_state.new_prizes):
                st.write(
                    f"{i + 1}. {print} | tỷ lệ {st.session_state.weights[i]} %"
                )
        else:
            st.info("Chưa có phần thưởng")
        st.subheader("Quay số ")
        if st.button("Quay ngay "):
            if st.session_state.new_prizes:
                spin_placeholder = st.empty()

                for i in range(15):
                    spin_placeholder.markdown(
                        f'## Đang quay ....{random.choice(st.session_state.new_prize)}'
                    )
                    time.sleep(0.1)
                #chọn kết quả theo tỷ lệ
                result = random.choices(
                    st.session_state.new_prize,
                    weights = st.session_state.weights,
                    k = 1
                )[0]
                spin_placeholder.empty()
                st.balloons()
                st.success(f"Chúc mừng bạn đã trúng: **{result}**")
            else:
                st.warning("Chưa có phần thưởng ")
        #reset
        if st.button("Reset game "):
            st.session_state.new_prizes = []
            st.session_state.weights = []
            st.success("Đã reset ")
with tab5:
    st.header("Kiểm tra tính cách theo DISC, " \
    "D-Dominance (Thống trị), " \
    "I-Influence (Ảnh hưởng), " \
    "S-Steadiness (Ổn định), " \
    "C--Conscientiousness (Tận tâm / Chuẩn mực)")
    st.markdown("Chọn một mô tả đúng nhất và một mô tả ít đúng nhất trong từng nhóm")
    groups = [
        {
            "D": "Tôi quyết đoán với thích tính kiểm soát",
            "I": "Hướng ngoại, giao tiếp tốt và truyền cảm hứng, tôi thích thân thiện và nói chuyện dễ dàng",
            "S": "Tôi tích kiên nhẫn và đáng tin cậy",
            "C": "Tôi chính xác và hệ thống"
        },
        {
            "D": "Tôi thích thử thách và hành động nhanh",
            "I": "Tôi thích tràn đây năng lượng và lạc quan",
            "S": "Tôi thích ổn định và hỗ trợ người khác",
            "C": "Tôi thích làm việc theo quy tắc rõ ràng",
        },
        {
            "D": "Tôi thích kiểm soát kết quả",
            "I": "Tôi thích được sự công nhận",
            "S": "Tôi ưu tiên sự hài hước",
            "C": "Tôi chú ý đến việc chi tiết và phân thích"
        }
    ]
    scores = {"D": 0, "I": 0, "S": 0, "C": 0}
    for idx, group in enumerate(groups):
        st.markdown(f"### Nhóm {idx + 1}")
        options = list(group.values())
        keys = list(group.keys())
        most = st.radio("Mô tả đúng nhất với bạn ", options, key = f"most_{idx}")
        least = st.radio("Mô tả ít đúng nhất với bạn ", options, key = f"least_{idx}")
        for key , val in group.items():
            if val == most:
                scores[key] += 1
            if val == least:
                scores[key] -= 1
    if st.button("Xem kết quả DISC "):
        st.header("Kết quả của bạn ")
        max_type = max(scores, key = scores.get)

        for style, score in scores.items():
            st.write(f"{style}: {score} điểm")
        st.markdown(f" Tính cách nổi bật của bạn là: {max_type}**")
        description = {
            "D": "Quyết đoán, định hướng kết quả và thích kiểm soát",
            "I": "Giao tiếp tốt, tràn đầy năng lượng và truyền cảm hứng",
            "S": "Kiên nhẫn, đáng tin cậy và hỗ trợ người khác",
            "C": "Chính xác, tuân thủ quy trình và thích phân tích logic"
        }
        st.info(description[max_type])
        st.markdown("________")
        st.markdown("Mô tả chi tiết các nhóm DISC")
        st.markdown("""
            - **D (Dominance)**: Người lãnh đạo, chủ động, thích cạnh tranh. Ví dụ CEO, nhà sáng lập
            - **I (Influence)**: Người truyền cảm hứng, thích giao tiếp, có sức hút. ví dụ: người làm marketing, diễn giả
            - **S (steadiness)**: Người hỗ trợ, trung thành, kiên trì. Ví dụ: giáo viên, điều dưỡng
            - **C (Conscientionousness)**: Người phân tích, tỉ mỉ, theo quy trình. Ví dụ: Kế toán, kỹ sư.
        """)
        st.caption(" Đây chỉ là bài tham khảo về chỉ số DISC")  
with tab6:
    #st.set_page_config(page_title="ứng dụng sức khỏe nâng cao ", layout="centered")
    st.title("ứng dụng theo dõi sức khỏe nâng cao")
    st.header("Nhập thông tin cá nhân")
    name = st.text_input("Họ và tên ")
    age = st.number_input("Tuổi: ", min_value=0, max_value=120, step=1)
    gender = st.radio("Giới tính: ", ("Nam", "Nữ"))
    height = st.number_input("Chiều cao(cm): ", min_value=50.0, max_value=250.0, step=0.1)
    weight = st.number_input("Cân nặng (cm)  ", min_value=10.0, max_value=250.0, step=0.1)
    activity_level = st.selectbox("Mức độ hoạt động thể chất: ", [
        "ít vận động",
        "vận động nhẹ (1-3 buổi / tuần)",
        "vận động vừa (3 - 5 buổi / tuần)",
        "vận động nhiều (6 - 10 buổi / tuần)",
        "vận động rất nhiều (2 lần/ ngày)"
    ])
    if st.button("Phân tích sức khỏe "):
        if height > 0 and weight > 0:
            height_m = height/100
            bmi = weight / (height_m ** 2)
            if gender == "Nam":
                bmr = 10*weight + 6.25*height-5*age+5
            else:
                bmr = 10*weight + 6.25*height-5*age - 161
            activity_factor = {
                "ít vận động": 1.2,
                "vận động nhẹ (1-3 buổi / tuần)":1.375,
                "vận động vừa (3 - 5 buổi / tuần)":1.55,
                "vận động nhiều (6 - 10 buổi / tuần)":1.725,
                "vận động rất nhiều (2 lần/ ngày)":1.9
            }
            activity_factor = activity_factor[activity_level]
            tdee = bmr * activity_factor
            water_inlake = weight * 35/1000
            st.subheader("Kết quả phân tích")
            st.write(f"** Xin chào {name}!**")
            st.write(f"** Chỉ số BMI:** {bmi:.2f}'**")
            st.write(f"** BMR(tỷ lệ trao đổi chất cơ bản):** '{bmr:.0f}' kcal/ngày**")
            st.write(f"** tdee(Nặng lượng tiêu hao mỗi ngày):** '{tdee:.0f}' kcal/ngày**")
            st.write(f"** Lượng nước nên uống mỗi ngày :** '{water_inlake:.0f}' lít**")
            st.markdown("### Đánh giá chỉ số BMI: ")
            if bmi < 18.5:
                st.warning("Bạn đang thiếu cân. Bạn nên tăng dinh dưỡng. Bạn nên tăng {round((18.5 - bmi)*(height_m ** 2)),2)} kg")
            elif 18.5 <= bmi < 24.9:
                st.success("Bạn có cân nặng bình thường. Duy trì lối sống lành mạnh")  
            elif 25 <= bmi < 29.9:
                st.success(f"Bạn đang thừa cân. Hãy cân bằng lại chế độ ăn và hoạt động. Bạn nên giảm {round(((bmi - 24.9)*(height_m**2)),2)} kg")
            else:
                st.error(f"Bạn đang béo phì. Cần tham khảo chuyên gia để cải thiện sức khỏe. Bạn nên giảm {round(((bmi - 24.9)*(height_m * 2)), 2)} kg")
            st.markdown("Gợi ý chế độ ăn theo muc tiêu: ")
            col1,col2 = st.columns(2)
            with col1:
                st.info("Duy trì cân nặng")
                st.write(f" Ăn khoảng '{tdee:.0f}' kal/ngày")
            with col2:
                st.info("Giảm cân nhẹ: ")
                st.write(f" Ăn khoảng '{tdee-300: .0f}' kal/ngày")
            st.markdown("Gợi ý thực đơn mẫu : ")
            st.markdown("""
            -sáng : Trứng luộc, bánh mì nguyên cám, trái cây
            -trưa : Cơm gạo nứt, ức gà, rau luộc, canh
            -tối: salad rau xanh, cá hấp, trái cây ít ngọt
            -snack: Hạt khô, sữa chua ít đường
            """)
    st.header("Theo dõi sức khỏe về nhịp tim")
    sys = st.number_input("Huyết áp tâm thu(mmhg) :", min_value=50, max_value=250, step=1)
    dia = st.number_input("Huyết áp tâm trường(mmhg) :", min_value=30, max_value=150, step=1)
    heart_rate = st.number_input("Nhịp tim khi nghỉ ngơi(bpm): ",min_value=30, max_value=200, step=1) 
    if st.button("Phân tích nhịp tim"):
        st.header("Kết quả phân tích tim mạch") 
        if sys<90 or dia<60:
            st.warning("Huyết áp thấp")       
        elif 90<= sys <= 120 and 60<=dia<=80:
            st.success("Huyết áp bình thường") 
        elif 130<= sys <= 139 and 80<=dia<=89:  
            st.success("Tiền huyết áp ")
        elif 140<= sys <= 159 and 90<=dia<=99:  
            st.success("Tăng huyết áp độ 1")  
        elif 160<= sys <= 179 and 100<=dia<=109:  
            st.success("Tăng huyết áp độ 2")   
        else:
            st.error("Tăng huyết áp độ 3")   

        if heart_rate < 60:
            st.warning("Nhịp tim chậm")    
        elif 60 <= heart_rate<=100:
            st.success("Nhịp tim bình thường")  
        else:
            st.success("Nhịp tim cao")   
    #Lý thuyết nhịp tim theo độ tuổi
    st.markdown("Nhịp tim theo độ tuổi ")
    st.markdown("""
        - Công thức nhịp tim tối đa: 220 - tuổi  
        - Vùng tập luyện hiệu quả: *50% - 85% nhịp tim tối đa*
        
        | Tuổi | Tối đa (bpm) | 50-85% (bpm) |
        |------|--------------|--------------|
        | 20   | 200          | 100 - 170    |
        | 30   | 190          | 95 - 162     |
        | 40   | 180          | 90 - 153     |
        | 50   | 170          | 85 - 145     |
        | 60   | 160          | 80 - 136     |
        | 70   | 150          | 75 - 128     |
        """)
    st.header("Phát triển chiều cao")

    if age > 0:
        st.subheader("Phân tích tiềm năng phát triển chiều cao ")
        if gender == "Nam":
            max_growth_age = 21
        else:
            max_growth_age = 19
        if age >= max_growth_age:
            st.info(""" Ở tuổi hiện tại, khả năng tăng chiều cao tự nhiên gần như là không còn.  
                    Bạn nên luyện tập và bổ sung dinh dưỡng để giữ vóc dáng cân đối.
            """)
        else:
            remaining_years = max_growth_age - age
            st.write(f"Bạn vẫn còn khoảng {remaining_years} năm để phát triển chiều cao tối ưu")
            if activity_level == "ít vận động ":
                growth_potential = "Thấp"
                st.warning("Mức độ vận động thấp có thể làm hạn chế phát triển chiều cao. Hãy cố gắng vận động nhiều hơn mỗi ngày.")
            if activity_level == ["vận động nhẹ (1-3 buổi / tuần)", "vận động vừa (3 - 5 buổi / tuần)"]:
                growth_potential = "Trung bình"
                st.info("Mức độ vận động khá tốt, bạn nên bổ sung thêm các bài kéo dãn hoặc thể thao ngoài trời để tối ưu sự phát triển")
            else:
                growth_potential = "Cao"
                st.success("Rất tốt, mức độ vận động cao giúp kích thích hormone tăng trưởng, hỗ trợ phát triển chiều cao tối đa.")
            st.markdown(f"Tiền năng phát triển chiều cao của bạn: {growth_potential}")
            st.markdown("Gợi ý phát triển chiều cao tối đa ")
            with st.expander("Chế độ dinh dưỡng nên bổ sung "):
                st.markdown("""
                    -Protein : Thịt nạc, cá, trứng, đậu phụ
                    -Canxi: Sữa, phô mai, sữa chua, cá hồi, rau xanh đậm
                    -Vitamin D: phơi nắng 15 đến 20 phút hoặc ăn trứng, cá 
                    -Kẽm và Magie: có trong hải sản, các loại hạt, ngũ cốc nguyên hạt
                    -Tránh: Nước ngọt có gas, đồ ăn nhanh, đồ chiên rán nhiều mỡ
                """)
            with st.expander("Bài tập hỗ trợ phát triển chiều cao "):
                st.markdown("""
                    -Tập hàng ngày: Bơi lội, nhảy dây, bóng rổ, đu xà, yoga kéo dãn 
                    -Buổi sáng: Kéo dãn cơ thể, vươn vai, hít thở sâu ngoài trời
                    -Thói quen: Giữ lưng thẳng khi ngồi và đứng, tránh gù lưng
""")
            with st.expander("Thói quen sinh hoạt và giấc ngủ "):
                st.markdown("""
                    -Ngủ đủ 8 - 10 tiếng/ngày, đặc biệt ngủ tử 22h đến 6h sáng
                    -Hạn chế thức khuya, dùng điện thoại trước khi ngủ
                    -Uống đủ nước(theo khuyến nghị ở phần trên) 
                    -Duy trì cân nặng hợp lý để không ảnh hưởng đến hormone tăng trưởng       
""")
            if gender == "Nam":
                avg_height = 175
            else:
                avg_height = 162
            potential_height = height + remaining_years * 0.8
            if potential_height > avg_height:
                potential_height = avg_height + 2
            st.markdown(f"Chiều cao tiềm năng ước tính: {potential_height: .1f} cm")
    else:
        st.warning("Vui lòng nhập thông tin cá nhân ở phần đầu (tuổi, giới tính, chiều cao...) trước khi phân tích")








         
        



                


                


