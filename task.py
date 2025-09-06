# streamlit_project.py
import streamlit as st
import subprocess
import os
st.set_page_config(page_title="📋 Menu-Based Automation Suite", layout="wide")
st.title("📋 Menu-Based Automation Suite")

st.sidebar.title("📁 Features")
feature = st.sidebar.radio("Select a Feature", [
    "Send Email",
    "Send SMS",
    "Make Phone Call",
    "Post on Instagram",
    "Send WhatsApp Message (Python)",
    "Send WhatsApp Message (JS)",
    "Blog: Companies using Linux",
    "Explore GUI Commands in Linux",
    "Change Program Icon in Linux",
    "Ctrl+C & Ctrl+Z Process Control",
    "Git: Init, Add, Commit, Push",
    "Git: Branch & Merge",
    "Git: Fork, Clone, PR",
    "Take Photo with JavaScript",
    "More Linux Terminals & GUIs",
    "University Finder",
    "Company Autobiography Generator",
    "Send Email via Mailtrap",
    "Draw Image with PIL",
    "List vs Tuple (Mutability Demo)",
    "Google Search (via Python)",
    "Face Swap with OpenCV",
    "Download Website (Offline Viewer)",
    "Mini Search Engine (External HTML + JS)",
    "Drag and Drop Box",
    "RAM Analysis with LiME"

])

if feature == "Send Email":
    st.subheader("📧 Send Email")
    st.code('''
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Hello from Python!")
msg['Subject'] = 'Test Email'
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'receiver_email@gmail.com'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('your_email@gmail.com', 'your_password')
    smtp.send_message(msg)
''', language='python')

elif feature == "Send SMS":
    st.subheader("📱 Send SMS")
    st.code("""
# Use Twilio or Fast2SMS API
# Example using Twilio
from twilio.rest import Client
client = Client('ACCOUNT_SID', 'AUTH_TOKEN')
message = client.messages.create(
    body='Hello from Python!',
    from_='+1234567890',
    to='+918888888888')
print(message.sid)
""", language='python')

elif feature == "Make Phone Call":
    st.subheader("📞 Make Phone Call")
    st.code("""
# Using Twilio again
call = client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',
    to='+918888888888',
    from_='+1234567890')
print(call.sid)
""", language='python')

elif feature == "Post on Instagram":
    st.subheader("📸 Post on Instagram")
    st.code("""
# Use instabot
from instabot import Bot
bot = Bot()
bot.login(username='your_username', password='your_password')
bot.upload_photo('photo.jpg', caption='Posted using Python!')
""", language='python')

elif feature == "Send WhatsApp Message (Python)":
    st.subheader("💬 Send WhatsApp using Python")
    st.code("""
import pywhatkit
pywhatkit.sendwhatmsg('+918888888888', 'Hello via Python!', 22, 30)
""", language='python')

elif feature == "Send WhatsApp Message (JS)":
    st.subheader("💬 Send WhatsApp using JavaScript")
    st.code("""
function sendWhatsApp() {
  var phone = "+918888888888";
  var message = "Hello from JavaScript!";
  window.open(`https://wa.me/${phone}?text=${encodeURIComponent(message)}`);
}
""", language='javascript')

elif feature == "Blog: Companies using Linux":
    st.subheader("🏢 Why Companies Use Linux")
    st.markdown('''
### Benefits:
- **Cost Efficiency**: Open source, no licensing fee
- **Security**: Highly secure and customizable
- **Performance**: Runs well on limited hardware

### Companies:
- **Google** – Custom Linux servers
- **Amazon** – AWS backend uses Linux
- **Facebook** – Operates data centers with Linux
''')

elif feature == "Explore GUI Commands in Linux":
    st.subheader("🖥 GUI Programs and Terminal Commands")
    st.markdown("""
- **Nautilus** → File manager → `nautilus`
- **Gedit** → Text editor → `gedit`
- **Terminal** → GNOME terminal → `gnome-terminal`
- **Calculator** → `gnome-calculator`
- **System Monitor** → `gnome-system-monitor`

### Enhance GUI:
- Install new interfaces: `sudo apt install kde-plasma-desktop`
- Use Tiling: `i3`, `awesomewm`
""")

