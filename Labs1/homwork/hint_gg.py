from gmail import GMail , Message

from random import choice

from datetime import datetime

gmail = GMail('vu.ntav@gmail.com', 'Anhvu2906')


html_new ="""
<p style="text-align: center;">Cộng H&ograve;a X&atilde; Hội Chủ Nghĩa Việt Nam</p>
<p style="text-align: center;">Độc Lập - Tự do - Hạnh Ph&uacute;c</p>
<h2 style="text-align: center;">ĐƠN KIẾN NGHỊ</h2>
<p><strong>K&iacute;nh Gửi :</strong> Bố Huỳnh Tuấn Anh</p>
<p>Con T&ecirc;n l&agrave; : Nguyễn Thế Anh Vũ</p>
<p>Con l&agrave;m đơn n&agrave;y để đề nghị bố phải t&igrave;m ngay 1 {{sickness}} xinh đẹp vả đảm đang để lo cho cuộc sống của bố sau n&agrave;y.con xin hết !!!</p>
<p>&nbsp;</p>
<p style="padding-left: 60px; text-align: center;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Người L&agrave;m Đơn</p>
<p style="padding-left: 60px; text-align: center;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Anh Vũ</p>
"""

reasons = [
    "cô vợ"
    "cô bồ"
    "cô người yêu"
]

from datetime import datetime
now = datetime.now()

count = 0
while count < 1:
    if now.hour == 7:
        msg = Message("Đơn Kiến Nghị",to = '20130075@student.hust.edu.vn',html = html_new)
    count += 1
    break