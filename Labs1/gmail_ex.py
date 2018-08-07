# 20130075@studen.hust.edu.vn

from gmail import GMail
from gmail import Message

gmail = GMail(' <vu.ntav@gmail.com>','Anhvu2906')
msg = Message('Test Message',to=' <vu.ntav@gmail.com>',html= html_to_send)
gmail.send(msg)

reasons = ["om"]
html_content ="""
<p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa việt nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<h1 style="text-align: center;"><strong>Đơn Xin Nghỉ Việc</strong></h1>
<p>K&iacute;nh gửi : Gi&aacute;m đốc abc</p>
<p>H&ocirc;m nay e xin thay nghi hoc vi {{sickness}}  </p>
<p>e xin chan thanh cam on</p>
"""