elif feature == "Change Program Icon in Linux":
    st.subheader("🎨 Change Program Icon")
    st.markdown("""
Steps:
1. Go to `/usr/share/applications/`
2. Edit the `.desktop` file
3. Modify the `Icon=` path to your custom `.png`
""")

elif feature == "Ctrl+C & Ctrl+Z Process Control":
    st.subheader("⌨ Ctrl+C and Ctrl+Z Commands")
    st.markdown("""
- `Ctrl+C` sends SIGINT (Interrupt)
- `Ctrl+Z` sends SIGTSTP (Stop)

Check using:
```bash
kill -l
```

Handle in Python:
```python
import signal
import sys

def handler(sig, frame):
    print("Interrupted")
    sys.exit(0)

signal.signal(signal.SIGINT, handler)
```
""")

elif feature == "Git: Init, Add, Commit, Push":
    st.subheader("🌿 Git Init and Push")
    st.code("""
mkdir myproject
cd myproject
git init
echo "# My Project" > README.md
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/user/repo.git
git push -u origin main
""", language='bash')

elif feature == "Git: Branch & Merge":
    st.subheader("🌱 Git Branch & Merge")
    st.code("""
git checkout -b feature1
echo "new feature" >> file.txt
git add .
git commit -m "Add feature1"
git checkout main
git merge feature1
""", language='bash')

elif feature == "Git: Fork, Clone, PR":
    st.subheader("🔀 Git Fork and PR")
    st.markdown("""
1. Fork a repo on GitHub
2. Clone it locally:
```bash
git clone https://github.com/yourname/forked-repo.git
```
3. Make changes and push:
```bash
git add .
git commit -m "Improved docs"
git push origin main
```
4. Create a pull request from GitHub UI
""")

elif feature == "Take Photo with JavaScript":
    st.subheader("📸 Take Photo Using JS")
    st.code("""
navigator.mediaDevices.getUserMedia({ video: true })
  .then(function(stream) {
    document.getElementById('video').srcObject = stream;
  });

function capture() {
  const canvas = document.createElement('canvas');
  const video = document.getElementById('video');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext('2d').drawImage(video, 0, 0);
  document.body.appendChild(canvas);
}
""", language='javascript')

