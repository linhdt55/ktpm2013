Nhóm 7:
	Đặng Tiến Linh
	Đồng Xuân Khánh
	Đinh Quang Sơn
 	Trịnh Đình Thanh

Cách chạy chương trình:
	1.Để test quá trình đăng nhập đến thư mục chứa các file trong bài, mở cmd và gõ: "pybot login.txt" , sau khi test login thành công gõ: "pybot login_error.txt" để test quá trình đăng nhập lỗi.
	2.Test quá trình thêm sinh viên gõ: pybot add_student.txt
	3.Test quá trình xóa sinh viên gõ: pybot delete_student.txt

Những lỗi phát hiện ra nhưng không viết được test là:
	1. Nếu ta thêm cùng một sinh viên 2 lần thì sẽ báo sinh viên đó đã tồn tại nhưng nhóm chưa test được.
	2. Khi điền các trường trong khi muốn thêm sinh viên mà các trường đó không đúng theo định dạng, ví dụ như: ngày tháng năm sinh thì lại nhập là 1 string chẳng han thì sẽ có lỗi xảy ra nhưng nhóm chưa test được.
	3. Trong web thì mỗi sinh viên có một id ở trong mã nguồn khác nhau chính vì vậy mà muốn xóa từng sinh viên ta lại phải thay đổi id theo từng sinh viên có trong danh sách lớp. Không tự động xóa theo ý muốn lựa chọn được.

Các chức năng đã test là 3 chức năng:
	1. Chức năng đăng nhập.
	2. Chức năng thêm 1 sinh viên.
	3. Chức năng xóa 1 sinh viên.

Số lượng test đã viết là 4 test 3 test pased, 1 test failed.

Những khó khăn khi làm:
	+ Đầu tiên là cài thư viện selenium, nhóm thấy khá khó khăn khư cài thư viện này, phải mất khá nhiều thời gian để cài được.
	+ Tài liệu robotframework đọc khá dài và lý thuyết nhiều, nhóm đã đọc và cũng phải hỏi han các bạn khác ngoài nhóm mới nắm được cơ chế để làm bài.

Những góp ý cho hệ thống:
	+ Nên đưa ngay video hướng dẫn thay cho "một số ảnh màn hình", em nhận "một số ảnh màn hình" này không mấy quan trọng, người dùng thường thích xem ngay cách sử dụng và hướng dẫn hơn. Và trong video cũng có ảnh màn hình rồi. "Một số ảnh màn hình" là không cần thiết mà nó lại chiếm quá nhiều không gian.
	+ Em cũng nghĩ không nên để nhiều màu cho các chữ "Đăng Nhập, DÙng Thử, Thông Sản Phẩm...." nên dùng một màu và thêm nữa nhưng ưu điểm nổi bật của hệ thống được liệt kê nên được làm rõ ràng hơn. Và những lời giải thích thêm ở dưới những từ chỉ chức năng hay ưu điểm của sản phẩm cũng nên được căn lề gọn gàng hơn.
	+ Phần liên hệ qua mạng xã hội nên có thêm facebook.
THANGK YOU FOR DOING.