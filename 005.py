import streamlit as st
from sklearn.linear_model import LinearRegression
import feedparser
import random

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
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["MV yêu thích ", "Dự đoán giờ đi ngủ", "Kiểm tra sức khỏe", "Lượng nước cần uống", "Kiểm tra số bước chân", "Gía vàng", "Đọc báo", "Giai tri"])
with tab1:
    st.header(f"Các bài hát của {selected_artist}")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)
with tab2:
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
with tab3:
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
with tab4:
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
with tab5:
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
with tab6:
    st.header("cập nhật giá vàng từ Vietnamnet")
    feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
    gold_news = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]
    if gold_news:
        for entry in gold_news[:5]: #hiển thị 5 bài báo gần nhất
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
with tab7:
    st.header("tin tức mới nhất")
    feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
    for entry in feed.entries[:5]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)
with tab8:
    tabA, tabB, tabC = st.tabs(["Game tung xúc sắc", "Game đoán số", "Kéo - Búa - Bao"])
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