elif feature == "More Linux Terminals & GUIs":
    st.subheader("🧩 Enhance Terminal & GUI Experience")
    st.markdown("""
- **Install extra terminals:**
```bash
sudo apt install terminator
sudo apt install tilix
```

- **Use multiple terminal windows:**
```bash
tmux
```

- **Add GUI environments:**
```bash
sudo apt install kde-standard
sudo apt install xfce4
```

- **Explore GUI launchers:**
```bash
rofi
dmenu
""")
elif feature == "University Finder":
    st.subheader("🎓 University Finder")
    st.write("Explore universities and colleges with full info, including cost, placement, and dorms.")

    import pyttsx3
    import speech_recognition as sr

    # Initialize TTS engine
    engine = pyttsx3.init()

    def speak_text(text):
        engine.say(text)
        engine.runAndWait()

    def recognize_speech():
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            st.info("🎤 Listening... Please say the university name.")
            audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            st.success(f"✅ You said: {query}")
            return query
        except sr.UnknownValueError:
            st.error("Could not understand your voice.")
        except sr.RequestError:
            st.error("Speech recognition service error.")
        return None

    # University data
    universities = [
        {
            "name": "Harvard University",
            "country": "USA",
            "location": "Cambridge, Massachusetts",
            "tuition": "$50,000/year",
            "courses": ["Computer Science", "Economics", "Law", "Business"],
            "placement_rate": "92%",
            "departments": ["Engineering", "Law", "Medicine", "Business"],
            "management": "Private",
            "dorm": "On-campus housing available",
            "website": "https://www.harvard.edu"
        },
        {
            "name": "University of Oxford",
            "country": "UK",
            "location": "Oxford, England",
            "tuition": "£38,000/year",
            "courses": ["Philosophy", "Computer Science", "History"],
            "placement_rate": "89%",
            "departments": ["Humanities", "Sciences", "Law"],
            "management": "Public",
            "dorm": "Collegiate housing",
            "website": "https://www.ox.ac.uk"
        },
        {
            "name": "University of Tokyo",
            "country": "Japan",
            "location": "Tokyo, Japan",
            "tuition": "¥535,800/year",
            "courses": ["Engineering", "Physics", "Biology"],
            "placement_rate": "85%",
            "departments": ["Science", "Engineering", "Law"],
            "management": "Public",
            "dorm": "Limited on-campus dormitories",
            "website": "https://www.u-tokyo.ac.jp"
        },
        {
            "name": "Vivekananda Global University (VGU)",
            "country": "India",
            "location": "Jagatpura, Jaipur, Rajasthan",
            "tuition": "₹120,000/year",
            "courses": ["Engineering", "Management", "Law", "Design"],
            "placement_rate": "75%",
            "departments": ["Engineering", "Law", "Design", "Agriculture"],
            "management": "Private",
            "dorm": "On-campus hostels with mess, Wi-Fi, gym, and laundry",
            "website": "https://vgu.ac.in/"
        },
        {
            "name": "JECRC University",
            "country": "India",
            "location": "Sitapura, Jaipur, Rajasthan",
            "tuition": "₹110,000/year",
            "courses": ["Computer Science", "Biotech", "Civil", "MBA"],
            "placement_rate": "80%",
            "departments": ["Engineering", "Sciences", "Business"],
            "management": "Private",
            "dorm": "Hostels with AC/Non-AC rooms, mess, 24x7 security",
            "website": "https://jecrcuniversity.edu.in/"
        },
        {
            "name": "Swami Keshvanand Institute of Technology (SKIT)",
            "country": "India",
            "location": "Ramnagaria, Jagatpura, Jaipur",
            "tuition": "₹100,000/year",
            "courses": ["Mechanical Engineering", "Electronics", "CSE", "MBA"],
            "placement_rate": "78%",
            "departments": ["Engineering", "Business", "Applied Sciences"],
            "management": "Private",
            "dorm": "Separate hostels for boys and girls with Wi-Fi, mess, gym",
            "website": "https://www.skit.ac.in/"
        }
    ]

    # Sidebar filters
    st.sidebar.header("🔍 Filter Options")
    selected_country = st.sidebar.selectbox("Select Country", ["All"] + list(set([u["country"] for u in universities])))
    selected_department = st.sidebar.selectbox("Select Department", ["All"] + sorted(set(d for u in universities for d in u["departments"])))
    search_name = st.sidebar.text_input("Search by University Name")

    if st.sidebar.button("🎙️ Use Voice Search"):
        voice_result = recognize_speech()
        if voice_result:
            search_name = voice_result

    # Apply filters
    filtered_universities = universities
    if selected_country != "All":
        filtered_universities = [u for u in filtered_universities if u["country"] == selected_country]
    if selected_department != "All":
        filtered_universities = [u for u in filtered_universities if selected_department in u["departments"]]
    if search_name:
        filtered_universities = [u for u in filtered_universities if search_name.lower() in u["name"].lower()]

    # Display results
    if not filtered_universities:
        st.warning("No universities found matching your criteria.")
    else:
        for uni in filtered_universities:
            with st.expander(f"{uni['name']}"):
                st.markdown(f"**🌐 Website:** [Visit]({uni['website']})")
                st.markdown(f"**📍 Location:** {uni['location']}, {uni['country']}")
                st.markdown(f"**💰 Tuition Fees:** {uni['tuition']}")
                st.markdown(f"**🏛️ Management Type:** {uni['management']}")
                st.markdown(f"**🏢 Departments:** {', '.join(uni['departments'])}")
                st.markdown(f"**📚 Courses Offered:** {', '.join(uni['courses'])}")
                st.markdown(f"**💼 Placement Rate:** {uni['placement_rate']}")
                st.markdown(f"**🛏️ Hostel/Dorm Info:** {uni['dorm']}")
                if st.button(f"🔊 Speak Details - {uni['name']}"):
                    message = (
                        f"{uni['name']} located in {uni['location']}, {uni['country']}. "
                        f"Tuition: {uni['tuition']}. Courses: {', '.join(uni['courses'])}. "
                        f"Departments: {', '.join(uni['departments'])}. Placement rate: {uni['placement_rate']}. "
                        f"Hostel info: {uni['dorm']}."
                    )
                    speak_text(message)

    st.markdown("---")
    st.caption("Built using Streamlit + pyttsx3 + SpeechRecognition | Demo dataset for global university exploration.")
