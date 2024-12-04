Bước 1: Sinh map!
(LƯU Ý VÌ ĐÂY LÀ BƯỚC QUAN TRỌNG)
(LƯU Ý VÌ ĐÂY LÀ BƯỚC QUAN TRỌNG)
(LƯU Ý VÌ ĐÂY LÀ BƯỚC QUAN TRỌNG)

- Từ file create_circle, sửa đổi số trong range() ở dòng 11 rồi chạy file để tạo ra 1 map ngẫu nhiên với số lượng goal tùy chỉnh (10, 20, 30)
=> Map được lưu trong assets/circles.txt
- Tạo mới 1 file tsp với tên dựa vào case muốn test (ví dụ 1 robot, 50 goals, low budgets => map_1_50_lb.tsp)
- Copy lại mẫu bằng 1 map bất kì rồi dán vào file vừa tạo. Bắt đầu bước sửa dữ liệu!!!

. Sửa dòng 5 thành ROBOT : {số robot của case}
. Sau dòng ROBOT_BUDGET_SECTION, điền thông tin budget của các con robot. Lưu ý ở trước budget còn có số thứ tự, budget của các con robot bằng nhau và tổng bằng 2400 trong trường hợp low budget và 10000000000 trong trường hợp high budgets
. Sửa dòng 6 thành DIMENSION: {số goal của case}
. Copy thông tin goals từ file circles.txt vào dưới dòng NODE_COORD_SECTION. Lưu ý xóa dòng ký tự trống để dòng EOF ngay bên dưới thông tin của goal (tránh trường hợp đọc sai file)


Bước 2: Chạy thuật toán
Ở đây chia thành 2 case, ứng với 2 trường hợp trước và sau khi cải tiến thuật toán
- Dòng 135 có hàm main(...) gồm 2 thông số
+ Tên của map: lấy tên của file case cần test ở bước 1: ví dụ "map_1_50_lb" 
+ Biến bool check trước hay sau cải tiến => Chạy 2 lần, 1 lần set thành true, 1 lần set thành false.

Tạo và chạy thử 1 map, push code rồi báo để tao check chuẩn hay chưa rồi tiếp tục chạy code tiếp.

Các kịch bản: (bao gồm cả low và high budget, nhớ tạo 2 file khác nhau để test (map_1_50_lb.tsp || map_1_50_hb.tsp))
** 1 Robot:
- 10 goal
- 20 goal
- 30 goal
- 50 goal
- 70 goal
- 100 goal
- 150 goal
- 200 goal
- 300 goal
- 400 goal
- 500 goal

** 100 goal
- 2 robot
- 3 robot
- 4 robot
- 5 robot
