import speech_recognition as sr

# Khởi tạo recognizer với engine là PocketSphinx
recognizer = sr.Recognizer()

# Sử dụng microphone là nguồn âm thanh
with sr.Microphone() as source:
    print("Hãy nói gì đó:")
    try:
        # Lắng nghe và nhận dạng giọng nói với PocketSphinx
        audio = recognizer.listen(source)
        text = recognizer.recognize_sphinx(audio, language="vi-VN")
        print("Bạn đã nói: " + text)
    except sr.UnknownValueError:
        print("Không thể nhận diện giọng nói.")
    except sr.RequestError as e:
        print("Không thể kết nối tới dịch vụ nhận diện giọng nói; {0}".format(e))