elif feature == "Company Autobiography Generator":
    st.subheader("🏢 Company Autobiography Generator (External Link)")
    st.write("Generate company autobiography using our Hugging Face Space.")

    st.markdown("Click below to open the tool in a new tab:")
    st.markdown(
        """
        <a href="https://huggingface.co/spaces/Badrekamil/Company-autobiography" target="_blank">
            <button style='padding:10px 20px;font-size:16px;'>🚀 Launch Generator</button>
        </a>
        """,
        unsafe_allow_html=True
    )
elif feature == "Send Email via Mailtrap":
    st.subheader("📧 Send Email via Mailtrap (SMTP)")

    sender_email = st.text_input("Sender Email", "sender@example.com")
    receiver_email = st.text_input("Receiver Email", "receiver@example.com")
    subject = st.text_input("Email Subject", "Mailtrap Sandbox Test Email")
    body = st.text_area("Email Body", "This is a test email sent from Mailtrap Sandbox. ✅")

    st.markdown("#### 📬 SMTP Settings (Mailtrap Sandbox)")
    smtp_server = st.text_input("SMTP Server", "sandbox.smtp.mailtrap.io")
    smtp_port = st.number_input("SMTP Port", value=587)
    username = st.text_input("Username", "543bcd25f37184")
    password = st.text_input("Password", "b366f918ed02a9", type="password")

    if st.button("📨 Send Email"):
        try:
            import smtplib
            from email.mime.text import MIMEText

            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = receiver_email

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(username, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())

            st.success("✅ Email sent successfully via Mailtrap!")
        except Exception as e:
            st.error(f"❌ Error: {e}")
elif feature == "Draw Image with PIL":
    st.subheader("🖼️ Create an Image with PIL")

    st.markdown("This tool draws a **red rectangle** and a **blue circle** on a white canvas (300x300 px).")

    if st.button("🎨 Generate Image"):
        from PIL import Image, ImageDraw

        # Create image
        image = Image.new("RGB", (300, 300), "white")
        draw = ImageDraw.Draw(image)

        # Draw shapes
        draw.rectangle([50, 50, 250, 250], fill="red")
        draw.ellipse([100, 100, 200, 200], fill="blue")

        # Save temporarily
        image_path = "my_digital_image.png"
        image.save(image_path)

        st.image(image_path, caption="Generated Image", use_column_width=False)
        st.success("✅ Image created and displayed!")
elif feature == "List vs Tuple (Mutability Demo)":
    st.subheader("🔄 List vs Tuple (Mutability Demo)")

    st.markdown("""
    ### 🧠 Concept:
    - **List**: Mutable – You can change, add, or remove items.
    - **Tuple**: Immutable – You cannot change items once defined.
    """)

    st.markdown("#### ✅ List Example:")
    my_list = [1, 2, 3]
    my_list.append(4)
    st.code("""
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
    """, language='python')
    st.write("Output:", my_list)

    st.markdown("#### ❌ Tuple Example:")
    st.code("""
my_tuple = (1, 2, 3)
my_tuple[0] = 5  # Error: 'tuple' object does not support item assignment
    """, language='python')

    try:
        my_tuple = (1, 2, 3)
        my_tuple[0] = 5  # This will raise an error
    except TypeError as e:
        st.error(f"Error: {e}")
elif feature == "Google Search (via Python)":
    st.subheader("🔎 Google Search (Python-based)")

    st.markdown("Search Google results using the `googlesearch` library. (Note: May not work on all networks.)")

    query = st.text_input("🔍 Enter search query", "Python programming tutorials")

    if st.button("Search"):
        try:
            from googlesearch import search  # Requires: pip install googlesearch-python

            st.info(f"Showing top 10 results for: **{query}**")

            results = list(search(query, num_results=10))
            for i, url in enumerate(results, 1):
                st.markdown(f"**{i}.** [{url}]({url})")

        except Exception as e:
            st.error(f"❌ Error occurred: {e}")
elif feature == "Face Swap with OpenCV":
    st.subheader("🧑‍🤝‍🧑 Seamless Face Swap using OpenCV")

    st.markdown("Upload two images with **clear faces** for seamless cloning using OpenCV.")

    uploaded_img1 = st.file_uploader("📤 Upload First Face Image", type=["jpg", "jpeg", "png", "webp"], key="img1")
    uploaded_img2 = st.file_uploader("📤 Upload Second Face Image", type=["jpg", "jpeg", "png", "webp"], key="img2")

    if uploaded_img1 and uploaded_img2:
        import cv2
        import numpy as np
        from PIL import Image

        file_bytes1 = np.asarray(bytearray(uploaded_img1.read()), dtype=np.uint8)
        file_bytes2 = np.asarray(bytearray(uploaded_img2.read()), dtype=np.uint8)

        img1 = cv2.imdecode(file_bytes1, cv2.IMREAD_COLOR)
        img2 = cv2.imdecode(file_bytes2, cv2.IMREAD_COLOR)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        faces1 = face_cascade.detectMultiScale(img1, 1.1, 5)
        faces2 = face_cascade.detectMultiScale(img2, 1.1, 5)

        if len(faces1) == 0 or len(faces2) == 0:
            st.error("❌ Could not detect faces in one or both images. Please upload different images.")
        else:
            x1, y1, w1, h1 = faces1[0]
            x2, y2, w2, h2 = faces2[0]

            face_img1 = img1[y1:y1+h1, x1:x1+w1]
            face_img2 = img2[y2:y2+h2, x2:x2+w2]

            face_img1_resized = cv2.resize(face_img1, (w2, h2))
            mask = 255 * np.ones(face_img1_resized.shape, face_img1_resized.dtype)
            center = (x2 + w2//2, y2 + h2//2)

            output = cv2.seamlessClone(face_img1_resized, img2, mask, center, cv2.NORMAL_CLONE)

            st.markdown("### ✅ Output: Swapped Face Image")
            st.image(cv2.cvtColor(output, cv2.COLOR_BGR2RGB), channels="RGB", use_column_width=True)
elif feature == "Download Website (Offline Viewer)":
    st.subheader("🌐 Download Website for Offline Viewing")

    st.markdown("This tool recursively downloads all internal HTML pages from a website.")

    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin, urlparse
    import os

    visited = set()

    def download_page(url, base_url, folder='downloaded_site'):
        if url in visited:
            return
        visited.add(url)

        try:
            response = requests.get(url)
            if response.status_code != 200:
                st.warning(f"⚠️ Skipped (status {response.status_code}): {url}")
                return
        except Exception as e:
            st.error(f"❌ Failed to download {url}: {e}")
            return

        os.makedirs(folder, exist_ok=True)

        path = urlparse(url).path.strip('/')
        if not path or path.endswith('/'):
            path += 'index.html'
        filename = os.path.join(folder, path.replace('/', '_'))

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        st.success(f"✅ Downloaded: {url}")

        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(base_url, href)
            if urlparse(full_url).netloc == urlparse(base_url).netloc:
                download_page(full_url, base_url, folder)

    website_url = st.text_input("🔗 Enter Website URL", "https://www.hash13.com/")
    folder_name = st.text_input("📁 Folder to Save", "downloaded_site")

    if st.button("⬇️ Start Download"):
        visited.clear()
        download_page(website_url.strip(), website_url.strip(), folder=folder_name.strip())
        st.success("🎉 Download complete! Check your local folder.")
elif feature == "Mini Search Engine (External HTML + JS)":
    st.subheader("🔍 Mini Search Engine (External App)")

    st.markdown("""
This is a custom Node.js + HTML powered Google search mini engine.

✅ Features:
- Uses SerpAPI to search Google  
- Clean HTML/JS interface  
- Runs on `http://localhost:3000`

⚙️ Make sure your `server.js` and `index.html` are in the `search_engine` folder.
""")

    if st.button("🚀 Launch Mini Search Engine"):
        import subprocess
        import webbrowser
        import os

        # Path to server.js
        server_path = os.path.join("search_engine", "server.js")

        # Start server in background
        try:
            subprocess.Popen(["node", server_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            st.success("✅ Server started successfully!")
        except Exception as e:
            st.error(f"❌ Failed to start server.js: {e}")

        # Open the web app in browser
        try:
            webbrowser.open("http://localhost:3000")
        except Exception as e:
            st.warning("Server started, but could not open browser.")
elif feature == "Drag and Drop Box":
    st.subheader("📦 Drag and Drop Box")

    # Render it visually
    import streamlit.components.v1 as components

    drag_and_drop_code = """
    <div id="dragDiv" style="width: 150px; height: 150px; background-color: lightcoral; position: absolute; top: 100px; left: 100px; cursor: grab; border-radius: 8px;">
      Drag me!
    </div>

    <script>
      const dragDiv = document.getElementById("dragDiv");

      let isDragging = false;
      let offsetX = 0, offsetY = 0;

      dragDiv.addEventListener("mousedown", function(e) {
        isDragging = true;
        offsetX = e.clientX - dragDiv.offsetLeft;
        offsetY = e.clientY - dragDiv.offsetTop;
        dragDiv.style.cursor = "grabbing";
      });

      document.addEventListener("mousemove", function(e) {
        if (isDragging) {
          dragDiv.style.left = (e.clientX - offsetX) + "px";
          dragDiv.style.top = (e.clientY - offsetY) + "px";
        }
      });

      document.addEventListener("mouseup", function() {
        isDragging = false;
        dragDiv.style.cursor = "grab";
      });
    </script>
    """

    components.html(drag_and_drop_code, height=500)
elif feature == "RAM Analysis with LiME":
    st.title("🧠 RAM Analysis using LiME")
    st.markdown("""
    Ever wondered what's really sitting inside your RAM right now?

    With **LiME (Linux Memory Extractor)**, you can:

    - 🗂 Dump the entire RAM in raw format  
    - 🐍 Extract live program variables (like Python strings)  
    - 🔍 See sensitive data exactly as it existed in memory  
    - 🔐 Prove how even “secure” inputs land in RAM before encryption

    This tool is for awareness and learning. It helps in:

    ✅ Better troubleshooting  
    ✅ Real security testing  
    ✅ Deep performance insights  
    """)

    # Removed the image display here

    # Display example command
    st.code("""
# Example: Using grep to find live Python variable in RAM dump
strings /root/mymem.data | grep 'hellopp'
# Output might show:
# =?hellopp
# hellopp
    """, language="bash")

    st.success("💡 Drives tell you history. RAM tells you the present.")
    st.warning("⚠️ This is a forensic-level tool. Use with proper permission and caution.")
